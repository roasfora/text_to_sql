import os
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
DATABASE_URL = os.getenv("DB_URL")

# Create engine
engine = create_engine(DATABASE_URL)

# Path to your data directory
DATA_DIR = os.path.join(os.path.dirname(__file__), "data")

# CSV filenames and matching table names
csv_tables = {
    "Product.csv": "product",
    "Region.csv": "region",
    "Reseller.csv": "reseller",
    "Sales.csv": "sales",
    "Salesperson.csv": "salesperson",
    "SalespersonRegion.csv": "salespersonregion",
    "Targets.csv": "targets"
}

# Function to load each CSV with lowercase columns
def load_csv_to_postgres(file_name, table_name):
    file_path = os.path.join(DATA_DIR, file_name)
    print(f"Loading {file_name} into table {table_name}...")

    df = pd.read_csv(file_path, sep="\t", on_bad_lines="skip")
    df.columns = [col.lower() for col in df.columns]  # Convert column names to lowercase

    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f" Loaded {len(df)} rows into {table_name}")

# Loop through and load all
for file_name, table_name in csv_tables.items():
    load_csv_to_postgres(file_name, table_name)
