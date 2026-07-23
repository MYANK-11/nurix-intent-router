import streamlit as st
from classifier import classify_intent, generate_handoff_summary
from examples import EXAMPLE_TRANSCRIPTS

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Nurix Intent Router",
    page_icon="🧠",
    layout="wide"
)

# ── API Key ───────────────────────────────────────────────────────────────────
GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", "")
if not GROQ_API_KEY:
    st.error("⚠️ Groq API key not found. Add it to `.streamlit/secrets.toml` as `GROQ_API_KEY = 'your_key'`")
    st.stop()

# ── Header ────────────────────────────────────────────────────────────────────
st.title("🧠 Intent-Based Conversation Router")
st.caption("Classifies customer support transcripts and decides: AI handles it, or escalate to a human agent.")
st.divider()

# ── Layout: two columns ───────────────────────────────────────────────────────
left, right = st.columns([1.1, 0.9], gap="large")

with left:
    st.subheader("📋 Transcript Input")

    # Example selector
    example_choice = st.selectbox(
        "Load an example transcript",
        options=["— paste your own —"] + list(EXAMPLE_TRANSCRIPTS.keys())
    )

    if example_choice != "— paste your own —":
        default_text = EXAMPLE_TRANSCRIPTS[example_choice].strip()
    else:
        default_text = ""

    transcript = st.text_area(
        label="Paste or edit the transcript below",
        value=default_text,
        height=320,
        placeholder="Customer: Hi, I need help with my order...\nAgent: Sure, can I get your order ID?\n..."
    )

    run = st.button("🔍 Classify Intent", type="primary", use_container_width=True)

with right:
    st.subheader("📊 Classification Result")

    if run:
        if not transcript.strip():
            st.warning("Please enter a transcript first.")
        else:
            with st.spinner("Classifying..."):
                result = classify_intent(transcript, GROQ_API_KEY)

            if result["intent"] == "error":
                st.error(f"Something went wrong: {result['reasoning']}")
            else:
                intent     = result["intent"]
                confidence = result["confidence"]
                escalate   = result["escalate"]
                reasoning  = result["reasoning"]

                # ── Intent badge ──────────────────────────────────────────────
                intent_labels = {
                    "lead_inquiry":        "💼 Lead Inquiry",
                    "billing_query":       "💳 Billing Query",
                    "product_complaint":   "😤 Product Complaint",
                    "cancellation_request":"❌ Cancellation Request",
                    "technical_issue":     "🔧 Technical Issue",
                    "general_inquiry":     "💬 General Inquiry",
                    "escalation_request":  "🚨 Escalation Request"
                }
                label = intent_labels.get(intent, intent)

                st.markdown(f"### {label}")

                # ── Confidence bar ────────────────────────────────────────────
                pct = int(confidence * 100)
                if confidence >= 0.75:
                    bar_color = "normal"
                elif confidence >= 0.60:
                    bar_color = "normal"
                else:
                    bar_color = "inverse"

                st.metric("Confidence Score", f"{pct}%")
                st.progress(confidence)

                st.divider()

                # ── Escalation decision ───────────────────────────────────────
                if escalate:
                    st.error("🔴 **ESCALATE TO HUMAN AGENT**")
                    st.markdown(
                        f"Confidence **{pct}%** is below the 60% threshold. "
                        "A human agent should take over this conversation."
                    )

                    # ── Handoff summary ───────────────────────────────────────
                    st.divider()
                    st.markdown("### 📋 Agent Handoff Briefing")
                    st.caption("Generated automatically for the human agent taking over.")

                    with st.spinner("Generating handoff summary..."):
                        summary = generate_handoff_summary(transcript, GROQ_API_KEY)

                    # Sentiment color
                    sentiment_colors = {
                        "Angry":     "🔴",
                        "Frustrated":"🟠",
                        "Neutral":   "🟡",
                        "Confused":  "🔵",
                        "Polite":    "🟢"
                    }
                    sentiment_icon = sentiment_colors.get(summary.get("sentiment", "Neutral"), "🟡")

                    urgency_colors = {
                        "High":   "🚨",
                        "Medium": "⚠️",
                        "Low":    "ℹ️"
                    }
                    urgency_icon = urgency_colors.get(summary.get("urgency", "Medium"), "⚠️")

                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown(f"**Customer Sentiment**")
                        st.markdown(f"{sentiment_icon} {summary.get('sentiment', 'Unknown')}")
                    with col2:
                        st.markdown(f"**Urgency Level**")
                        st.markdown(f"{urgency_icon} {summary.get('urgency', 'Medium')}")

                    st.markdown("**Core Issue**")
                    st.warning(summary.get("core_issue", "N/A"))

                    st.markdown("**Key Details**")
                    st.info(summary.get("key_details", "N/A"))

                    st.markdown("**Suggested First Action**")
                    st.success(summary.get("suggested_action", "N/A"))

                    with st.expander("View raw handoff JSON"):
                        st.json(summary)

                else:
                    st.success("✅ **AI CAN HANDLE THIS**")
                    st.markdown(
                        f"Confidence **{pct}%** is above the 60% threshold. "
                        "The AI agent can resolve this without human intervention."
                    )

                st.divider()

                # ── Reasoning ─────────────────────────────────────────────────
                st.markdown("**🧾 Model Reasoning**")
                st.info(reasoning)

                # ── Raw result (collapsed) ────────────────────────────────────
                with st.expander("View raw JSON output"):
                    st.json(result)

    else:
        st.markdown(
            """
            <div style='text-align:center; color:#888; margin-top: 80px;'>
                <p style='font-size:48px'>👈</p>
                <p>Load an example or paste a transcript,<br>then click <b>Classify Intent</b></p>
            </div>
            """,
            unsafe_allow_html=True
        )

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption("Built to demonstrate intent routing for enterprise AI voice & chat agents · Powered by Groq + LLaMA 3.3 70B")