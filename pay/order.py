# namespace UnitTest.Pay.Order

from enum import Enum
from typing import List
from dataclasses import dataclass, field


class OrderStatus(Enum):
    OPEN = 'open'
    PAID = 'paid'


@dataclass
class LineItem:
    name: str
    price: int
    quantity: int = 1
    
    @property
    def total(self) -> int:
        return self.price * self.quantity
   

@dataclass
class Order:
    line_items: List[LineItem] = field(default_factory=list)
    status: OrderStatus = OrderStatus.OPEN

    @property
    def total(self) -> int:
        return sum(item.total for item in self.line_items)
    
    def pay(self) -> None:
        self.status = OrderStatus.PAID
