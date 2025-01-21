from Functionary import Functionary

id = int(input("Digite o id: "))
hours_value = float(input("Valor da hora: "))
hours_worked = float(input("Horas trabalhadas: "))

new_functionary = Functionary(id,hours_value,hours_worked)
print(new_functionary)