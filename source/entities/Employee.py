from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class Status(Enum):
    ACTIVE = "ACTIVE"
    ON_LEAVE = "ON_LEAVE"
    LICENCIE = "LICENCIE"
    RETRAITE = "RETRAITE"




class Email:
    def __init__(self, addresse:str):
        if not "@" in addresse or "." not in addresse:
            raise ValueError("Invalid addresse email!!! ")
        self.email = addresse.strip()

    def __str__(self):
        return self.email




class Money:
    def __init__(self, amount:int, currency:Currency):
        if amount < 0 :
            return ValueError("Salary connot be negative")
        if currency not in Currency:
            raise ValueError("Currency unavailable")
        self.amount=amount
        self.currency=currency
    
    def __str__(self):
        return f"{self.amount} {self.currency}"




@dataclass
class Employee:
    firstName: str
    lastName: str
    phone: str
    email: str
    birthDay: date
    hireDate: date
    position: str
    departement: str
    salary: int
    status: Status = field(default=Status.ACTIVE)

    def __post_init__(self):
        pass

    def licency(self) -> None :
        if self.status not in (Status.ACTIVE, Status.ON_LEAVE):
            raise ValueError(
                f"Connot licency an employee who is {self.status}"
            )
        self.status = Status.LICENCIE
    
    def is_active(self) -> bool :
        return self.status == Status.ACTIVE
    
    def is_on_leave(self) -> bool :
        return self.status == Status.ON_LEAVE

    def is_licencie(self) -> bool :
        return self.status == Status.LICENCIE
    
    def is_retraite(self) -> bool :
        return self.status == Status.RETRAITE

    

    

