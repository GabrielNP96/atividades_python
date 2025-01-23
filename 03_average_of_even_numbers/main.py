"""
Crie uma função que receba uma lista de números inteiros como parâmetro e retorne uma nova lista contendo apenas os números pares da lista original.
1  Além disso, a função deve calcular e retornar a média dos números pares
"""

def get_user_data() -> list:
    i = True
    numbers_list = []
    while i == True:
        try:
            number = float(input("Digite um número: "))
            numbers_list.append(number)
            if len(numbers_list) <= 1:
                number = float(input("Digite pelo menos mais um número: "))
                numbers_list.append(number)
            out = input('Deseja adcionar mais numeros? S para sim e N para não: ').upper()
            if out == "N":
                print(numbers_list)
                break
        except:
            print('Digite apenas números')

get_user_data()