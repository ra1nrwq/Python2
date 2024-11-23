def analyze_list(lst):
    if not all(isinstance(x, (int, float)) for x in lst):
        return "Ошибка: список должен содержать только числа."
    
    max_val = max(lst)
    min_val = min(lst)
    avg_val = sum(lst) / len(lst)
    sorted_lst = sorted(lst)
    
    n = len(lst)
    if n % 2 == 1:
        med_val = sorted_lst[n // 2]
    else:
        med_val = (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    
    return {'max': max_val, 'min': min_val, 'avg': avg_val, 'med': med_val}

def tuple_stats(tpl):
    if not all(isinstance(x, (int, float)) for x in tpl):
        return "Ошибка: кортеж должен содержать только числа."
    
    sum_val = sum(tpl)
    avg_val = sum_val / len(tpl)
    unique_tpl = tuple(set(tpl))
    
    return (sum_val, avg_val, unique_tpl)

def symmetric_difference(set1, set2):
    if not isinstance(set1, set) or not isinstance(set2, set):
        return "Ошибка: оба аргумента должны быть множествами."
    
    return set1.symmetric_difference(set2)


def main():
    # Задание 1: Анализ списка
    try:
        user_list = list(map(float, input("Введите список чисел через пробел: ").split()))
        print("Результат анализа списка:", analyze_list(user_list))
    except ValueError:
        print("Ошибка: Введите корректные числа через пробел.")
    
    # Задание 2: Работа с кортежами
    try:
        user_tuple = tuple(map(float, input("Введите кортеж чисел через пробел: ").split()))
        print("Результат работы с кортежем:", tuple_stats(user_tuple))
    except ValueError:
        print("Ошибка: Введите корректные числа через пробел.")
    
    # Задание 3: Симметрическая разность
    try:
        user_set1 = set(map(float, input("Введите первое множество чисел через пробел: ").split()))
        user_set2 = set(map(float, input("Введите второе множество чисел через пробел: ").split()))
        print("Симметрическая разность множеств:", symmetric_difference(user_set1, user_set2))
    except ValueError:
        print("Ошибка: Введите корректные числа через пробел.")
    
    print("\nРазница между структурами данных:")
    print("Словарь (dict) - неупорядоченная коллекция пар ключ-значение. Ключи должны быть уникальными.")
    print("Множество (set) - неупорядоченная коллекция уникальных элементов. Используется для операций над множествами.")
    print("Кортеж (tuple) - неизменяемая упорядоченная последовательность, часто используется для хранения фиксированных данных.")

main()