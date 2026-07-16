from abc import ABC, abstractmethod
from source.entities.Employee import Employee, Status
from typing import List, Optional

class EmployeeRepo(ABC):

    @abstractmethod
    def add_employee(self, employee: Employee) -> Optional[Employee]:
        ...

    @abstractmethod
    def get_employee(self, id: int) -> Optional[Employee]:
        ...

    @abstractmethod
    def get_by_status(self, status:Status) -> List[Employee]:
        ...

    @abstractmethod
    def get_all(self) -> List[Employee]:
        ...

    @abstractmethod
    def update_employee(self, id:int, status:Status) -> Optional[Employee]:
        ...

    @abstractmethod
    def change_employee_post(self, id:int, post:str) -> Optional[Employee]:
        ...

    @abstractmethod
    def raise_employee_salary(self, id:int, amount:int) -> Optional[Employee]:
        ...
    
    @abstractmethod
    def cut_employee_salary(self, id:int, amount:int) -> Optional[Employee]:
        ...

    