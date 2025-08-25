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

Key = Tuple[str, TDirection, Decimal]

def match_orders_trades(
    orders: list[Order],
    trades: list[Trade],
) -> list[Match]:
    # Bucket by (symbol, direction, quantity)
    order_buckets: dict[Key, list[Order]] = defaultdict(list)
    trade_buckets: dict[Key, list[Trade]] = defaultdict(list)

    for o in orders:
        order_buckets[(o.symbol, o.direction, o.quantity)].append(o)
    for t in trades:
        trade_buckets[(t.symbol, t.direction, t.quantity)].append(t)

    # Sort by time inside each bucket
    for k in order_buckets:
        order_buckets[k].sort(key=lambda o: o.submitted_date)
    for k in trade_buckets:
        trade_buckets[k].sort(key=lambda t: t.filled_date)

    matches: List[Match] = []

    all_keys = set(order_buckets) | set(trade_buckets)

    for key in all_keys:
        print(key)
        o_list = order_buckets.get(key, [])
        t_list = trade_buckets.get(key, [])

        i = j = 0
        while i < len(o_list) and j < len(t_list):
            print(o_list[i])
            print(t_list[j])
            o = o_list[i]
            t = t_list[j]

            # Enforce time ordering: trade must be strictly after order
            if t.filled_date <= o.submitted_date:
                # Skip the trade if it occurs before the earliest unmatched order of this key
                j += 1
                continue
            print("match", o, t)
            # Keys already match by construction; quantities equal by key
            matches.append(Match(order=o, trade=t, allocated_quantity=o.quantity))
            i += 1
            j += 1

    return matches

