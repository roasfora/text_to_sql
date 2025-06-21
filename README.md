
# 🧠 Text-to-SQL Business Intelligence Agent

A lightweight AI-powered FastAPI application that translates natural language queries into SQL using a fine-tuned T5 model and executes them on a PostgreSQL database. It enables non-technical users to explore data with plain English.

---

## 🚀 Features

- Natural language → SQL with `T5-SQL`
- Runs on `FastAPI` with a RESTful `/query` endpoint
- Executes queries on `PostgreSQL` (Render-hosted)
- Logs and returns results as structured JSON
- Designed for future integration with:
  - 🧠 FAISS + Pydantic for memory and context
  - 📊 Dashboards or visualizations
  - 🗃️ Query history

---

## 📁 Project Structure

```
text_to_sql/
├── app/
│   ├── main.py                # FastAPI app entrypoint
│   ├── agent.py               # T5-SQL inference logic
│   ├── db_connect.py          # SQLAlchemy DB connection
│   ├── schema_utils.py        # Builds schema prompt for model
│   ├── models.py              # Pydantic request/response models
├── data/                      # Raw CSVs
├── load_data.py              # Load CSVs into PostgreSQL (lowercase schema)
├── test_query.py             # Test script for POST /query
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repo

```bash
git clone <repo-url>
cd text_to_sql
```

### 2. Create `.env`

```
DB_URL=postgresql://<user>:<password>@<host>:<port>/<dbname>
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Load the Data

```bash
python load_data.py
```

This loads all CSVs from `/data` and saves tables with lowercase names and columns.

---

## 🧪 Run the App

```bash
uvicorn app.main:app --reload
```

Open Swagger UI at:  
👉 [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🔁 Test It

```bash
python test_query.py
```

Or use `curl`:
```bash
curl -X POST http://localhost:8000/query -H "Content-Type: application/json" -d "{"question": "What are the total sales by region?"}"
```

---

## 🧠 Future Improvements

- Memory storage via FAISS + Pydantic
- Automatic charting with matplotlib or Vega
- Add Streamlit frontend or React dashboard
- Query validation and correction
- Retry + fallback LLMs (e.g., SQLCoder)

---

## 🛡 License

MIT License. Open source and free to use.

---

## 👨‍💻 Author

Rodrigo Moutinho

roasfora@gmail.com
