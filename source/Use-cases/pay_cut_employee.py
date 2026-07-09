from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeRepo
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
    employee = Optional[Employee]
    status : bool


class PayCutEmployee:
    def __init__(self, repository:EmployeRepo) -> None:
        self.repository = repository

    def execute(self, data_input:EmployeInput) -> EmployeeOutput:
        employee = self.repository.get_employee(data_input.name)
        if not employee:
            return EmployeeOutput(
                message = "Employee not found",
                employee = None, 
                status = False
            )
        if not employee.validate_pay_cut(EmployeInput.amount):
            return EmployeeOutput(
                message = f"Connot salary to small to cut {EmployeInput.amount} ", 
                employee = employee, 
                status = False
            )
        employee.cut_pay()
        employee = self.repository.update_employee(employee)
        return EmployeeOutput(
            message = "Employee cuted-pay Successfully", 
            employee = employee, 
            status = True
            )