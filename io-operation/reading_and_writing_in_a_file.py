with open("test.txt", "r") as f:
    print(f.read()) # file open in reading mode

with open("test.txt","w") as f:
    f.write("Ok I think i'm egoistic") # file writing in reading mode 