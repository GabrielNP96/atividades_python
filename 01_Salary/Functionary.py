class Functionary:
    def __init__(self,id, hours_value, hours_worked):
        self.id = id
        self.hours_value = hours_value
        self.hours_worked = hours_worked
        self.salary = hours_value * hours_worked

    def __str__(self):
        return f'Number = {self.id}\nSalary = U$ {self.salary:.2f}'

