from datetime import datetime
from application import salary
from application.db import people


print(datetime.now())
salary.calculate_salary()
people.get_employees()
