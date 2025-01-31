def is_palindrome(text):
    text = text.replace(" ", "").lower()  # Убираем пробелы и приводим к нижнему регистру
    return text == text[::-1]  # Сравниваем текст с его обратной версией


word_or_phrase = input("Введите слово или фразу: ")
if is_palindrome(word_or_phrase):
    print("Это палиндром")
else:
    print("Это не палиндром")
