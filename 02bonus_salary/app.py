from Vendor import Vendor

name = input('Digite seu nome: ')
salary = float(input("Digite o salario fixo: "))
total_sales = float(input("Digite o total de vendas em dinheiro: "))

new_vendor = Vendor(name, salary, total_sales)
print(new_vendor.total_to_receive())