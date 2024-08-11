select 
    order_id::int as order_id
    , order_date::timestamp as order_at
    , customer_phone
from {{ source('store', 'orders') }}