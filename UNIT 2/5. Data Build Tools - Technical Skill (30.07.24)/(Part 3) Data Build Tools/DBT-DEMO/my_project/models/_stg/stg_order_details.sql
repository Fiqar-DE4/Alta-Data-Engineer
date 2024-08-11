select 
    order_detail_id::int as order_detail_id
    , order_id::int as order_id
    , product_id::int as product_id
    , quantity as order_qty
    , price as unit_sales
from {{ source('store', 'order_details') }}