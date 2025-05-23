
from dagster_project.assets import load_file, run_dbt
from dagster import Definitions, load_assets_from_modules

defs = Definitions(
    assets=load_assets_from_modules([load_file, run_dbt])
)
