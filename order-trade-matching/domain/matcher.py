from .models import Match, Order, Trade


def match_orders_trades(
    orders: list[Order], trades: list[Trade]
) -> list[Match]:  # noqa: E501
    """
    For a list of unique Quorus orders and a list of unique custodian trades
    for a single account, matches the orders to the trades.

    For example:
        - Order: Buy 50 AAPL on 2023-01-10 matches
            Trade: Buy 50 AAPL on 2023-01-10
        - Order1: Sell 1 BTC on 2023-02-20, Order2: Sell 0.5 BTC on 2023-02-20
            matches Trade: Sell 1.5 BTC @ $30001.48 on 2023-02-20
        - Order: Buy 100 USBOND on 2023-03-15 matches
            Trade1: Buy 50 USBOND @ $518.5 on 2023-03-15,
            Trade 2: Buy 50 USBOND @ $518.7 on 2023-03-15

    Args:
        orders (list[Order]): list of unique Quorus orders
        transactions (list[Trade]): list of unique custodian trades

    Returns:
        list[Match]: list of `Match`es containing the matched
        orders and trades and the allocated quantity
    """

    return []
