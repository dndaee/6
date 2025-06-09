def process_set(A, x):
    """
    Функція обробляє множину A:
    - додає x, якщо його немає
    - видаляє x, якщо він є
    """
    if not isinstance(A, set):
        print("A не є множиною. Перетворюємо на список.")
        A = set(list(A)) 

    if x in A:
        A.remove(x)
    else:
        A.add(x)

    return A

user_input = input("Введіть символи множини A без пробілів (наприклад: abcde): ")
A = set(user_input)

x = input("Введіть символ x: ")

B = process_set(A, x)

print("Множина B:", B)
