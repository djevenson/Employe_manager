class EmployeRepo:
    def __init__(self):
        self.employers = []

    def add_employer(self, employer: Employer):
        self.employers.append(employer)

    def get_employers(self):
        return self.employers