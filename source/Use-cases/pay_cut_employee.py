from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeeRepo
from dataclasses import dataclass
from typing import  Optional


@dataclass
class EmployeInput:
    name : str
    amount : int
    def __post_init__(self):
        self.name = self.name.strip()


@dataclass
class EmployeeOutput:
    message : str = ""
    employee : Optional[Employee]
    status : bool


class PayCutEmployee:
    def __init__(self, repository:EmployeRepo) -> None:
        self.repository = repository

    def execute(self, data_input:EmployeeInput) -> EmployeeOutput:
        employee = self.repository.get_employee(data_input.name)
        if not employee:
            return EmployeeOutput(
                message = "Employee not found",
                employee = None, 
                status = False
            )
        if not employee.is_active() or not employee.is_on_leave():
            return EmployeeOutput(
                message = f"Connot cut-pay an employee who is {employee.status}", 
                employee = employee, 
                status = False
            )
        if not employee.validate_pay_cut(data_input.amount):
            return EmployeeOutput(
                message = f"Connot salary to small to cut {data_input.amount} ", 
                employee = employee, 
                status = False
            )
        employee.cut_pay(data_input.amount)
        employee = self.repository.update_employee(employee)
        return EmployeeOutput(
            message = "Employee cuted-pay Successfully", 
            employee = employee, 
            status = True
            )