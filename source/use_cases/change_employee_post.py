from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeeRepo
from dataclasses import dataclass
from typing import  Optional


@dataclass
class ChangeEmployeePostInput:
    id : str
    new_post : str
    

@dataclass
class EmployeeOutput:
    message : str 
    employee : Optional[Employee]
    status : bool


class ChangeEmployeePost:
    def __init__(self, repository:EmployeeRepo) -> None:
        self.repository = repository

    def execute(self, data_input:ChangeEmployeePostInput) -> EmployeeOutput:
        employee = self.repository.get_employee(data_input.id)
        if employee is None:
            return EmployeeOutput(
                message = "Employee not found",
                employee = None, 
                status =False
            )
        if employee.is_laid_off() or employee.is_retired():
            return EmployeeOutput(
                message = f"Connot change post of an employee who is {employee.status}", 
                employee = employee, 
                status = False
            )
        if not data_input.new_post:
            return EmployeeOutput(
                message = "new post connot be empty",
                employee = None, 
                status =False
            )
        employee.change_post(data_input.new_post)
        employee = self.repository.change_employee_post(data_input.id, employee.post)
        return EmployeeOutput(
            message = "Post changed Successfully", 
            employee = employee, 
            status = True
        )