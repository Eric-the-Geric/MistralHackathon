#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 25 13:31:08 2024

@author: scli
"""

import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage

# Key: CcQg4IF1bBbmGinorbfFISos0Eqs4hpm
api_key = 'CcQg4IF1bBbmGinorbfFISos0Eqs4hpm'
model = "mistral-large-latest"

client = MistralClient(api_key=api_key)

chat_response = client.chat(
    model=model,
    messages=[ChatMessage(role="user", content="What is the best French cheese?")]
)

print(chat_response.choices[0].message.content)


from mistralai.client import MistralClient

# api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-embed"

client = MistralClient(api_key=api_key)

embeddings_response = client.embeddings(
    model=model,
    input=["Embed this sentence.", "As well as this one."]
)

print(embeddings_response)