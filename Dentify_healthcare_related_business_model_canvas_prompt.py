import openai
import os
import json

# set your OpenAI API key
openai.api_key = "xxxxxxxx"

SYSTEM_PROMPT = "You are a sophisticated and intelligent business analysis system. Your task is to analyze the provided business model canvas, which includes nine components: Value Propositions, Customer Segments, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, and Cost Structure. Determine if the given business model canvas includes healthcare-related business. Respond strictly with 'Y' for Yes if it contains healthcare-related business, or 'N' for No if it does not. Provide no additional information or explanation."

USER_PROMPT_1 = "Analyze this business model canvas and determine if the corresponding company includes healthcare-related business."


def analyze_healthcare_business(bmc_dict):
    """
    Analyze the given business model canvas dictionary to determine if the company includes healthcare-related business.
    """
    final_prompt = json.dumps(bmc_dict)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_PROMPT_1},
            {"role": "assistant", "content": final_prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip(" \n")
