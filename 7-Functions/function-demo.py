# 1- Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

def printWord_1(word, each):
    i = 0
    while i < each:
        print(word)
        i += 1

printWord_1("Hello", 5) # Hello, Hello, Hello, Hello, Hello

def printWord_2(word, each):
    print(word * each)

printWord_2("Hello\n", 5) # Hello, Hello, Hello, Hello, Hello

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazınız.

def changeToList(*args):
    list =[]
    for i in args:
        list.append(i)
    return  list

result = changeToList(1,2,3,4,5,6,7,8,9)
print(result)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun.
def findPrimeNumber(number1, number2):
    primeNumbers = []
    for number in range(number1, number2):
        if number > 1:
            is_prime = True
            for i in range(2, int(number*0.5) + 1):
                if (number % i) == 0:
                    is_prime = False
                    break
            if is_prime:
                primeNumbers.append(number)
    return primeNumbers

print(findPrimeNumber(10, 20))  # [11, 13, 17, 19]


# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.

def perfectDivisors(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return divisors

print(perfectDivisors(10)) # [1, 2, 5]
print(perfectDivisors(40)) # [1, 2, 4, 5, 8, 10, 20]