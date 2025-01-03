# try:
#     file = open("newfile2.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("dosya okuma hatası")
# finally:
#     print("dosya kapandı.")
#     file.close()

file = open("newfile.txt","r")
for i in file:
    print(i.strip())

file.close()

file = open("newfile.txt","r")
content = file.read()
print(content)
file.close()

file = open("newfile.txt","r")
content = file.read(5)
print(content)  # Mesut
content = file.read(1)
content = file.read(8)
print(content)  # KURTULAN
file.close()

file = open("newfile.txt","r")
content = file.readline()
print(content)  # Mesut KURTULAN

file = open("newfile.txt","r")
content = file.readlines()
print(content)  # ['Mesut KURTULAN\n', 'Mesut KURTULAN']
print(content[0])  # Mesut KURTULAN
print(content[1])  # Mesut KURTULAN