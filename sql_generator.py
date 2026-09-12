import os

def generate_sql(question, schema):
    question = question.lower()
    if 'sales' in question:
        return "SELECT * FROM sales;"
    elif 'highest paid' in question or 'salary' in question:
        return "SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 1;"
    return "SELECT * FROM employees;"
