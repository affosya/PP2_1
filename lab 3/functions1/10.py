def is_palindrome(s):
    s = s.replace(" ", "").lower()  # Убираем пробелы и приводим к нижнему регистру
    return s == s[::-1]  # Сравниваем строку с её перевёрнутой версией

# Пример использования:
print(is_palindrome("madam"))  # Вывод: True
print(is_palindrome("A man a plan a canal Panama"))  # Вывод: True
print(is_palindrome("hello"))  # Вывод: False
