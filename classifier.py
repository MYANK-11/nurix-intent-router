# import os       # here we are just importing the library nothing else 
# import json
# import groq
 
# INTENTS = [                     # here we are making the list called Intents and the purpose of the list is that it tell us what type of intent is from the text 
#     "lead_inquiry",                
#     "billing_query",
#     "product_complaint",
#     "cancellation_request",
#     "technical_issue",
#     "general_inquiry",
#     "escalation_request"
# ]

# ESCALATION_THRESHOLD = 0.60                   # defining the threshold 

# SYSTEM_PROMPT = """You are an intent classification engine for an AI customer support system.   

# Given a customer support or sales chat transcript, you must:
# 1. Identify the primary intent from this fixed list:
#    - lead_inquiry: Customer is asking about a product/service with interest in purchasing
#    - billing_query: Questions about invoices, payments, charges, refunds
#    - product_complaint: Customer is unhappy about a product or service experience
#    - cancellation_request: Customer wants to cancel a subscription or order
#    - technical_issue: Customer is facing a bug, error, or technical problem
#    - general_inquiry: Generic question that doesn't fit other categories
#    - escalation_request: Customer is explicitly asking to speak to a human or manager

# 2. Assign a confidence score between 0.0 and 1.0 for your classification.

# You MUST respond with ONLY a valid JSON object in this exact format, nothing else:
# {
#   "intent": "<one of the 7 intents above>",
#   "confidence": <float between 0.0 and 1.0>,
#   "reasoning": "<one sentence explaining why>"
# }"""


# def classify_intent(transcript: str, api_key: str) -> dict:
#     """
#     Takes a raw chat transcript and returns intent, confidence, and escalation decision.
#     """
#     client = groq.Groq(api_key=api_key)

#     try:
#         response = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=[
#                 {"role": "system", "content": SYSTEM_PROMPT},
#                 {"role": "user", "content": f"Classify this transcript:\n\n{transcript}"}
#             ],
#             temperature=0.1,  # Low temp = more deterministic classification
#             max_tokens=200
#         )

#         raw = response.choices[0].message.content.strip()

#         # Clean up if model wraps in markdown fences
#         if raw.startswith("```"):
#             raw = raw.split("```")[1]
#             if raw.startswith("json"):
#                 raw = raw[4:]
#         raw = raw.strip()

#         result = json.loads(raw)

#         # Validate intent is from our list
#         if result["intent"] not in INTENTS:
#             result["intent"] = "general_inquiry"
#             result["confidence"] = 0.3

#         # Clamp confidence to 0-1
#         result["confidence"] = max(0.0, min(1.0, float(result["confidence"])))

#         # Core escalation decision
#         result["escalate"] = result["confidence"] < ESCALATION_THRESHOLD

#         return result

#     except json.JSONDecodeError:
#         return {
#             "intent": "general_inquiry",
#             "confidence": 0.0,
#             "reasoning": "Failed to parse model response.",
#             "escalate": True
#         }
#     except Exception as e:
#         return {
#             "intent": "error",
#             "confidence": 0.0,
#             "reasoning": str(e),
#             "escalate": True
#         }
    


# import os
# import json
# import groq

# INTENTS = [
#     "lead_inquiry",
#     "billing_query",
#     "product_complaint",
#     "cancellation_request",
#     "technical_issue",
#     "general_inquiry",
#     "escalation_request"
# ]

# ESCALATION_THRESHOLD = 0.60

# SYSTEM_PROMPT = """You are an intent classification engine for an AI customer support system used by Indian enterprises like Myntra, Tata, and Cult.fit.

# LANGUAGE NOTE: Transcripts may be in English, Hindi, or Hinglish (mixed Hindi-English). Classify based on meaning, not language. Examples of Hinglish you may see: "mera order abhi tak nahi aaya" (my order hasn't arrived), "paisa wapas karo" (give my money back), "kab aayega" (when will it come), "band karo subscription" (cancel subscription).

# Given a customer support or sales chat transcript, you must:
# 1. Identify the primary intent from this fixed list:

#    - lead_inquiry: Customer is asking about a product or service with interest in buying. They ask about price, features, demos, EMI, or trial options. They have NOT purchased yet.

#    - billing_query: Customer has questions about payments, invoices, charges, refunds, or GST receipts. They have already paid and are asking about that transaction.

#    - product_complaint: Customer is unhappy about their experience AFTER purchase. This includes delayed deliveries, wrong items, damaged products, poor service quality, or unmet expectations. NOTE: A late or missing delivery is a product_complaint, NOT a technical_issue.

#    - cancellation_request: Customer explicitly wants to stop, cancel, or not renew a subscription, membership, or order.

#    - technical_issue: Customer is facing a software bug, app crash, login error, or platform malfunction. This is ONLY for digital/technical problems — not physical delivery issues.

#    - general_inquiry: A vague or generic question that does not clearly fit any category above.

#    - escalation_request: Customer is explicitly demanding to speak to a human, senior agent, or manager. Phrases like "senior se baat karni hai", "manager ko bulao", or "I want to speak to a human" indicate this.

# 2. Assign a confidence score between 0.0 and 1.0 for your classification.
#    - Use high confidence (0.8-1.0) only when the intent is unmistakably clear.
#    - Use medium confidence (0.6-0.79) when the intent is likely but has some ambiguity.
#    - Use low confidence (below 0.6) when the transcript could reasonably fit multiple intents.

# You MUST respond with ONLY a valid JSON object in this exact format, nothing else:
# {
#   "intent": "<one of the 7 intents above>",
#   "confidence": <float between 0.0 and 1.0>,
#   "reasoning": "<one sentence explaining why>"
# }"""


# def classify_intent(transcript: str, api_key: str) -> dict:
#     """
#     Takes a raw chat transcript and returns intent, confidence, and escalation decision.
#     """
#     client = groq.Groq(api_key=api_key)

#     try:
#         response = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=[
#                 {"role": "system", "content": SYSTEM_PROMPT},
#                 {"role": "user", "content": f"Classify this transcript:\n\n{transcript}"}
#             ],
#             temperature=0.1,  # Low temp = more deterministic classification
#             max_tokens=200
#         )

#         raw = response.choices[0].message.content.strip()

#         # Clean up if model wraps in markdown fences
#         if raw.startswith("```"):
#             raw = raw.split("```")[1]
#             if raw.startswith("json"):
#                 raw = raw[4:]
#         raw = raw.strip()

#         result = json.loads(raw)

#         # Validate intent is from our list
#         if result["intent"] not in INTENTS:
#             result["intent"] = "general_inquiry"
#             result["confidence"] = 0.3

#         # Clamp confidence to 0-1
#         result["confidence"] = max(0.0, min(1.0, float(result["confidence"])))

#         # Core escalation decision
#         result["escalate"] = result["confidence"] < ESCALATION_THRESHOLD

#         return result

#     except json.JSONDecodeError:
#         return {
#             "intent": "general_inquiry",
#             "confidence": 0.0,
#             "reasoning": "Failed to parse model response.",
#             "escalate": True
#         }
#     except Exception as e:
#         return {
#             "intent": "error",
#             "confidence": 0.0,
#             "reasoning": str(e),
#             "escalate": True
#         }



import os
import json
import groq

INTENTS = [
    "lead_inquiry",
    "billing_query",
    "product_complaint",
    "cancellation_request",
    "technical_issue",
    "general_inquiry",
    "escalation_request"
]

ESCALATION_THRESHOLD = 0.60

SYSTEM_PROMPT = """You are an intent classification engine for an AI customer support system used by Indian enterprises like Myntra, Tata, and Cult.fit.

LANGUAGE NOTE: Transcripts may be in English, Hindi, or Hinglish (mixed Hindi-English). Classify based on meaning, not language. Examples of Hinglish you may see: "mera order abhi tak nahi aaya" (my order hasn't arrived), "paisa wapas karo" (give my money back), "kab aayega" (when will it come), "band karo subscription" (cancel subscription).

Given a customer support or sales chat transcript, you must:
1. Identify the primary intent from this fixed list:

   - lead_inquiry: Customer is asking about a product or service with interest in buying. They ask about price, features, demos, EMI, or trial options. They have NOT purchased yet.

   - billing_query: Customer has questions about payments, invoices, charges, refunds, or GST receipts. They have already paid and are asking about that transaction.

   - product_complaint: Customer is unhappy about their experience AFTER purchase. This includes delayed deliveries, wrong items, damaged products, poor service quality, or unmet expectations. NOTE: A late or missing delivery is a product_complaint, NOT a technical_issue.

   - cancellation_request: Customer explicitly wants to stop, cancel, or not renew a subscription, membership, or order.

   - technical_issue: Customer is facing a software bug, app crash, login error, or platform malfunction. This is ONLY for digital/technical problems — not physical delivery issues.

   - general_inquiry: A vague or generic question that does not clearly fit any category above.

   - escalation_request: Customer is explicitly demanding to speak to a human, senior agent, or manager. Phrases like "senior se baat karni hai", "manager ko bulao", or "I want to speak to a human" indicate this.

2. Assign a confidence score between 0.0 and 1.0 for your classification.
   - Use high confidence (0.8-1.0) only when the intent is unmistakably clear.
   - Use medium confidence (0.6-0.79) when the intent is likely but has some ambiguity.
   - Use low confidence (below 0.6) when the transcript could reasonably fit multiple intents.

You MUST respond with ONLY a valid JSON object in this exact format, nothing else:
{
  "intent": "<one of the 7 intents above>",
  "confidence": <float between 0.0 and 1.0>,
  "reasoning": "<one sentence explaining why>"
}"""


HANDOFF_PROMPT = """You are a handoff summary generator for an AI customer support system used by Indian enterprises.

A conversation has been flagged for human agent takeover because the AI was not confident enough to handle it.

Your job is to generate a concise briefing note for the human agent who will now take over. The agent has NOT read the transcript — your summary is all they get before they start talking to the customer.

You MUST respond with ONLY a valid JSON object in this exact format, nothing else:
{
  "sentiment": "<one of: Angry / Frustrated / Neutral / Confused / Polite>",
  "core_issue": "<one sentence — what is the customer's main problem>",
  "key_details": "<important specifics — order IDs, policy numbers, dates, amounts mentioned>",
  "urgency": "<one of: High / Medium / Low>",
  "suggested_action": "<one sentence — what should the human agent do first>"
}"""


def generate_handoff_summary(transcript: str, api_key: str) -> dict:
    """
    Generates a structured briefing note for the human agent taking over the conversation.
    Called only when escalate = True.
    """
    client = groq.Groq(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": HANDOFF_PROMPT},
                {"role": "user", "content": f"Generate a handoff summary for this transcript:\n\n{transcript}"}
            ],
            temperature=0.2,
            max_tokens=300
        )

        raw = response.choices[0].message.content.strip()

        # Clean markdown fences if present
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        raw = raw.strip()

        return json.loads(raw)

    except Exception as e:
        return {
            "sentiment": "Unknown",
            "core_issue": "Could not generate summary.",
            "key_details": "N/A",
            "urgency": "High",
            "suggested_action": "Read the full transcript carefully before responding."
        }


def classify_intent(transcript: str, api_key: str) -> dict:
    """
    Takes a raw chat transcript and returns intent, confidence, and escalation decision.
    """
    client = groq.Groq(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Classify this transcript:\n\n{transcript}"}
            ],
            temperature=0.1,  # Low temp = more deterministic classification
            max_tokens=200
        )

        raw = response.choices[0].message.content.strip()

        # Clean up if model wraps in markdown fences
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        raw = raw.strip()

        result = json.loads(raw)

        # Validate intent is from our list
        if result["intent"] not in INTENTS:
            result["intent"] = "general_inquiry"
            result["confidence"] = 0.3

        # Clamp confidence to 0-1
        result["confidence"] = max(0.0, min(1.0, float(result["confidence"])))

        # Core escalation decision
        result["escalate"] = result["confidence"] < ESCALATION_THRESHOLD

        return result

    except json.JSONDecodeError:
        return {
            "intent": "general_inquiry",
            "confidence": 0.0,
            "reasoning": "Failed to parse model response.",
            "escalate": True
        }
    except Exception as e:
        return {
            "intent": "error",
            "confidence": 0.0,
            "reasoning": str(e),
            "escalate": True
        }