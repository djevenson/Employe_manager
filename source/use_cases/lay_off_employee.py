from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeeRepo
from dataclasses import dataclass
from typing import  Optional


@dataclass
class LayOffEmployeeInput:
    id:int

@dataclass
class EmployeeOutput:
    employee : Optional[Employee]
    status : bool
    message : str = ""


class LayOffEmployee:
    def __init__(self, repository:EmployeeRepo) -> None:
        self.repository = repository

    def execute(self, data_input:LayOffEmployeeInput) -> EmployeeOutput:
        employee = self.repository.get_employee(data_input.id)
        if not employee:
            return EmployeeOutput(
                message = "Employee not found",
                employee = None, 
                status = False
            )
        if employee.is_laid_off() or employee.is_retired():
            return EmployeeOutput(
                message = f"Connot lay-off an employee who is {employee.status.value}", 
                employee = employee, 
                status = False
            )
        employee.lay_off()
        employee = self.repository.update_employee(data_input.id, employee.status)
        return EmployeeOutput(
            message = "Employee layed-off Successfully", 
            employee = employee, 
            status = True
        )