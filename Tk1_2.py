#Write a Python program to test whether a passed letter is a vowel or not.
vowel_letter = ('a','o','e','i','u','A','O','U','I','E')
Your_letter= input("Enter The Letter: ")
if Your_letter in vowel_letter:
    print("True")
else:
    print("False")