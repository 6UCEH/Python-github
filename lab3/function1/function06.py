def reverse_words(sentence):
    words = sentence.split(" ")  
    reversed_words = words[::-1] 
    return " ".join(reversed_words)  

# Пример использования
sentence = input("\nВведите предложение: ")
result = reverse_words(sentence)
print("\nРезультат:\n", result)
