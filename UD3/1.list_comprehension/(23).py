import datetime

def days_in_month(month):
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days_per_month[month - 1]

def sum_of_digits(n):
    return sum(int(d) for d in str(n))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Obtener el mes actual
now = datetime.datetime.now()
current_month = now.month

# Obtener el número de días en el mes actual
num_days = days_in_month(current_month)

# Generar el diccionario comprimido para el mes actual
days_dict = {day: is_prime(sum_of_digits(day)) for day in range(1, num_days + 1)}

print(days_dict)
