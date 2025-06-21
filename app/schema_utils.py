from sqlalchemy import inspect
from .db_connect import engine

def get_schema_prompt():
    inspector = inspect(engine)
    schema_parts = []
    for table in inspector.get_table_names():
        columns = [col['name'] for col in inspector.get_columns(table)]
        schema_parts.append(f"{table}: {', '.join(columns)}")
    return " | ".join(schema_parts)
