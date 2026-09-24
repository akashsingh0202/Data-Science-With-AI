# write a python function to remove a given word from a list ad strip it at the same time 

def remove_word(words, target):

    new_list = []

    for word in words:
        if word.strip() != target:
            new_list.append(word)

    return new_list


words = ["python", "  hello  ", "java", "hello"]

print("this is the words what do u want to remove : ", words)

target = input("Enter word to remove: ")

words = remove_word(words, target)

print(words)