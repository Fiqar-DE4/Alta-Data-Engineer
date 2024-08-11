select
    product_id::int as product_id
    , brand_id::int as brand_id
    , name as product_name
    , price as product_price
from {{ source('store', 'products') }}





-- -- Use the `ref` function to select from other models

-- select *
-- from {{ ref('stg_brands') }}
-- where id = 1
