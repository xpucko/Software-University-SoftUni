def palindrome(text, index):
    if index == len(text) // 2:
        return f'{text} is a palindrome'
    if text[index] != text[len(text) - 1 - index]:
        return f'{text} is not a palindrome'
    return palindrome(text, index + 1)
