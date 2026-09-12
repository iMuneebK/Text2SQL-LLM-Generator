# 🗣️ Text-to-SQL AI Assistant

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-red.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-green.svg)

A Natural Language to SQL query generator that takes conversational English questions and converts them to precise SQL queries using LLMs and few-shot prompting.

## Features
- 💬 Natural language interface for database querying
- 🔍 Automatic schema detection and parsing
- 📊 Real-time execution and visualization of results
- 🎯 Few-shot prompting for high accuracy

## Architecture
User Input -> Streamlit UI -> Prompt Construction (w/ Schema) -> LLM -> SQL Query -> DB Executor -> Results.

## Quick Start
```bash
pip install -r requirements.txt
python sample_data.py
streamlit run app.py
```
