from enum import Enum
from collections import deque,defaultdict




emp_dict:defaultdict = {}


emp_dict[1] = {"type":"Engineer", "name" : "ram"}
emp_dict[2] = {"type":"Manager", "name" : "shyam"}
emp_dict[3] = {"type":"Engineer", "name" : "krishna"}


# Enum to represent employee status
class Status(Enum):
    FREE = 0
    BUSY = 1


# Base Employee class
class Employee:
    def __init__(self, name):
        self.name = name
        self.status = Status.FREE

    def is_free(self):
        return self.status == Status.FREE

    def handle_incident(self):
        print(f"{self.__class__.__name__} {self.name} is handling the incident.")
        self.status = Status.BUSY

    def resolve_incident(self):
        self.status = Status.FREE
        print(f"{self.__class__.__name__} {self.name} is now free.")


# Engineer and Manager classes inherit from Employee
class Engineer(Employee):
    pass


class Manager(Employee):
    pass


# Interview Task
class PagerDuty:
    def __init__(self):
        self.engineer_pool = deque()
        self.manager_pool = deque()

    def add_person(self,id):
        if(id in emp_dict):
            name = emp_dict[id]["name"]
            type = emp_dict[id]["type"]

            print(f"{name} {type}")
            if(type == "Engineer"):
                print(f"adding {name} to engineer pool ")
                self.engineer_pool.append(Engineer(name))
            else:
                self.manager_pool.append(Manager(name))
                
        else:
            print("non  employee")
            

    def dispatch_alert(self):
        #raise NotImplementedError()
        poc:Employee = None
        if(len(self.engineer_pool)) > 0:
            poc = self.engineer_pool.popleft()
            poc.handle_incident()
        elif(len(self.manager_pool)) > 0:
            poc = self.manager_pool.popleft()
            poc.handle_incident()
        else:
            print(f" no body available for the call")
            raise KeyError


    