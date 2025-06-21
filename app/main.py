from fastapi import FastAPI
from .models import QueryRequest, QueryResponse
from .agent import text_to_sql
from .schema_utils import get_schema_prompt
from .db_connect import engine
import pandas as pd

app = FastAPI()

@app.post("/query", response_model=QueryResponse)
def query_handler(request: QueryRequest):
    schema = get_schema_prompt()
    sql = text_to_sql(request.question, schema)

    try:
        df = pd.read_sql(sql, con=engine)
        result = df.to_dict(orient="records")
    except Exception as e:
        result = [{"error": str(e)}]

    return QueryResponse(sql=sql, result=result)
