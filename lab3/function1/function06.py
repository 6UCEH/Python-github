def reverse_words(sentence):
    words = sentence.split(" ")  
    reversed_words = words[::-1] 
    return " ".join(reversed_words)  

# Пример использования
sentence = input("Введите предложение: ")
result = reverse_words(sentence)
print("Результат:", result)
