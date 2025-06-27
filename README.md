# 🤖 Summarize Text from YouTube or Website using LangChain + Groq API

This Streamlit app summarizes content from **YouTube videos** or **webpages** using **LangChain** and the **Groq LLM API (Gemma-7B-It)**.

It intelligently loads the textual content from URLs and delivers a clean summary using advanced language models.

---

## 🚀 Features

- 📺 Summarize **YouTube** videos with transcript extraction  
- 🌐 Summarize **webpages** using UnstructuredIO's `UnstructuredURLLoader`  
- 🤖 Uses **Gemma-7B-It** model from **Groq API** via LangChain  
- 📦 Clean, minimal, and intuitive **Streamlit UI**  
- ✅ URL validation and user guidance in sidebar  

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Groq API (Gemma-7B-It)**
- **UnstructuredIO**
- **YoutubeLoader**

---
# 🤖 Summarize Text from YouTube or Website

---

## 🔧 Environment Setup

You can use `.env` for storing the API key:


GROQ_API_KEY=your_groq_api_key_here  
---
# 🧠 How It Works

- Loads content using `YoutubeLoader` or `UnstructuredURLLoader`
- Sends the text to a summarization chain powered by **LangChain + Groq**
- Returns a concise summary in natural language

---

## 📝 Example Usage

Enter a link like:

- [https://www.youtube.com/watch?v=dQw4w9WgXcQ](https://www.youtube.com/watch?v=dQw4w9WgXcQ)
- [https://en.wikipedia.org/wiki/Natural_language_processing](https://en.wikipedia.org/wiki/Natural_language_processing)

Click **"Summarize the Content from YT or Website"**, and let the model do the rest!

---

## 📌 Notes

- Only **public YouTube videos** with **transcripts** are supported  
- Summarization quality depends on video content/text structure  
- Model used: **Gemma-7B-It** via **Groq’s fast LLM hosting**
