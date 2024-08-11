{{
    config(
        materialized='citus_materialization',
        distribution_column='order_date'
    )
}}

with base as (
    select
        date(orders.order_date) as order_date
        , order_details.quantity
        , order_details.price
    from {{ source('store', 'orders') }} AS orders
    inner join {{ source('store', 'order_details') }} AS order_details
        on orders.order_id = order_details.order_id
)

, aggregated_sales as (
    select
        order_date
        , sum(quantity) as total_quantity
        , sum(price) as total_revenue
    from base
    group by order_date
)

select *
from aggregated_sales
order by order_date