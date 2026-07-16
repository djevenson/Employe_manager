import os
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from dotenv import load_dotenv
from source.Interface_Adapter.controller.controller import EmployeeController
from source.Interface_Adapter.repository.repository import PosgreSQLEmployeeRepo
from source.entities.Employee import Status
from typing import Optional


load_dotenv()


class AddEmployee(BaseModel):
    name: str
    email: str
    salary: int
    post: str


def _build_db_connection_string() -> str:
    """
    Construit la chaîne de connexion PostgreSQL à partir des variables
    d'environnement, plutôt que d'avoir des identifiants en dur dans le code.

    Variables attendues : DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
    Voir le fichier .env.example pour la liste complète.
    """
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")

    missing = [
        var_name
        for var_name, value in [
            ("DB_NAME", db_name),
            ("DB_USER", db_user),
            ("DB_PASSWORD", db_password),
        ]
        if not value
    ]
    if missing:
        raise RuntimeError(
            "Variables d'environnement manquantes pour la connexion à la base de "
            f"données : {', '.join(missing)}. "
            "Créez un fichier .env à partir de .env.example, ou définissez-les "
            "directement dans l'environnement."
        )

    return (
        f"dbname={db_name} user={db_user} password={db_password} "
        f"host={db_host} port={db_port}"
    )


def create_app(employee_repo: Optional[PosgreSQLEmployeeRepo] = None) -> FastAPI:
    app = FastAPI(
        title="Employee Manager API",
        description="API REST pour la gestion des employés, construite selon l'architecture propre.",
        version="2.3.1",
    )
    if employee_repo is None:
        connection_string = _build_db_connection_string()
        employee_repo = PosgreSQLEmployeeRepo(connection_string)

    controller = EmployeeController(employee_repo)

    @app.get("/health")
    async def health_check():
        return {"status": "great"}

    @app.post("/employees")
    async def add_employee(name:str, email:str, salary:int, post:str):
        result = controller.add_employee(name, email, salary, post)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    @app.get("/employees/{id}")
    async def get_employee(id: int):
        result = controller.get_employee(id)
        if not result["success"]:
            raise HTTPException(status_code=404, detail=result["error"])
        return result

    @app.get("/employees")
    async def list_employees(status: Status = Query(None)):
        result = controller.list_employees(status)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    
    @app.put("/employees/{id}/activate")
    async def activate_employee(id: int):
        result = controller.activate_employee(id)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    
    @app.put("/employees/{id}/onleave")
    async def on_leave_employee(id: int):
        result = controller.on_leave_employee(id)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    @app.put("/employees/{id}/layoff")
    async def lay_off_employee(id: int):
        result = controller.lay_off_employee(id)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    @app.put("/employees/{id}/retire")
    async def retire_employee(id: int):
        result = controller.retire_employee(id)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    @app.put("/employees/{id}/salary")
    async def raise_employee_salary(id: int, amount: int):
        result = controller.raise_employee(id, amount)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result
    
    @app.put("/employees/{id}/salary-cut")
    async def pay_cut_employee(id: int, amount: int):
        result = controller.pay_cut_employee(id, amount)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    @app.put("/employees/{id}/post")
    async def change_employee_post(id: int, post: str):
        result = controller.change_employee_post(id, post)
        if not result["success"]:
            raise HTTPException(status_code=400, detail=result["error"])
        return result

    return app
