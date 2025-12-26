"""
Call Center: Imagine you have a call center with three levels of employees: respondent, manager,
and director. An incoming telephone call must be first allocated to a respondent who is free. If the
respondent can't handle the call, he or she must escalate the call to a manager. If the manager is not
free or not able to handle it, then the call should be escalated to a director. Design the classes and
data structures for this problem. Implement a method dispatchCall ( } which assigns a call to
the first available employee.
"""

from enum import IntEnum

# Enum to denote the different employee levels
class EmployeeLevel(IntEnum):
    RESPONDANT = 0
    MANAGER = 1
    DIRECTOR = 2

# The base employee class
class Employee():
    # Has the name, level and is_free values
    def __init__(self, name: str, level: EmployeeLevel, is_free: bool):
        self.name: str = name
        self.level: EmployeeLevel = level
        self.is_free: bool = is_free

    # returns if the employee is free or not
    def check_free(self):
        return self.is_free
    
    # handle call action
    def handleCall(self):
        self.is_free = False
        print(f"CALL HANDLED BY {self.level} : {self.name.upper()}")

# The three types of employees in the company
class Respondent(Employee):
    def __init__(self, name, level, is_free):
        super().__init__(name, level, is_free)

class Manager(Employee):
    def __init__(self, name, level, is_free):
        super().__init__(name, level, is_free)

class Director(Employee):
    def __init__(self, name, level, is_free):
        super().__init__(name, level, is_free)


