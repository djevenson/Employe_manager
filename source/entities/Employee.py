from dataclasses import dataclass, field
from datetime import date, timezone
from enum import Enum


class Status(Enum):
    ACTIVE = "ACTIVE"
    ON_LEAVE = "ON_LEAVE"
    LAY_OFF = "LAY_OFF"
    RETRAITE = "RETRAITE"

def _now() -> datetime:
    return datetime.now(timezone.uct)

@dataclass
class Employee:
    name: str
    email: str
    hire_date: datetime = field(default=_now())
    post: str
    salary: int
    status: Status = field(default=Status.ACTIVE)

    def __post_init__(self):
        pass

    def activate(self) ->None:
        self.status = Status.ACTIVE

    def on_leave(self) -> None:
        self.status = status.ON_LEAVE
        
    def lay_off(self) -> None :
        self.status = Status.LICENCIE

    def retraite(self) -> None:
        self.status = Status.RETRAITE

    def raise_employe(self, amount:int) -> None:
        self.salary += amount

    def cut_pay(self, amount:int) -> None:
        self.salary -= amount
        
    def validate_raise(self, amount:int) -> None:
        return amount < 10

    def validate_pay_cut(self, amount:int) -> bool:
        return (self.salary - amount) < 100

    def is_active(self) -> bool :
        return self.status == Status.ACTIVE
    
    def is_on_leave(self) -> bool :
        return self.status == Status.ON_LEAVE

    def is_licencie(self) -> bool :
        return self.status == Status.LICENCIE
    
    def is_retraite(self) -> bool :
        return self.status == Status.RETRAITE

    

    

