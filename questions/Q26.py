s = str(input("enter a word:"))
str1 = str(input("enter prefix:"))
str2 = str(input("enter suffix:"))


def prefixx(s, str1):
    if s.startswith(str1):
        print("it has the given prefix")
    else:
        print("it does not start with the given prefix")


def suffixx(s, str2):
    if s.endswith(str2):
        print("it has the given suffix")
    else:
        print("it does not end with the given suffix")


prefixx(s, str1)
suffixx(s, str2)
