from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeeRepo
from dataclasses import dataclass
from typing import  Optional


@dataclass
class PayCutEmployeeInput:
    id:int
    amount : int
    


@dataclass
class EmployeeOutput:
    message : str
    employee : Optional[Employee]
    status : bool


class PayCutEmployee:
    def __init__(self, repository:EmployeeRepo) -> None:
        self.repository = repository

    def execute(self, data_input:PayCutEmployeeInput) -> EmployeeOutput:
        employee = self.repository.get_employee(data_input.id)
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
        employee = self.repository.cut_employee_salary(employee.name, data_input.amount)
        return EmployeeOutput(
            message = "Employee cuted-pay Successfully", 
            employee = employee, 
            status = True
            )