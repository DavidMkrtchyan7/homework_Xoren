def palindrome(text: str):
    l = len(text)
    for i in range(l//2):
        if text[i] != text[l-i-1]:
            return False
    return True
while True:
    text = input("Enter the text:")
    if text == '':
        print("Hello")
        break
    print("The text", text, "is a palindrome" if palindrome(text) else "is not a palindrome")