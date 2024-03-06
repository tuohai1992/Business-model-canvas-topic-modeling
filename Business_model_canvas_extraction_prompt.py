import openai
import os
import re
import ast
import datetime
import pandas as pd
from bs4 import BeautifulSoup
import string
import json
import time


openai.api_key = "xxxxxxxxxx"
SYSTEM_PROMPT = """
You are a Named Entity Recognition (NER) system. Analyze sentences provided by the user and extract entities based on defined categories: Value Propositions, Customer Segments, Channels, Customer Relationships, Revenue Streams, Key Resources, Key Activities, Key Partnerships, and Cost Structure. Return results strictly in a structured dictionary format without additional comments or explanations.
"""

USER_PROMPT_1 = "Are you clear about your role?"

ASSISTANT_PROMPT_1 = "Yes, I understand my role. I'm ready to analyze the provided text and extract the relevant entities. Please provide the sentence for analysis."



PROMPT = (
    "Entity Definition:\n"
    "1. Value Propositions: This refers to the bundle of products and services that create value for a specific customer segment. Value propositions are the reasons why customers choose one company over another.\n"
    "2. Customer Segments: These are the different groups of people or organizations an enterprise aims to reach and serve. Customers can be segmented into distinct groups based on needs, behaviors, and other traits.\n"
    "3. Channels: This component describes how a company communicates with and reaches its customer segments to deliver a value proposition. Channels are touchpoints that play an important role in the customer experience.\n"
    "4. Customer Relationships: This outlines the types of relationships a company establishes with specific customer segments. Customer relationships may range from personal to automated, and from transactional to long-term.\n"
    "5. Revenue Streams: These represent the cash a company generates from each customer segment. A revenue stream can be one-time payments or recurring revenues from ongoing payments for a product or service.\n"
    "6. Key Resources: These are the most important assets required to make a business model work. They can be physical, financial, intellectual, or human.\n"
    "7. Key Activities: The most important activities in executing a company's value proposition. Key activities could be producing, problem-solving, or platform/network maintenance.\n"
    "8. Key Partnerships: Some activities are outsourced and some resources are acquired outside the enterprise. Key partnerships involve the network of suppliers and partners that make the business model work.\n"
    "9. Cost Structure: This describes all costs incurred to operate a business model. It could include fixed and variable costs, economies of scale, and economies of scope.\n"
    "\n"
    "Output should be in a structured dictionary format directly reflecting the analyzed input without any additional comments or preambles. If a category has no entities, list 'None' for that category.\n\n"    "Example Format:\n"
    "{{\n"
    "   'Value Propositions': ['sample value A', 'sample value B'],\n"
    "   'Customer Segments': ['sample segment'],\n"
    "   'Channels': ['sample channel'],\n"
    "   ... (other components as needed) ...\n"
    "}}\n\n"
    "Actual Input for Analysis:\n"
    "{}\n\n"
    "Directly provide the structured dictionary output based on the actual input, with no additional comments or narrative."
)
def openai_chat_completion_response(final_prompt):
  response = openai.ChatCompletion.create(
              model="gpt-4-1106-preview",
              messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": USER_PROMPT_1},
                    {"role": "assistant", "content": ASSISTANT_PROMPT_1},
                    {"role": "user", "content": final_prompt}
                ]
            )

  return response['choices'][0]['message']['content'].strip(" \n")





PROMPT_final = PROMPT.format(section_text)
ners = openai_chat_completion_response(PROMPT_final)

