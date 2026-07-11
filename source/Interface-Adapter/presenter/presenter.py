from source.entities.Employee import Employee, 
from datetime import datetime, timezone
from typing import List, Any, Dict


class EmployeePresenter:
    @staticmethod
    def to_dict(employee: Employee) -> Dict[str, Any]:
        return {
            "id": employee.id,
            "name": employee.name,
            "email": employee.email,
            "post": employee.post,
            "salary": employee.salary,
            "hire_date": employee.hire_date.isoformat(),
            "status": employee.status.value
        }
    
    @staticmethod
    def to_list(employees: List[Employee]) -> List[Dict[str, Any]]:
        return [EmployeePresenter.to_dict(employee) for employee in employees]