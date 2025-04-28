# Psycopg- demo

A simple customer management system built in Python using PostgreSQL. This system allows you to manage customers through basic CRUD operations. The structure is modular to promote scalability and clarity.

---

## 📁 Project Structure

```
├── customers.py     # Logic for managing customers (create, update, retrieve, delete)
├── db.py            # Database connection and query execution (PostgreSQL abstraction)
├── main.py          # Entry point to interact with customer functions
├── example.env      # Sample environment variable file
├── requirements.txt # Dependencies for the project
├── venv/            # Virtual environment directory
├── __pycache__/     # Compiled Python files
```

---

## Features

- Create, update, retrieve, and delete customers
- PostgreSQL query abstraction layer via `db.py`
- Structured, modular, and clean architecture
- Environment variable configuration for database credentials

---

## Technologies

- Python 3
- PostgreSQL
- psycopg (PostgreSQL driver for Python)

---

## How to Use

1. Clone the repository:

   ```bash
   git clone https://github.com/LSCasas/psycopg.git
   cd psycopg
   ```

2. Set up a virtual environment and install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Configure your `.env` file based on `example.env` with your PostgreSQL credentials.

4. Run your project:

   ```bash
   python main.py
   ```

---

## Example

```python
import customers

# Create a new customer
customers.create_customer("test", "test@example.com", "CDMX")

# Get all customers
all_customers = customers.get_all_customers()
print(all_customers)
```

---

## Requirements

- Python 3.x
- PostgreSQL server (local or remote)
- psycopg library (`pip install psycopg`)
- Virtual environment recommended

---
