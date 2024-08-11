select
    orders.*
    , case
        when orders.order_id % 2 != 0 then 'marketing'
        else 'finance'
    end as mart_flaging
from {{ ref('int_orders') }} as orders