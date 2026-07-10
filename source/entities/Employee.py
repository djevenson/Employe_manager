from dataclasses import dataclass, field
from datetime import date, timezone, datetime
from enum import Enum


class InvalideDAta(Exception):
    pass


class Status(Enum):
    ACTIVE = "ACTIVE"
    ON_LEAVE = "ON_LEAVE"
    LAY_OFF = "LAY_OFF"
    RETIRE = "RETIRE"

def _now() -> datetime:
    return datetime.now(timezone.utc)

@dataclass
class Employee:
    name: str
    email: str
    post: str
    salary: int
    hire_date: datetime = field(default_factory=_now)
    status: Status = field(default=Status.ACTIVE)

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise InvalideDAta("Name connot be empty")
        if not self.email.strip():
            raise InvalideDAta("Email connot be empty") 
        if not self.post.strip():
            raise InvalideDAta("Post connot be empty")
        if self.salary < 100 :
            raise InvalideDAta("Salary connot be less than 100")
        self.name = self.name.strip()
        self.email = self.email.strip()
        self.post = self.post.strip()

    def activate(self) ->None:
        self.status = Status.ACTIVE

    def on_leave(self) -> None:
        self.status = Status.ON_LEAVE
        
    def lay_off(self) -> None :
        self.status = Status.LAY_OFF

    def retire(self) -> None:
        self.status = Status.RETIRE

    def raise_employe(self, amount:int) -> None:
        self.salary += amount

    def cut_pay(self, amount:int) -> None:
        self.salary -= amount
        
    def change_post(self, new_post : str) -> None:
        self.post = new_post

    def validate_raise(self, amount:int) -> bool:
        return amount < 10

    def validate_pay_cut(self, amount:int) -> bool:
        return (self.salary - amount) < 100

    def is_active(self) -> bool :
        return self.status == Status.ACTIVE
    
    def is_on_leave(self) -> bool :
        return self.status == Status.ON_LEAVE

    def is_fire(self) -> bool :
        return self.status == Status.LAY_OFF
    
    def is_retire(self) -> bool :
        return self.status == Status.RETIRE