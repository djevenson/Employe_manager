from source.entities.Employee import Employee, Status
from source.use_cases.Interface.employe_repo import EmployeeRepo
from dataclasses import dataclass
from typing import Optional


@dataclass
class ActivateEmployeeInput:
    name : str
    def __post_init__(self):
        self.name = self.name.strip()


@dataclass
class EmployeeOutput:
        message : str
        employee : Optional[Employee]
        status : bool


class ActivateEmployee:
    def __init__(self, repository:EmployeeRepo) -> None:
        self.repository = repository

    def execute(self, data_input:ActivateEmployeeInput) -> EmployeeOutput:
        employee = self.repository.get_employee(data_input.name)
        if not employee:
            return EmployeeOutput(
                message = "Employee not found",
                employee = None, 
                status = False
            )
        if not employee.is_on_leave():
            return EmployeeOutput(
                message = f"Connot active an employee who is {employee.status}", 
                employee = employee, 
                status = False
            )
        employee.activate()
        employee = self.repository.update_employee(employee)
        return EmployeeOutput(
            message = "Employee activated Successfully", 
            employee = employee, 
            status = True
        )