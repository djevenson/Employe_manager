from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeRepo
from dataclasses import dataclass
from typing import  Optional


@dataclass
class EmployeInput:
    name : str
    def __post_init__(self):
        self.name = self.name.strip()


@dataclass
class EmployeeOutput:
    message : str = ""
    employee = Optional[Employee]
    status : bool


class ActivateeEmployee:
    def __init__(self, repository:EmployeRepo) -> None:
        self.repository = repository

    def execute(self, data_input:EmployeInput) -> EmployeeOutput:
        employee = self.repository.get_employee(data_input.name)
        if not employee:
            return EmployeeOutput(message = "Employee not found", False)
        if not employee.is_active:
            return EmployeeOutput(
                message = f"Connot on-leave an employee who is {employee.status}", 
                employee = employee, 
                status = False
            )
        employee.on_leave()
        employee = repository.update_employee(employee)
        return EmployeeOutput(
            message = "Employee on-leaved Successfully", 
            employee = employee, 
            status = True
            )
