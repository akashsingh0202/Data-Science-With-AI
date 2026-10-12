# 9. Check whether a character is a vowel or consonant.
# Example: Character: a → Vowel

n=input("enter character")

# if(n=='a' or n=='A' or n=='e' or n=='E'  or n=='i' or n=='I' or n=='o' or n=='O' or n=='u' or n=='U'):
if(n in "aeiouAEIOU"):
    print("vowel")

else:
    print('constant')
    