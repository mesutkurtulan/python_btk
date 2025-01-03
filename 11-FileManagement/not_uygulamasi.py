
def not_hesapla(line):
    line = line[:-1]
    liste = line.split(':')
    notlar = liste[1].split(',')
    not_ortalaması = (int(notlar[0])+int(notlar[1])+int(notlar[2]))/3
    return liste[0] + ': ' + str(not_ortalaması)

def ortalamaları_oku():
    with open("exam_results.txt","r") as file:
        for line in file:
            print(not_hesapla(line))

def not_gir():
    name = input("Student Name: ")
    lastname = input("Student LastName: ")
    point1 = input("Point 1: ")
    point2 = input("Point 2: ")
    point3 = input("Point 3: ")

    with open("exam_results.txt","a") as file:
        file.write(name + ' ' + lastname + ':' + point1 + ',' + point2 + ',' + point3 + '\n')

def notlari_kayıt_et():
    with open("exam_results.txt","r") as file:
        liste = []
        for line in file:
            liste.append(not_hesapla(line))

    with open("exam_results_with_averages.txt","w") as file2:
        for i in liste:
            file2.write(i + '\n')


while True:
    islem = input("1- Notları oku\n2- Not Gir\n3- Notları Kayıt Et\n4- Çıkış\n")

    if islem == "1":
        ortalamaları_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
       notlari_kayıt_et()
    else:
        break