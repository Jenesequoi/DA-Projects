
mainMenu = ' Please select an option:\n1. Register\n2. Login\n3. Exit\n'
userMenu = ' Please select an option:\n1. Check Balance\n2. Deposit Funds\n3. Withdraw Funds\n4. Transfer Funds\n5. Last 5 transactions\n6. Logout\n'
accounts = {}
ledger = {}
accountIndex = 1

choice = int(input(mainMenu))
#mainMenu while loop
while choice != 3:
    #Process menu choice
    if choice == 1:
        #Register user information
        name = input('Please enter your full name: ')
        age = input('Please enter your age in years: ')
        nationalID = input('Please enter your national identity number: ')
        balance = input('Please enter your inital account balance: ')
        password = input('Please enter password for your account: ')
        accNo = f'BOK-0{accountIndex}'
        #Save information to accounts and ledger
        accounts[accNo] = [name, int(age), nationalID, int(balance), password]
        ledger[accNo] = []
        ledger[accNo].append((' Deposit', balance, ' Opening balance'))
        print(f'Registered successfully. Your account number is {accNo}')
        #increment
        accountIndex +=1
    elif choice == 2:
        #Ask for Login details
        accNo = input('Please enter your account number: ')
        password = input('Please enter your password: ')
        #Check if account number is in database
        if accNo not in accounts:
            print('Invalid account number')
        else:
            if accounts[accNo][4] != password:
                print('Invalid password')
            else:
                print('Successfully logged in!')
                #userMenu while loop
                uchoice = int(input(userMenu))
                while uchoice != 6:
                    #process user menu choice
                    if uchoice == 1:
                        #Check balance
                        print(f'Your account balance is {accounts[accNo][3]} KES')
                    elif uchoice == 2:
                        #Make a deposit
                        amount = int(input('Please enter an amount to deposit: '))
                        #save deposit into accounts and ledger
                        accounts[accNo][3] += amount
                        ledger[accNo].append(('Deposit', amount, 'User deposit'))
                        print(f'You successfully deposited {amount} KES')
                    elif uchoice == 3:
                        #Make a withdrawal
                        amount = int(input('Please enter an amount to withdraw: '))
                        if amount > accounts[accNo][3]:
                            print(f'Insufficient funds, your balance is {accounts[accNo][3]} KES')
                        else:
                            #Save to accounts and ledger
                            accounts[accNo][3] -= amount
                            ledger[accNo].append(('Withdrawal', amount, 'User withdrawal'))
                            print(f"You successfully withrew {amount} KES")
                    elif uchoice == 4:
                        #Making a transfer
                        amount = int(input('Please enter amount to transfer: '))
                        if amount > accounts[accNo][3]:
                            print(f'Insufficient funds, your balance is {accounts[accNo][3]} KES')
                        else:
                            #Ask for recipient
                            rx = input('Please enter the recipient account number: ')
                            if rx not in accounts:
                                print('Invalid account number')
                            else:
                                #Save to accounts and ledger
                                accounts[accNo][3] -= amount
                                accounts[rx][3] += amount
                                ledger[accNo].append(('Transfer', amount, f'User transfer to {rx}'))
                                ledger[rx].append(('Received', amount, f'from user {accNo}'))
                                print(f"You have successfully transferred {amount} KES to {rx}")
                    elif uchoice == 5:
                        #Show last 5 transactions
                        for t in ledger[accNo][-5]:
                            print(f'{t[0]} of {t[1]} SEK. {t[2]}')
                    else:
                        print('Invalid option')
                    #Get next selection
                    uchoice = int(input(userMenu))
                print(f'Goodbye {accounts[accNo][0]}')
    else:
        print('Invalid option')
    choice = int(input(mainMenu))
print('Virtual Bank is now closed. Thank you. Come again!')