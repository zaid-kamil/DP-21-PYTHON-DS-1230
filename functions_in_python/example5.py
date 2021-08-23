# 1. waf to remove all the special characters from a string
# 2. waf to count all the words in a string
# 3. waf to count the special characters in a string


# 1.
from string import punctuation

def remove_special_characters():
    sentence = input("enter something:")
    for i in punctuation:
        sentence = sentence.replace(i, "")
    return sentence

# 2.
def count_words():
    sentence = input("enter something:")
    words = sentence.split()
    return len(words)

if __name__ == "__main__":
    print(remove_special_characters())
