
def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:
        # Вызываем функцию с переданным списком и сохраняем результат в словаре
        results[func.__name__] = func(int_list)

    return results  # Возвращаем словарь с результатами

if __name__ == '__main__':


    print(apply_all_func([6, 20, 15, 9], max, min))  # Вывод: {'max': 20, 'min': 6}
    print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
