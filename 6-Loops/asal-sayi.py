'''
Soru: Girilen bir sayının asal olup olmadığını bulun.
** Asal Sayı 1 ve kendisi hariç tam böleni olmayan
   sayılara denir.
'''

number = int(input("Enter a number: "))
isPrime = True
if number <= 2:
    isPrime = False

for i in range(2, number):
    if number % i == 0:
        isPrime = False
        break
if isPrime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")