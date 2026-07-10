from source.use_cases.Interface.employe_repo import EmployeeRepo
import psycopg2
from source.entities.Employee import Employee, Status


_DT_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

class PosgreSQLEmployeeRepo(EmployeeRepo):
    def __init__(self, db_connection) -> None:
        self.db_connection = db_connection
        self._init_schema()
    
    def _init_schema(self):
        with self._db_connect as conn:
            conn.execute("""   
                CREATE TABLE IF NOT EXIST employees (
                name        VARCHAR(120),
                email       VARCHAR(120) UNIQUE,
                post        VARCHAR(120),
                salary      INT(5),
                hire_date   VARCHAR(100)
                status      VARCHAR(10)
                )
            """)

    def add_employee(self, employee:Employee) -> Employee:
        with self._db_connect() as connection:
            connection.execute(
                """
                INSERT INTO tasks (name, email, post, salary, hire_date, status)
                VALUES (%s, %s, %s, %s, %s, %s) RETURNNING *
                """,
                self._to_row(employee),
            )
            connection.commit()
            employee = connection.fetchone()
            connection.close()
        return employee

    def get_employee(self, name: str) -> Optional[Employee]:
        with self._db_connect() as connection:
            connection.execute(
                """SELECT * FROM emplpoyees WHERE name=%s """,(name,)
            )
            employee = connection.fetchone()
        return self._from_row(employee)

    def get_by_status(status:Status) -> List[Employee]:
        with self._db_connect() as connection:
            connection.execute(
                """SELECT * FROM employees WHERE status=%s """,(status.value,)
            )
            employees = connection.fetchall()
        return [self._from_row(e) for  e in employees]
    
    def get_all(self) -> List[Employee]:
        connection.execute(
                """SELECT * FROM employees """
            )
            employees = connection.fetchall()
        return [self._from_row(e) for  e in employees]

    def update_employee(self, name:str, status:Status) -> Optional[Employee]:
        with self._db_connect() as connection:
            connection.execute(
                """UPDATE employees 
                SET status=%s WHERE name=%s 
                RETURNNING *""", 
                (status.values, name)
            ) 
            employee = connect.fetchone()
            connection.commit()
            connection.close()
        return self._from_row(employee) 

    def raise_employee_salary(self, name:str, amount:int) -> Optional[Employee]:
        with self._db_connect() as connection:
            connection.execute(
                """UPDATE FROM employees 
                SET salary = salary+%s 
                WHERE name=%s RETURNNING *""",
                (name, amount) 
            )
            connection.commit()
            employee = connection.fetchone()
        return self._from_row(employee)

    def cut_employee_salary(self, name:str, amount:int) -> Optional[Employee]:
        with self._db_connect() as connection :
            connection.execute(
                """UPDATE FROM employees 
                SET salary = salary-%s 
                WHERE name=%s RETURNNING * """,
                (name, amount)
            )
            connection.commit()
            employee = connection.fetchone()
        return self._from_row(employee)

    def _db_connect(self) -> PosgreSQLConnection:
        connection = psycopg2.connect(self.db_path)
        return connection
    
    def _to_row(self, employee:Employee) -> tuple:
        return (
            employee.name,
            employee.email,
            employee.salary,
            employee.post,
            employee.hire_date.strftime(_DT_FORMAT),
            employee.status
        )

    def _from_row(row) -> Employee:
        return {
            name = row["name"],
            email = row["email"],
            post = row["status"],
            salary = row["salary"],
            hire_date = datetime.strptime(row["hire_date"], _DT_FORMAT).replace(tzinfo=timezone.utc),
            status = Status(row["status"])
        }
