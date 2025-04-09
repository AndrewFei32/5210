#!/usr/bin/env python
# coding: utf-8


# In[4]:


import streamlit as st
from src.agents import TranslationAgent, SummarizerAgent, SentimentAgent, KeywordAgent, HeadlineAgent

# Set up Streamlit page
st.set_page_config(page_title="🌍 GlobalText Insight", layout="wide")
st.title("🌍 GlobalText Insight - Multilingual News Analyzer")

# Text input area
st.subheader("📄 Input News Content (Any Language)")
input_text = st.text_area("Paste your news article here:", height=300)

# Initialize agents
translator = TranslationAgent()
summarizer = SummarizerAgent()
sentimenter = SentimentAgent()
keyworder = KeywordAgent()
headliner = HeadlineAgent()



# In[7]:


# Run analysis when button is clicked
if st.button("Analyze"):
    if not input_text.strip():
        st.warning("Please enter some content before clicking Analyze.")
    else:
        with st.spinner(" Agents are analyzing the content..."):
            # Agent workflow
            translated = translator.run(input_text)
            summary = summarizer.run(translated)
            sentiment = sentimenter.run(translated)
            keywords = keyworder.run(translated)
            headline = headliner.run(translated)

        st.success(" Analysis Complete!")

        # Display results
        st.subheader("Translated Content")
        st.write(translated)

        st.subheader("Summary")
        st.write(summary)

        st.subheader("Sentiment")
        st.write(sentiment)

        st.subheader("Keywords & Tags")
        st.write(keywords)

        st.subheader("Suggested Headline")
        st.write(headline)

# Footer        
st.markdown("""
---
© 2025 GlobalText Insight | Powered by OpenAI & Streamlit
""")


# In[ ]:




