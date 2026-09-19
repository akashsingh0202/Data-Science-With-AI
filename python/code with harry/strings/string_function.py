a="abhishek"
print(len(a))
print(a.capitalize)
print(a.endswith("ek"))
print(a.startswith('ab'))
print(a.upper())
print(a.lower())
print(a.title())
text = "  hello  "
text.lstrip()   # left spaces
text.rstrip()   # right spaces
print(text.strip())

text = "I like Java"
print(text.replace("Java", "Python"))

text = "Python SQL Java"

print(text.split())

words = ["Python", "SQL", "Java"]

print(" - ".join(words))

text = "Hello Python"

print(text.find("Python"))

text = "banana"

print(text.count("a"))

print("12345".isdigit())


print("Python".isalpha())


print("Python123".isalnum())

print("   ".isspace())