from .models import Match, Order, Trade


def match_orders_trades(
    orders: list[Order], trades: list[Trade]
) -> list[Match]:  # noqa: E501
    """
    For a list of unique Quorus orders and a list of unique custodian trades
    for a single account, matches the orders to the trades.

    Args:
        orders (list[Order]): list of unique Quorus orders
        transactions (list[Trade]): list of unique custodian trades

    Returns:
        list[Match]: list of `Match`es containing the matched
        orders and trades and the allocated quantity
    """

    return []
