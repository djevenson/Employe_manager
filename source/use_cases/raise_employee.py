from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeeRepo
from dataclasses import dataclass
from typing import  Optional


@dataclass
class RaiseEmployeeInput:
    name : str
    amount : int
    def __post_init__(self):
        self.name = self.name.strip()


@dataclass
class EmployeeOutput:
    employee : Optional[Employee]
    status : bool
    message : str = ""


class RaiseEmployee:
    def __init__(self, repository:EmployeeRepo) -> None:
        self.repository = repository

    def execute(self, data_input:RaiseEmployeeInput) -> EmployeeOutput:
        employee = self.repository.get_employee(data_input.name)
        if not employee:
            return EmployeeOutput(
                message = "Employee not found",
                employee = None, 
                status = False
            )
        if not employee.validate_raise(data_input.amount):
            return EmployeeOutput(
                message = "Amount must be greater than 10", 
                employee = employee, 
                status = False
            )
        if not employee.is_active() or not employee.is_on_leave():
            return EmployeeOutput(
                message = f"Connot raise an employee who is {employee.status}", 
                employee = employee, 
                status = False
            )
        employee.raise_employe(data_input.amount)
        employee = self.repository.raise_employee_salary(employee.name, data_input.amount)
        return EmployeeOutput(
            message = "Employee raised Successfully", 
            employee = employee, 
            status = True
        )