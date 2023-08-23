from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Literal


@dataclass
class Order:
    symbol: str
    quantity: Decimal
    direction: Literal["buy", "sell"]
    submitted_date: datetime


@dataclass
class Trade:
    symbol: str
    cost_basis: Decimal
    quantity: Decimal
    price: Decimal
    direction: Literal["buy", "sell"]
    filled_date: datetime


@dataclass
class Match:
    order: Order
    trade: Trade
    allocated_quantity: Decimal
