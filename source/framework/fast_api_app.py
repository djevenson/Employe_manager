from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from source.Interface-Adapter.controller.controller import EmployeeController
from source.Interface-Adapter.repository.employee_repo import EmployeeRepo
from source.entities.Employee import Status

class AddEmployee(BaseModel):
    name: str
    email: str
    salary: int
    post: str


def create_app(employee_repo: EmployeeRepo = None) -> FastAPI:
    app = FastAPI()
    if employee_repo is None:
        employee_repo = PosgreSQLEmployeeRepo("dbname=employees user=postgres password=secret")  # Initialize with a default repository if none is provided
    
    controller = EmployeeController(employee_repo)


    @app.get("/health")
    async def health_check():
        return {"status": "great"}

    @app.post("/employees")
    async def add_employee(employee: AddEmployee):
        result = controller.add_employee(employee.dict())
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    @app.get("/employees/{name}")
    async def get_employee(name: str):
        result = controller.get_employee(name)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    @app.get("/employees")
    async def list_employees(status: Status = Query(None)):
        result = controller.list_employees(status)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    @app.put("/employees/{name}/status")
    async def update_employee_status(name: str, status: Status):
        result = controller.update_employee(name, status)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    
    @app.put("/employees/{name}/salary")
    async def raise_employee_salary(name: str, amount: int):
        result = controller.raise_employee_salary(name, amount)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    @app.put("/employees/{name}/post")
    async def change_employee_post(name: str, post: str):
        result = controller.change_employee_post(name, post)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    @app.put("/employees/{name}/activate")
    async def activate_employee(name: str):
        result = controller.activate_employee(name)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    @app.put("/employees/{name}/layoff")
    async def lay_off_employee(name: str):
        result = controller.lay_off_employee(name)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    @app.put("/employees/{name}/onleave")
    async def on_leave_employee(name: str):
        result = controller.on_leave_employee(name)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    
    @app.put("/employees/{name}/retire")
    async def retire_employee(name: str):
        result = controller.retire_employee(name)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    return app
