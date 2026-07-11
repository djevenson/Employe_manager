from source.use_cases.Interface.employe_repo import EmployeeRepo
from source.entities.Employee import Status
from typing import List, Optional, Dict, Any
from source.interface_adapter.presenter.employee_presenter import EmployeePresenter

from source.use_cases.active_employee import ActivateEmployee, ActivateEmployeeInput
from source.use_cases.add_employee import AddEmployee, AddEmployeeInput
from source.use_cases.change_employee_post import ChangeEmployeePost, ChangeEmployeePostInput
from source.use_cases.get_employee import GetEmployee, GetEmployeeInput
from source.use_cases.lay_off_employee import LayOffEmployee, LayOffEmployeeInput
from source.use_cases.list_employee import ListEmployees, ListEmployeesInput
from source.use_cases.on_leave_employee import OnLeaveEmployee, OnLeaveEmployeeInput
from source.use_cases.pay_cut_employee import PayCutEmployee, PayCutEmployeeInput
from source.use_cases.raise_employee import RaiseEmployee, RaiseEmployeeInput
from source.use_cases.retire_employee import RetireEmployee, RetireEmployeeInput



class EmployeeController:

    def __init__(self, employee_repo: EmployeeRepo):
        self.add_employee = AddEmployee(employee_repo)
        self.get_employee = GetEmployee(employee_repo)
        self.change_employee_post = ChangeEmployeePost(employee_repo)
        self.list_employees = ListEmployees(employee_repo)
        self.activate_employee = ActivateEmployee(employee_repo)
        self.lay_off_employee = LayOffEmployee(employee_repo)
        self.on_leave_employee = OnLeaveEmployee(employee_repo)
        self.pay_cut_employee = PayCutEmployee(employee_repo)
        self.raise_employee = RaiseEmployee(employee_repo)
        self.retire_employee = RetireEmployee(employee_repo)

    def add_employee(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        name = input_data.get("name").strip()
        email = input_data.get("email").strip() 
        if not name or not email:
            return {"success": False, "error": "Name and email are required fields."}
        output_data = self.add_employee.execute(AddEmployeeInput(name=name, email=email, salary=input_data.get("salary"), post=input_data.get("post")))
        return {
            "success": True, 
            "employee": EmployeePresenter.to_dict(output_data.employee)
        }

    def get_employee(self, name:str) -> Dict[str, Any]:
        if not name.strip():
            return {"success": False, "error": "Name is a required field."}
        output_data = self.get_employee.execute(GetEmployeeInput(name=name))
        return {
            "success": True, 
            "employee": EmployeePresenter.to_dict(output_data.employee)
        }

    def list_employees(self, status: Optional[Status] = None) -> Dict[str, Any]:
        if status:
            try:
                status = Status(status)
            except ValueError:
                valid_statuses = [status.value for status in Status]
                return {"success": False, "error": f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}"}
        output_data = self.list_employees.execute(ListEmployeesInput(status=status))
        return {
            "success": True, 
            "employees": [EmployeePresenter.to_list(output_data.employees) ],
            "total": output_data.total
        }

    def activate_employee(self, name: str) -> Dict[str, Any]:
        if not name.strip():
            return {"success": False, "error": "Name is a required field."}
        output_data = self.activate_employee.execute(ActivateEmployeeInput(name=name))
        return {
            "success": True, 
            "employee": EmployeePresenter.to_dict(output_data.employee)
        }
        

    def lay_off_employee(self, name: str) -> Dict[str, Any]:
        if not name.strip():
            return {"success": False, "error": "Name is a required field."}
        output_data = self.lay_off_employee.execute(LayOffEmployeeInput(name=name))
        return {
            "success": True, 
            "employee": EmployeePresenter.to_dict(output_data.employee)
        }

    def on_leave_employee(self, name: str) -> Dict[str, Any]:
        if not name.strip():
            return {"success": False, "error": "Name is a required field."}
        output_data = self.on_leave_employee.execute(OnLeaveEmployeeInput(name=name))
        return {
            "success": True, 
            "employee": EmployeePresenter.to_dict(output_data.employee)
        }

    def pay_cut_employee(self, name: str) -> Dict[str, Any]:
        if not name.strip():
            return {"success": False, "error": "Name is a required field."}
        output_data = self.pay_cut_employee.execute(PayCutEmployeeInput(name=name))
        return {
            "success": True, 
            "employee": EmployeePresenter.to_dict(output_data.employee)
        }

    def raise_employee(self, name: str) -> Dict[str, Any]:
        if not name.strip():
            return {"success": False, "error": "Name is a required field."}
        output_data = self.raise_employee.execute(RaiseEmployeeInput(name=name))
        return {
            "success": True, 
            "employee": EmployeePresenter.to_dict(output_data.employee)
        }

    def retire_employee(self, name: str) -> Dict[str, Any]:
        if not name.strip():
            return {"success": False, "error": "Name is a required field."}
        output_data = self.retire_employee.execute(RetireEmployeeInput(name=name))
        return {
            "success": True, 
            "employee": EmployeePresenter.to_dict(output_data.employee)
        }

    def change_employee_post(self, name: str, new_post: str) -> Dict[str, Any]:
        if not name.strip():
            return {"success": False, "error": "Name is a required field."}
        if not new_post.strip():
            return {"success": False, "error": "New post is a required field."}
        output_data = self.change_employee_post.execute(ChangeEmployeePostInput(name=name, new_post=new_post))
        return {
            "success": True, 
            "employee": EmployeePresenter.to_dict(output_data.employee)
        }