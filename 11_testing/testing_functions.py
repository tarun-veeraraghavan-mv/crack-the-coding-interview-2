# Function to test
def get_temp(temp: int) -> str:
    if temp > 20:
        return "hot"
    else:
        return "cold"
  
def add(a: int, b: int) -> int:
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Testing a class
class UserManager():
    def __init__(self):
        self.users = []

    def add_user(self, name, email):
        if not name or not email:
            raise ValueError("Name and email is needed")

        user = {"name": name, "email": email}

        self.users.append(user)

        return True

    def get_users(self):
        return self.users