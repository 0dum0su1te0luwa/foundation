from class_practice import BankAccount

if __name__ == '__main__':
    my_account = BankAccount("Jedidiah", 10000)
    
    my_account.deposit(5000)
    my_account.withdraw(3000)

    print(my_account.get_balance())

