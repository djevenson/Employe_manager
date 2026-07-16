from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeeRepo
from dataclasses import dataclass
from typing import  Optional


@dataclass
class OnLeaveEmployeeInput:
    id:int
    
    

@dataclass
class EmployeeOutput:
    message : str 
    employee : Optional[Employee]
    status : bool


class OnLeaveEmployee:
    def __init__(self, repository:EmployeeRepo) -> None:
        self.repository = repository

    def execute(self, data_input:OnLeaveEmployeeInput) -> EmployeeOutput:
        employee = self.repository.get_employee(data_input.id)
        if employee is None:
            return EmployeeOutput(message = "Employee not found", employee = None, status = False)
        if not employee.is_active():
            return EmployeeOutput(
                message = f"Cannot on-leave an employee who is {employee.status}", 
                employee = employee, 
                status = False
            )
        employee.on_leave()
        employee = self.repository.update_employee(data_input.id, employee.status)
        return EmployeeOutput(
            message = "Employee on-leaved Successfully", 
            employee = employee, 
            status = True
            )
