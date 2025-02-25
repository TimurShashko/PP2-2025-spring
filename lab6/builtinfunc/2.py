def count_upper_lower(s):
    upper_count = 0
    lower_count = 0
    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count

if __name__ == "__main__":
    test_string = input("Введите строку: ")
    upper_c, lower_c = count_upper_lower(test_string)
    print(f"Upper case letters: {upper_c}")
    print(f"Lower case letters: {lower_c}")
