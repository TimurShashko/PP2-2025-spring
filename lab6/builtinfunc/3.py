def is_palindrome(s):
    cleaned = "".join(s.split()).lower()
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    test_string = input("Введите строку: ")
    print("Является палиндромом?" , is_palindrome(test_string))
