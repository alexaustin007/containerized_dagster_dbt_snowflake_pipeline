
from dagster import asset
import subprocess

@asset
def dbt_transform(load_file_to_snowflake):
    subprocess.run(["dbt", "run", "--project-dir", "dbt_project", "--profiles-dir", "dbt_project"])
