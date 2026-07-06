from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeRepo
from dataclasses import dataclass
from typing import Optional


@dataclass
class EmployeInput:
    name: str
    def __post_init__(self):
        self.name = self.name.strip()


@dataclass
class EmployeeOutput:
    message : str = ""
    employee : Optional[Employee]
    status : bool


class GetEmployee:
    def __init__(self, repository:EmployeRepo):
        self.repository = repository

    def execute(self, input_data: EmployeInput) -> EmployeeOutput:
        employee = self.repository.get_employee(informations.name)
        if not employee:
            return EmployeeOutput(
                message="Employee not found",
                employee = None,
                status = False
            )
        return EmployeeOutput(employee = employee, status = True)