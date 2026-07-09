from abc import ABC, abstracmethod
from source.entities.Employee import Employee, Status
from typing import List, Optional

class employee(ABC):

    @abstracmethod
    def add_employee(self, employee: Employer) -> Employee:
        ...

    @abstracmethod
    def get_employee(self, employee: Employer) -> Optional[Employee]:
        ...

    @abstracmethod
    def get_by_status(self, status:Status) -> List[Employee]:
        ...

    @abstracmethod
    def get_all(self) -> List[Employee]:
        ...

    @abstracmethod
    def update_employee(self, employee : Employee) -> Employee:
        ...