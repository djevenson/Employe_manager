from abc import ABC, abstractmethod
from source.entities.Employee import Employee, Status
from typing import List, Optional

class EmployeeRepo(ABC):

    @abstractmethod
    def add_employee(self, employee: Employee) -> Optional[Employee]:
        ...

    @abstractmethod
    def get_employee(self, name: str) -> Optional[Employee]:
        ...

    @abstractmethod
    def get_by_status(self, status:Status) -> List[Employee]:
        ...

    @abstractmethod
    def get_all(self) -> List[Employee]:
        ...

    @abstractmethod
    def update_employee(self, name:str, status:Status) -> Optional[Employee]:
        ...

    @abstractmethod
    def update_employee_salary(self, name:str, amount:int) -> Optional[Employee]:
        ...