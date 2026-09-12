import streamlit as st
from sql_generator import generate_sql
from db_utils import execute_query
from schema_parser import get_schema
import os

st.set_page_config(page_title="Text-to-SQL AI", layout="wide")
st.title("🗣️ Text-to-SQL AI Assistant")

schema = get_schema()
with st.sidebar:
    st.header("Database Schema")
    st.code(schema, language="sql")

question = st.text_input("Ask a question about your data (e.g., 'Who is the highest paid employee?'):")

if st.button("Generate & Run SQL"):
    if question:
        query = generate_sql(question, schema)
        st.subheader("Generated SQL")
        st.code(query, language="sql")
        
        st.subheader("Results")
        df, error = execute_query(query)
        if error:
            st.error(f"Error: {error}")
        else:
            st.dataframe(df)
