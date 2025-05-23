with source_data as (
    select * from {{ source('MY_SCHEMA', 'your_table') }}
)

select
    id,
    name,
    value,
    value * 2 as double_value
from source_data 