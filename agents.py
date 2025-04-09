#!/usr/bin/env python
# coding: utf-8

# In[1]:


from openai import OpenAI
import os


# In[2]:


# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class TranslationAgent:
    def run(self, text: str) -> str:
        prompt = f"Please translate the following news content into English:\n{text}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            timeout=60
        )
        return response.choices[0].message.content.strip()

class SummarizerAgent:
    def run(self, text: str) -> str:
        prompt = f"Please provide a concise and clear summary of the following content:\n{text}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            timeout=60
        )
        return response.choices[0].message.content.strip()

class SentimentAgent:
    def run(self, text: str) -> str:
        prompt = f"Please determine the sentiment of the following content (positive, neutral, or negative) and briefly explain why:\n{text}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            timeout=60
        )
        return response.choices[0].message.content.strip()

class KeywordAgent:
    def run(self, text: str) -> str:
        prompt = f"Extract 3 to 5 key keywords and 1 to 2 topic tags from the following content. Format the output as: Keywords: ... Tags: ...\n{text}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            timeout=60
        )
        return response.choices[0].message.content.strip()

class HeadlineAgent:
    def run(self, text: str) -> str:
        prompt = f"Generate a concise and engaging English headline for the following news content:\n{text}"
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            timeout=60
        )
        return response.choices[0].message.content.strip()


# In[ ]:




