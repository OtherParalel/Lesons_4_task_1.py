def is_palindrome(word):
    # Converting a word to lower case
    word = word.lower()
    # Reversing the word and comparing it with the original
    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindrome("випив"))
print(is_palindrome("мова"))

# Writing code in one line

print("Введіть слово: "); print(str(input().lower() == input().lower()[::-1]))

