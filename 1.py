def remove_duplicates(input_list):
    """Функція для видалення повторень зі списку"""
    return list(set(input_list))

user_input = input("Введіть елементи списку через пробіл: ")
user_list = user_input.split()

unique_list = remove_duplicates(user_list)

print("Список без повторень:", unique_list)
