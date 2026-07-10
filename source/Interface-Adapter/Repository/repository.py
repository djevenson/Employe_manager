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
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                self._to_row(employee),
            )
            connection.commit()
            connection.close()
        return employee

    def get_by_status(status:Status) -> List[Employee]:
        with self._db_connect() as connection:
            connection.execute(
                """SELECT * FROM employees WHERE status=%s """,(status.value)
            )
            employees = connection.fetchall()
        return [self._from_row(e) for  e in employees]
    
    def get_all(self) -> List[Employee]:
        connection.execute(
                """SELECT * FROM employees """
            )
            employees = connection.fetchall()
        return [self._from_row(e) for  e in employees]

    def update_employee(self, name:str, status:Status) -> Employee:
        with self._db_connect() as connection:
            connection.execute(
                """UPDATE employees SET status=%s WHERE name=%s RETURNNING *""", (status.values, name)
            ) 
            employee = connect.fetchall()
            connection.commit()
            connection.close()
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
