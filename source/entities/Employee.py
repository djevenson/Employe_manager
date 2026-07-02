from dataclasses import dataclass, field
from datetime import date
from enum import Enum


class Status(Enum):
    ACTIVE = "ACTIVE"
    ON_LEAVE = "ON_LEAVE"
    LICENCIE = "LICENCIE"
    RETRAITE = "RETRAITE"


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

    def __post_init__(self) -> None:
        if self.salary < 0 :
            raise ValueError("Salary connot be negative!!")

        if "@" not in self.email() or "." not in self.email.strip():
            raise ValueError("Email invalide!!")
        self.email=self.email.strip()


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

    

    

