from source.entities.Employee import Employee
from source.use_cases.Interface.employe_repo import EmployeeRepo
from dataclasses import dataclass
from typing import  Optional


@dataclass
class LayOffEmployeeInput:
    name : str
    def __post_init__(self):
        self.name = self.name.strip()


@dataclass
class EmployeeOutput:
    employee : Optional[Employee]
    status : bool
    message : str = ""


class LayOffEmployee:
    def __init__(self, repository:EmployeeRepo) -> None:
        self.repository = repository

    def execute(self, data_input:LayOffEmployeeInput) -> EmployeeOutput:
        employee = self.repository.get_employee(data_input.name)
        if not employee:
            return EmployeeOutput(
                message = "Employee not found",
                employee = None, 
                status = False
            )
        if not employee.is_active() or not employee.is_on_leave():
            return EmployeeOutput(
                message = f"Connot lay-off an employee who is {employee.status}", 
                employee = employee, 
                status = False
            )
        employee.lay_off()
        employee = self.repository.update_employee(employee.name, data_input.new_post)
        return EmployeeOutput(
            message = "Employee layed-off Successfully", 
            employee = employee, 
            status = True
        )