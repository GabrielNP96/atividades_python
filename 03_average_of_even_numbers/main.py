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
                return numbers_list
        except:
            print('Digite apenas números')

def only_even_numbers(list) -> list:
    even_list = []
    for number in list:
        if number % 2 == 0:
            even_list.append((number))

    print(even_list)
    return even_list

def sum_list(list) -> str:
    return f'A soma dos números pares é = {sum(list)}'

print(sum_list(only_even_numbers(get_user_data())))
