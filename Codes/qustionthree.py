def process_texts(text1, text2):
    combined = text1 + text2
    char_list = list(combined)
    return char_list


text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")
result = process_texts(text1, text2)
print("\nCharacters in the combined text:")
print(result)
print("\nThank you for using my application\nAfter processing the input.")