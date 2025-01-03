'''
    students = {
        '120': {
            'name': 'Ali',
            'lastname': 'Yılmaz',
            'phone': '532 000 00 01'
        },
        '125': {
            'name': 'Can',
            'lastname': 'Korkmaz',
            'phone': '532 000 00 02'
        },
        '128': {
            'name': 'Volkan',
            'lastname': 'Yükselen',
            'phone': '532 000 00 03'
        },
    }

    1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
       dictionary içinde saklayınız.

    2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.
'''

'''
students = {}

number = input('Student Number: ')
name = input('Student Name: ')
lastname = input('Student Lastname: ')
phone = input('Student Phone: ')

students[number] = {
    'name': name,
    'lastname': lastname,
    'phone': phone
}

print(students)
'''

students = {
        '120': {
            'name': 'Ali',
            'lastname': 'Yılmaz',
            'phone': '532 000 00 01'
        },
        '125': {
            'name': 'Can',
            'lastname': 'Korkmaz',
            'phone': '532 000 00 02'
        },
    }

students.update({
    '125': {
        'name': 'Can',
        'lastname': 'Korkmaz',
        'phone': '532 000 00 02'
    },
})

students['128'] = {
    'name': 'Volkan',
    'lastname': 'Yükselen',
    'phone': '532 000 00 03'
}

print(students)
print(students["125"])  # {'name': 'Can', 'lastname': 'Korkmaz', 'phone': '532 000 00 02'}
print(students["125"]["name"])  # Can