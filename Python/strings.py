string1 = input("Enter a string: ")

print(f"String: {string1}")
print(f"String Length: {len(string1)}")
letter = str(input("Enter a letter to find: "))
print(f"Position of {letter} is at index {string1.find(letter)}")
print(f"Capitalized String: {string1.capitalize()}")
print(f"Uppercase String: {string1.upper()}")
print(f"Lowercase String: {string1.lower()}")

replace = str(input("What letter do you want to replace?"))
newLetter = str(input("Replace With: "))
string1 = string1.replace(replace, newLetter )

print(string1)

# indexing string[start : end : step]
print(string1[ : 4]) # [start : end]
print(string1[0 : : 2]) # [start : : step]
print(string1[-4 : -1]) # [start(negative) : end(negative)]
print(string1[ : :-1]) # reverse string