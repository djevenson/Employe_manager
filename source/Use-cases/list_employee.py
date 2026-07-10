from source.entities.Employee import Employee, Status
from source.use_cases.Interface.employe_repo import EmployeeRepo
from dataclasses import dataclass, field
from typing import List, Optional



@dataclass
class ListInput:
    status : Optional[Status] = None


@dataclass
class EmployeesOutput:
    total: int = 0
    employees: List[Employee] = field(default_factory = List)
    def __post_init__(self) ->None:
        self.total = len(employees)
    

class ListEmployee:
    def __init__(self, repository:EmployeeRepo) -> None:
        self.repository = repository

    def execute(self, list_input:ListInput) -> EmployeesOutput:
        if list_input.status is not None:
            employees = self.repository.get_by_status(list_input.status)
        else:
            employees = self.repository.get_all()
        return EmployeesOutput(employees = employees)
        