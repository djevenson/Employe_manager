from source.entities.Employee import Employee, Status
from source.use_cases.Interface.employe_repo import EmployeRepo
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
    def __init__(self, repository:EmployeRepo) -> None:
        self.repository = repository

    def execute(self, list_input:ListInput) -> EmployeeOutput:
        if list_input.status is not None:
            employees = self.repository.find_by_status(list_input.status)
        else:
            employees = self.repository.get_all()
        return EmployeeOutput(employees = employees)
        