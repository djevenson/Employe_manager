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
        if employee is None:
            return EmployeeOutput(
                message = "Employee not found",
                employee = None, 
                status = False
            )
        
        if not employee.validate_pay_cut(data_input.amount):
            return EmployeeOutput(
                message = f"Cannot cut salary by {data_input.amount}, minimum salary must remain 100", 
                employee = employee, 
                status = False
            )
        
        if employee.is_laid_off() or employee.is_retired():
            return EmployeeOutput(
                message = f"Cannot cut-pay an employee who is {employee.status.value}", 
                employee = employee, 
                status = False
            )

        employee.cut_pay(data_input.amount)
        employee = self.repository.cut_employee_salary(data_input.id, data_input.amount)
        return EmployeeOutput(
            message = "Employee salary reduced Successfully", 
            employee = employee, 
            status = True
            )