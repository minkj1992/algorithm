# select a.cart_id
# from
#     (
#         select cart_id
#         from cart_products
#         where name = "우유"
#     ) a, cart_products b
# where a.cart_id = b.cart_id and b.name = "요거트"
# order by b.id;
#
# from collections import Counter
# from itertools import permutations, combinations
