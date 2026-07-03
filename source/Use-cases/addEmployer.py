from source.entities.employer import Employer
from source.use_cases.Interface.EmployeRepo import EmployeRepo

EmployerRepository = EmployeRepo()


class AddEmployerInput:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address



class AddEmployerOutput:
    def __init__(self, employer: Employer):
        self.employer = employer



class AddEmployer:
    def __init__(self, input_data: AddEmployerInput):
        self.input_data = input_data

    def execute(self) -> AddEmployerOutput:
        employer = Employer(name=self.input_data.name, address=self.input_data.address)
        EmployerRepository.add_employer(employer)
        return AddEmployerOutput(employer)