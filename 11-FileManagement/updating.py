with open("newfile.txt","r+") as file:
    content = file.read()
    print(content)

with open("newfile.txt","a") as file:
    file.write("\nCourtney H. Roberts")