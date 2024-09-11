def count_case(sentence):
    upper_count = 0
    lower_count = 0

    for char in sentence:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

# 主程序
if __name__ == "__main__":
    sentence = input("Please enter a sentence: ")
    upper_count, lower_count = count_case(sentence)
    
    print(f"Number of uppercase letters: {upper_count}")
    print(f"Number of lowercase letters: {lower_count}")
