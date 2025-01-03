# Bankomat

JaneHesap = {
    'name': 'Jane Doe',
    'accountNo': '12345',
    'mainBalance': 3000,
    'additionalbalance': 2000
}

JohnHesap = {
    'name': 'John Doe',
    'accountNo': '67890',
    'mainBalance': 2000,
    'additionalbalance': 1000
}

def withdraw(account, amount):
    totalBalance = account['mainBalance'] + account['additionalbalance']
    print(f"Hello {account["name"]}")

    if account['mainBalance'] >= amount:
        print(f"Your main balance {account['mainBalance']} is eligible for withdraw {amount}")
        account['mainBalance'] -= amount
        print(f"Your new main balance is: {account['mainBalance']}")
    elif account['mainBalance'] < amount <= totalBalance:
        print(f"Your main balance {account['mainBalance']} is not eligible for withdraw {amount}")
        print(f"But your total balance {totalBalance} is eligible for withdraw {amount}")
        account['additionalbalance'] -= (amount - account['mainBalance'])
        account['mainBalance'] -= account['mainBalance']
        print(f"Your new main balance is: {account['mainBalance']}")
        print(f"Your new additional balance is: {account['additionalbalance']}")
    elif amount > totalBalance:
        print(f"Your total balance {totalBalance} is not eligible for withdraw {amount}")
    else:
        print("Unknown")


withdraw(JaneHesap,80.00)