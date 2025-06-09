def find_five_min_elements(lst):
    """Функція знаходить перші п’ять мінімальних елементів списку"""
    sorted_list = sorted(lst)
    return sorted_list[:5]  

user_input = input("Введіть ціле число через пробіл: ")
user_list = list(map(int, user_input.split()))

min_elements = find_five_min_elements(user_list)

print("Перші п’ять мінімальних елементів:", min_elements)
