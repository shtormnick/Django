try:
    f = open("simple.txt","w")
    f.write("this i some texte")
except IOError:
    print("Error: Something wrong!")
else:
    print("Success!")
    f.close()
