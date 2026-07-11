from source.use_cases.Interface.employe_repo import EmployeeRepo
import psycopg2
from source.entities.Employee import Employee, Status
from datetime import datetime, timezone
from typing import List, Optional

_DT_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

class PosgreSQLEmployeeRepo(EmployeeRepo):
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self._init_schema()
    
    def _init_schema(self):
        with self._db_connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""   
                    CREATE TABLE IF NOT EXISTS employees (
                    id          SERIAL PRIMARY KEY,
                    name        VARCHAR(120) UNIQUE,
                    email       VARCHAR(120) UNIQUE,
                    post        VARCHAR(120),
                    salary      INTEGER,
                    hire_date   VARCHAR(100),
                    status      VARCHAR(10)
                    )
                """)

    def add_employee(self, employee:Employee) -> Optional[Employee]:
        with self._db_connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO employees (name, email, post, salary, hire_date, status)
                    VALUES (%s, %s, %s, %s, %s, %s) RETURNING *
                    """,
                    self._to_row(employee),
                )
                employee = cursor.fetchone()
                connection.commit()
        return self._from_row(employee) if employee else None

    def get_employee(self, name: str) -> Optional[Employee]:
        with self._db_connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT * FROM employees WHERE name=%s """,(name,)
                )
                employee = cursor.fetchone()
        return self._from_row(employee) if employee else None

    def get_by_status(self, status:Status) -> List[Employee]:
        with self._db_connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT * FROM employees WHERE status=%s """,(status.value,)
                )
                employees = cursor.fetchall()
        return [self._from_row(e) for  e in employees] if employees else []
    
    def get_all(self) -> List[Employee]:
        with self._db_connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """SELECT * FROM employees """
                )
                employees = cursor.fetchall()
        return [self._from_row(e) for  e in employees] if employees else []

    def update_employee(self, name:str, status:Status) -> Optional[Employee]:
        with self._db_connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE employees 
                    SET status=%s WHERE name=%s 
                    RETURNING *""", 
                    (status.value, name)
                ) 
                employee = cursor.fetchone()
                connection.commit()
        return self._from_row(employee) if employee else None

    def raise_employee_salary(self, name:str, amount:int) -> Optional[Employee]:
        with self._db_connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE employees 
                    SET salary = salary+%s 
                    WHERE name=%s RETURNING *""",
                (amount, name) 
            )
            employee = cursor.fetchone()
            connection.commit()    
        return self._from_row(employee) if employee else None

    def cut_employee_salary(self, name:str, amount:int) -> Optional[Employee]:
        with self._db_connect() as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE employees 
                    SET salary = salary-%s 
                    WHERE name=%s RETURNING * """,
                    (amount, name)
                )
                employee = cursor.fetchone()
                connection.commit()
        return self._from_row(employee) if employee else None

    def _db_connect(self) -> connection:
        connection = psycopg2.connect(self.db_path)
        return connection
    
    def _to_row(self, employee:Employee) -> tuple:
        return (
            employee.name,
            employee.email,
            employee.post,
            employee.salary,
            employee.hire_date.strftime(_DT_FORMAT),
            employee.status.value
        )

    def _from_row(self, row:tuple) -> Employee:
        return Employee(
            id=row[0],
            name=row[1],
            email=row[2],
            post=row[3],
            salary=row[4],
            hire_date=datetime.strptime(row[5], _DT_FORMAT).replace(tzinfo=timezone.utc),
            status=Status(row[6])
        )
