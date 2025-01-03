# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adi,dosya_erişme_modu)
# dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.

# "w": (Write) yazma modu.
file = open("newfile.txt", 'w')
print(file)   # name='newfile.txt' mode='w' encoding='UTF-8'>
file.write("John DOE")
file.close()

# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.

file = open("newfile.txt", 'a')
print(file)   # name='newfile.txt' mode='a' encoding='UTF-8'>
file.write("\nJane DOE")
file.close()

# "x": (Create) oluşturma. Dosya zaten varsa hata verir.
try:
    file = open("newfile.txt", 'x') # FileExistsError: [Errno 17] File exists: 'newfile.txt'
except FileExistsError as ex:
    print(ex)   # [Errno 17] File exists: 'newfile.txt'
finally:
    file.close()

# "r": (Read) okuma. varsayılan. dosya konumda yoksa hata verir.
file = open("newfile.txt", 'r')
print(file)   # name='newfile.txt' mode='r' encoding='UTF-8'>
file.close()