#Write a Python program to get the command-line arguments
import sys

script_name = sys.argv[0]

num_arguments = len(sys.argv)

argument_list = sys.argv[::]


print(f"This is the name/path of the script: {script_name}")
print(f"('Number of arguments:', {num_arguments})")
print(f"('Argument List:', {argument_list})")