# Задача "Среднее арифметическое":
# Напишите программу, которая находит среднее арифметическое чисел из списка данных.

def average(nums: list) -> float:
    return sum(nums) / len(nums)

assert average([ 7, 8, 9, 8, 7, 9]) == 8


# Задача "Стандартное отклонение":
# Найдите стандартное отклонение числовых данных из списка с помощью соответствующей функции.

def standart_deviation(nums: list) -> float:
    avg = average(nums)
    return round(((sum([(i - avg)**2 for i in nums]))/(len(nums)-1))**.5, 2)

assert standart_deviation([ 7, 8, 9, 8, 7, 9]) == 0.89
