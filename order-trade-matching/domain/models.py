from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from typing import Literal

TDirection = Literal["buy", "sell"]


@dataclass(order=True)
class Order:
    symbol: str
    quantity: Decimal
    direction: TDirection
    submitted_date: datetime

    def __repr__(self) -> str:
        return f"Order({self.symbol}, {self.direction}, {self.submitted_date}, {self.quantity})"


@dataclass(order=True)
class Trade:
    symbol: str
    cost_basis: Decimal
    quantity: Decimal
    price: Decimal
    direction: TDirection
    filled_date: datetime

    def __repr__(self) -> str:
        return f"Trade({self.symbol}, {self.direction}, {self.filled_date}, {self.quantity})"


@dataclass(order=True)
class Match:
    order: Order
    trade: Trade
    allocated_quantity: Decimal

    def __repr__(self) -> str:
        return f"Order: {self.order} | Trade: {self.trade}, Alloc. Quant.: {self.allocated_quantity})"  # noqa: E501
