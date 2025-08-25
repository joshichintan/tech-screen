# ORDERS_TO_MATCH = []

# TRADES_TO_MATCH = []

# TARGET_MATCHES = []

#--------------------------------

# from .models import Order, Trade, Match, TDirection
# from datetime import datetime, timezone
# from decimal import Decimal

# # Test Orders
# ORDERS_TO_MATCH = [
#     Order(
#         symbol="AAPL",
#         quantity=Decimal("100"),
#         direction="buy",
#         submitted_date=datetime(2024, 1, 1, 9, 30, 0, tzinfo=timezone.utc)
#     ),
#     Order(
#         symbol="AAPL", 
#         quantity=Decimal("50"),
#         direction="buy",
#         submitted_date=datetime(2024, 1, 1, 10, 0, 0, tzinfo=timezone.utc)
#     ),
#     Order(
#         symbol="GOOGL", 
#         quantity=Decimal("200"),
#         direction="sell",
#         submitted_date=datetime(2024, 1, 1, 9, 45, 0, tzinfo=timezone.utc)
#     ),
#     Order(
#         symbol="MSFT",
#         quantity=Decimal("75"),
#         direction="buy",
#         submitted_date=datetime(2024, 1, 1, 11, 0, 0, tzinfo=timezone.utc)
#     )
# ]

# # Test Trades (executions)
# TRADES_TO_MATCH = [
#     Trade(
#         symbol="AAPL",
#         cost_basis=Decimal("150.00"),
#         quantity=Decimal("100"),
#         price=Decimal("150.00"),
#         direction="buy",
#         filled_date=datetime(2024, 1, 1, 9, 35, 0, tzinfo=timezone.utc)
#     ),
#     Trade(
#         symbol="AAPL", 
#         cost_basis=Decimal("151.00"),
#         quantity=Decimal("50"),
#         price=Decimal("151.00"),
#         direction="buy",
#         filled_date=datetime(2024, 1, 1, 10, 5, 0, tzinfo=timezone.utc)
#     ),
#     Trade(
#         symbol="GOOGL",
#         cost_basis=Decimal("2800.00"),
#         quantity=Decimal("200"),
#         price=Decimal("2800.00"),
#         direction="sell",
#         filled_date=datetime(2024, 1, 1, 9, 50, 0, tzinfo=timezone.utc)
#     ),
#     Trade(
#         symbol="MSFT",
#         cost_basis=Decimal("380.00"),
#         quantity=Decimal("75"),
#         price=Decimal("380.00"),
#         direction="buy",
#         filled_date=datetime(2024, 1, 1, 11, 15, 0, tzinfo=timezone.utc)
#     )
# ]

# # Expected matches - these are what your matcher should return
# TARGET_MATCHES = [
#     Match(
#         order=ORDERS_TO_MATCH[0],  # order_1: AAPL BUY 100 @ 9:30
#         trade=TRADES_TO_MATCH[0],  # trade_1: AAPL BUY 100 @ 9:35
#         allocated_quantity=Decimal("100")
#     ),
#     Match(
#         order=ORDERS_TO_MATCH[1],  # order_2: AAPL BUY 50 @ 10:00
#         trade=TRADES_TO_MATCH[1],  # trade_2: AAPL BUY 50 @ 10:05
#         allocated_quantity=Decimal("50")
#     ),
#     Match(
#         order=ORDERS_TO_MATCH[2],  # order_3: GOOGL SELL 200 @ 9:45
#         trade=TRADES_TO_MATCH[2],  # trade_3: GOOGL SELL 200 @ 9:50
#         allocated_quantity=Decimal("200")
#     ),
#     Match(
#         order=ORDERS_TO_MATCH[3],  # order_4: MSFT BUY 75 @ 11:00
#         trade=TRADES_TO_MATCH[3],  # trade_4: MSFT BUY 75 @ 11:15
#         allocated_quantity=Decimal("75")
#     )
# ]
#--------------------------------

from .models import Order, Trade, Match, TDirection
from datetime import datetime, timezone
from decimal import Decimal

# Test Orders
ORDERS_TO_MATCH = [
    # Basic matches
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
    ),
    
    # Edge Case 1: Order with no matching trade (wrong direction)
    Order(
        symbol="TSLA",
        quantity=Decimal("150"),
        direction="buy",
        submitted_date=datetime(2024, 1, 1, 9, 15, 0, tzinfo=timezone.utc)
    ),
    
    # Edge Case 2: Order with no matching trade (wrong quantity)
    Order(
        symbol="NVDA",
        quantity=Decimal("300"),
        direction="sell",
        submitted_date=datetime(2024, 1, 1, 10, 30, 0, tzinfo=timezone.utc)
    ),
    
    # Edge Case 3: Order with no matching trade (wrong symbol)
    Order(
        symbol="AMZN",
        quantity=Decimal("80"),
        direction="buy",
        submitted_date=datetime(2024, 1, 1, 11, 30, 0, tzinfo=timezone.utc)
    ),
    
    # Edge Case 4: Multiple orders for same symbol/direction/quantity
    Order(
        symbol="META",
        quantity=Decimal("100"),
        direction="buy",
        submitted_date=datetime(2024, 1, 1, 8, 45, 0, tzinfo=timezone.utc)
    ),
    Order(
        symbol="META",
        quantity=Decimal("100"),
        direction="buy",
        submitted_date=datetime(2024, 1, 1, 9, 15, 0, tzinfo=timezone.utc)
    ),
    
    # Edge Case 5: Order submitted after trade (should not match)
    Order(
        symbol="NFLX",
        quantity=Decimal("120"),
        direction="sell",
        submitted_date=datetime(2024, 1, 1, 14, 0, 0, tzinfo=timezone.utc)
    )
]

# Test Trades (executions)
TRADES_TO_MATCH = [
    # Basic matches
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
    ),
    
    # Edge Case 1: Trade with wrong direction (TSLA SELL vs BUY order)
    Trade(
        symbol="TSLA",
        cost_basis=Decimal("250.00"),
        quantity=Decimal("150"),
        price=Decimal("250.00"),
        direction="sell",  # Different from order direction
        filled_date=datetime(2024, 1, 1, 9, 20, 0, tzinfo=timezone.utc)
    ),
    
    # Edge Case 2: Trade with wrong quantity (NVDA 250 vs 300 order)
    Trade(
        symbol="NVDA",
        cost_basis=Decimal("450.00"),
        quantity=Decimal("250"),  # Different from order quantity
        price=Decimal("450.00"),
        direction="sell",
        filled_date=datetime(2024, 1, 1, 10, 35, 0, tzinfo=timezone.utc)
    ),
    
    # Edge Case 3: Trade for different symbol (no AMZN order)
    Trade(
        symbol="CRM",  # Different symbol
        cost_basis=Decimal("200.00"),
        quantity=Decimal("80"),
        price=Decimal("200.00"),
        direction="buy",
        filled_date=datetime(2024, 1, 1, 11, 35, 0, tzinfo=timezone.utc)
    ),
    
    # Edge Case 4: Multiple trades for META (should match both orders)
    Trade(
        symbol="META",
        cost_basis=Decimal("320.00"),
        quantity=Decimal("100"),
        price=Decimal("320.00"),
        direction="buy",
        filled_date=datetime(2024, 1, 1, 8, 50, 0, tzinfo=timezone.utc)
    ),
    Trade(
        symbol="META",
        cost_basis=Decimal("321.00"),
        quantity=Decimal("100"),
        price=Decimal("321.00"),
        direction="buy",
        filled_date=datetime(2024, 1, 1, 9, 20, 0, tzinfo=timezone.utc)
    ),
    
    # Edge Case 5: Trade before order (should not match)
    Trade(
        symbol="NFLX",
        cost_basis=Decimal("180.00"),
        quantity=Decimal("120"),
        price=Decimal("180.00"),
        direction="sell",
        filled_date=datetime(2024, 1, 1, 13, 30, 0, tzinfo=timezone.utc)  # Before order
    )
]

# Expected matches - these are what your matcher should return
TARGET_MATCHES = [
    # Basic matches
    Match(
        order=ORDERS_TO_MATCH[0],  # AAPL BUY 100 @ 9:30
        trade=TRADES_TO_MATCH[0],  # AAPL BUY 100 @ 9:35
        allocated_quantity=Decimal("100")
    ),
    Match(
        order=ORDERS_TO_MATCH[1],  # AAPL BUY 50 @ 10:00
        trade=TRADES_TO_MATCH[1],  # AAPL BUY 50 @ 10:05
        allocated_quantity=Decimal("50")
    ),
    Match(
        order=ORDERS_TO_MATCH[2],  # GOOGL SELL 200 @ 9:45
        trade=TRADES_TO_MATCH[2],  # GOOGL SELL 200 @ 9:50
        allocated_quantity=Decimal("200")
    ),
    Match(
        order=ORDERS_TO_MATCH[3],  # MSFT BUY 75 @ 11:00
        trade=TRADES_TO_MATCH[3],  # MSFT BUY 75 @ 11:15
        allocated_quantity=Decimal("75")
    ),
    
    # Edge Case 4: Multiple META orders should match multiple META trades
    Match(
        order=ORDERS_TO_MATCH[7],  # META BUY 100 @ 8:45
        trade=TRADES_TO_MATCH[7],  # META BUY 100 @ 8:50
        allocated_quantity=Decimal("100")
    ),
    Match(
        order=ORDERS_TO_MATCH[8],  # META BUY 100 @ 9:15
        trade=TRADES_TO_MATCH[8],  # META BUY 100 @ 9:20
        allocated_quantity=Decimal("100")
    )
]

# Summary of what should NOT match:
# - TSLA order (wrong direction)
# - NVDA order (wrong quantity) 
# - AMZN order (no matching trade)
# - NFLX order (trade before order)
# - TSLA trade (wrong direction)
# - NVDA trade (wrong quantity)
# - CRM trade (wrong symbol)
# - NFLX trade (before order)