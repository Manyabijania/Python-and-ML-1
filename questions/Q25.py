f = open("file1.txt", "r")
x = f.readlines()
f1=open("new.txt","w")
f1.writelines(x)
f.close()
f1.close()


