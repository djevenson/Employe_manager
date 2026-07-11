from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeeRepo
from dataclasses import dataclass
from typing import  Optional


@dataclass
class ChangeEmployeePostInput:
    name : str
    new_post : str
    def __post_init__(self):
        self.name = self.name.strip()
        self.new_post = self.new_post.strip()


@dataclass
class EmployeeOutput:
    message : str 
    employee : Optional[Employee]
    status : bool


class ChangeEmployeePost:
    def __init__(self, repository:EmployeeRepo) -> None:
        self.repository = repository

    def execute(self, data_input:ChangeEmployeePostInput) -> EmployeeOutput:
        employee = self.repository.get_employee(data_input.name)
        if not employee:
            return EmployeeOutput(
                message = "Employee not found",
                employee = None, 
                status =False
            )
        if not employee.is_active() or not employee.is_on_leave():
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
        employee = self.repository.update_employee(employee)
        return EmployeeOutput(
            message = "Post changed Successfully", 
            employee = employee, 
            status = True
        )