str1=str(input("enter a word:"))
str2=str(input("enter second word:"))
if len(str1)!=len(str2):
    print("Not anagram")
else:
    if sorted(str1) == sorted(str2):
        print("Anagram")
    else:
        print("not anagram")
