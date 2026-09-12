import sqlite3

def init_db(db_path="database.db"):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY, name TEXT, department TEXT, salary INTEGER)''')
    c.execute('''CREATE TABLE IF NOT EXISTS sales (
        id INTEGER PRIMARY KEY, employee_id INTEGER, amount REAL, date TEXT)''')
    
    c.execute("DELETE FROM employees")
    c.execute("DELETE FROM sales")
    
    c.executemany("INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", 
                  [('Alice', 'Engineering', 95000), ('Bob', 'Sales', 75000), ('Charlie', 'Marketing', 65000)])
    
    conn.commit()
    conn.close()
    print("Sample database initialized.")

if __name__ == "__main__":
    init_db()
