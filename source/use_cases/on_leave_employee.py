from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeeRepo
from dataclasses import dataclass
from typing import  Optional


@dataclass
class OnLeaveEmployeeInput:
    name : str
    def __post_init__(self):
        self.name = self.name.strip()


@dataclass
class EmployeeOutput:
    message : str 
    employee : Optional[Employee]
    status : bool


class OnLeaveEmployee:
    def __init__(self, repository:EmployeeRepo) -> None:
        self.repository = repository

    def execute(self, data_input:OnLeaveEmployeeInput) -> EmployeeOutput:
        employee = self.repository.get_employee(data_input.name)
        if not employee:
            return EmployeeOutput(message = "Employee not found", employee = None, status = False)
        if not employee.is_active() or not employee.is_on_leave():
            return EmployeeOutput(
                message = f"Connot on-leave an employee who is {employee.status}", 
                employee = employee, 
                status = False
            )
        employee.on_leave()
        employee = self.repository.update_employee(data_input.name, data_input.new_post)
        return EmployeeOutput(
            message = "Employee on-leaved Successfully", 
            employee = employee, 
            status = True
            )
