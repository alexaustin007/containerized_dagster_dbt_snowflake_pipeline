
from dagster import asset
import pandas as pd
import snowflake.connector
import os

@asset
def load_file_to_snowflake():
    df = pd.read_csv("data/input_data.csv")

    conn = snowflake.connector.connect(
        user=os.getenv("SNOWFLAKE_USER"),
        password=os.getenv("SNOWFLAKE_PASSWORD"),
        account=os.getenv("SNOWFLAKE_ACCOUNT"),
        database=os.getenv("SNOWFLAKE_DATABASE"),
        schema=os.getenv("SNOWFLAKE_SCHEMA")
    )
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(
    "INSERT INTO your_table (id, name, value) VALUES (%s, %s, %s)",
    (int(row["id"]), str(row["name"]), int(row["value"]))
)


    conn.commit()
    cursor.close()
    conn.close()
