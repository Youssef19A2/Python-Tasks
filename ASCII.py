#Python program to get the ASCII value of a character
def get_ascii_value(char):
    return ord(char)

letter = input("Enter a character: ")
ascii_value = get_ascii_value(letter)
print(f"The ASCII value of '{letter}' is {ascii_value}.")