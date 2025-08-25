# ORDERS_TO_MATCH = []

# TRADES_TO_MATCH = []

# TARGET_MATCHES = []

#--------------------------------

from .models import Order, Trade, Match, TDirection
from datetime import datetime, timezone
from decimal import Decimal

# Test Orders
ORDERS_TO_MATCH = [
    Order(
        symbol="AAPL",
        quantity=Decimal("100"),
        direction="buy",
        submitted_date=datetime(2024, 1, 1, 9, 30, 0, tzinfo=timezone.utc)
    ),
    Order(
        symbol="AAPL", 
        quantity=Decimal("50"),
        direction="buy",
        submitted_date=datetime(2024, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
    ),
    Order(
        symbol="GOOGL", 
        quantity=Decimal("200"),
        direction="sell",
        submitted_date=datetime(2024, 1, 1, 9, 45, 0, tzinfo=timezone.utc)
    ),
    Order(
        symbol="MSFT",
        quantity=Decimal("75"),
        direction="buy",
        submitted_date=datetime(2024, 1, 1, 11, 0, 0, tzinfo=timezone.utc)
    )
]

# Test Trades (executions)
TRADES_TO_MATCH = [
    Trade(
        symbol="AAPL",
        cost_basis=Decimal("150.00"),
        quantity=Decimal("100"),
        price=Decimal("150.00"),
        direction="buy",
        filled_date=datetime(2024, 1, 1, 9, 35, 0, tzinfo=timezone.utc)
    ),
    Trade(
        symbol="AAPL", 
        cost_basis=Decimal("151.00"),
        quantity=Decimal("50"),
        price=Decimal("151.00"),
        direction="buy",
        filled_date=datetime(2024, 1, 1, 10, 5, 0, tzinfo=timezone.utc)
    ),
    Trade(
        symbol="GOOGL",
        cost_basis=Decimal("2800.00"),
        quantity=Decimal("200"),
        price=Decimal("2800.00"),
        direction="sell",
        filled_date=datetime(2024, 1, 1, 9, 50, 0, tzinfo=timezone.utc)
    ),
    Trade(
        symbol="MSFT",
        cost_basis=Decimal("380.00"),
        quantity=Decimal("75"),
        price=Decimal("380.00"),
        direction="buy",
        filled_date=datetime(2024, 1, 1, 11, 15, 0, tzinfo=timezone.utc)
    )
]

# Expected matches - these are what your matcher should return
TARGET_MATCHES = [
    Match(
        order=ORDERS_TO_MATCH[0],  # order_1: AAPL BUY 100 @ 9:30
        trade=TRADES_TO_MATCH[0],  # trade_1: AAPL BUY 100 @ 9:35
        allocated_quantity=Decimal("100")
    ),
    Match(
        order=ORDERS_TO_MATCH[1],  # order_2: AAPL BUY 50 @ 10:00
        trade=TRADES_TO_MATCH[1],  # trade_2: AAPL BUY 50 @ 10:05
        allocated_quantity=Decimal("50")
    ),
    Match(
        order=ORDERS_TO_MATCH[2],  # order_3: GOOGL SELL 200 @ 9:45
        trade=TRADES_TO_MATCH[2],  # trade_3: GOOGL SELL 200 @ 9:50
        allocated_quantity=Decimal("200")
    ),
    Match(
        order=ORDERS_TO_MATCH[3],  # order_4: MSFT BUY 75 @ 11:00
        trade=TRADES_TO_MATCH[3],  # trade_4: MSFT BUY 75 @ 11:15
        allocated_quantity=Decimal("75")
    )
]
