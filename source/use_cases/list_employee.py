from source.entities.Employee import Employee, Status
from source.use_cases.Interface.employe_repo import EmployeeRepo
from dataclasses import dataclass, field
from typing import List, Optional



@dataclass
class ListEmployeesInput:
    status : Optional[Status] = None


@dataclass
class EmployeesOutput:
    employees: List[Employee] = field(default_factory = list)
    total: int = 0
    def __post_init__(self) ->None:
        self.total = len(self.employees)
    

class ListEmployees:
    def __init__(self, repository:EmployeeRepo) -> None:
        self.repository = repository

    def execute(self, list_input:ListEmployeesInput) -> EmployeesOutput:
        if list_input.status is not None:
            employees = self.repository.get_by_status(list_input.status)
        else:
            employees = self.repository.get_all()
        employees_sorted = sorted(employees, key=lambda e: e.hire_date, reverse=True)
        return EmployeesOutput(employees = employees_sorted)                