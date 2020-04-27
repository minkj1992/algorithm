SELECT distinct a.user_id
from carts as a,
    (
        select cart_id
        from cart_products
        where name = "밀가루"
    ) as b
where a.id = b.cart_id
order by a.user_id;