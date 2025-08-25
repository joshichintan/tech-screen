from .models import Match, Order, Trade, TDirection, Decimal
from collections import defaultdict
from typing import Tuple, List


# def match_orders_trades(
#     orders: list[Order], trades: list[Trade]
# ) -> list[Match]:  # noqa: E501
#     """
#     For a list of unique Quorus orders and a list of unique custodian trades
#     for a single account, matches the orders to the trades.

#     Args:
#         orders (list[Order]): list of unique Quorus orders
#         transactions (list[Trade]): list of unique custodian trades

#     Returns:
#         list[Match]: list of `Match`es containing the matched
#         orders and trades and the allocated quantity
#     """

#     return []
Key = Tuple[str, TDirection]

def match_orders_trades(
    orders: list[Order],
    trades: list[Trade],
) -> list[Match]:

    order_buckets: dict[Key, list[Order]] = defaultdict(list)
    trade_buckets: dict[Key, list[Trade]] = defaultdict(list)

    for o in orders:
        order_buckets[(o.symbol, o.direction)].append(o)
    for t in trades:
        trade_buckets[(t.symbol, t.direction)].append(t)

    # Sorting orders and trades based on time
    for k in order_buckets:
        order_buckets[k].sort(key=lambda o: (o.submitted_date, o.quantity))
    for k in trade_buckets:
        trade_buckets[k].sort(key=lambda t: (t.filled_date, t.quantity))

    matches: List[Match] = []

    all_keys = set(order_buckets) | set(trade_buckets)
    print("all_keys", all_keys)
    for key in all_keys:
        o_list = order_buckets.get(key, [])
        t_list = trade_buckets.get(key, [])

        # Track left over
        print(key)
        print("o_list", o_list)
        print("t_list", t_list)
        print("--------------------------------")
        o_remaining = [o.quantity for o in o_list]
        t_remaining = [t.quantity for t in t_list]

        # two pointers to iterate through orders and trades
        oi = ti = 0
        while oi < len(o_list) and ti < len(t_list):
            o = o_list[oi]
            t = t_list[ti]

            # orders must be before trades
            if t.filled_date < o.submitted_date:
                print("trade before order", t, o)
                ti += 1
                continue

            # allocate the minimum of the remaining quantities
            alloc = min(o_remaining[oi], t_remaining[ti])

            # if quantity is greater than 0, add the match
            if alloc > Decimal(0):
                matches.append(Match(order=o, trade=t, allocated_quantity=alloc))
                print('Allocating', alloc,"match", o, t,)
                o_remaining[oi] -= alloc
                t_remaining[ti] -= alloc
            print("o_remaining", o_remaining)
            print("t_remaining", t_remaining)

            # if either trade or order is fullfilled, move the pointer
            if o_remaining[oi] == Decimal(0):
                print("order is fullfilled", o_remaining[oi])
                oi += 1
            if t_remaining[ti] == Decimal(0):
                print("trade is fullfilled", t_remaining[ti])
                ti += 1
        print('\n\n')

    return matches