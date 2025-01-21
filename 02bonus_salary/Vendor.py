class Vendor:
    def __init__(self,name, salary, total_sales):
        self.name = name
        self.salary = salary
        self.total_sales = total_sales
        self.commission = total_sales * 0.15

    def total_to_receive(self):
            total = self.salary + self.commission
            return f'TOTAL = R$ {total:.2f}'


