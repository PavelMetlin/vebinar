x = input('Введите число ')

def sum(x):                           
    if float(x) < 0:                         
        x = float(x) * (-1)
    number = 0

    for i in str(x):
        if i != '.':
            number += int(i)
    return number

   
print(f'Сумма цифр равна {sum(x)}')