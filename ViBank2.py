
# global variables
accounts = {}
ledger = {}
accountIndex = 1
# define menu functions
def mainMenu():
    menuStr = ' Please select an option:\n1. Register\n2. Login\n3. Exit\n'
    try:
        return int(input(menuStr))
    except ValueError:
        # invalid input
        return -1
def userMenu():
    userMenu = ' Please select an option:\n1. Check Balance\n2. Deposit Funds\n3. Withdraw Funds\n4. Transfer Funds\n5. Last 5 transactions\n6. Logout\n'
    try:
        int(input(userMenu))
    except ValueError:
        # invalid input
        return -1

# define user functions
def registerUser():
    # call global variables
    global accounts, ledger, accountIndex
    # get user information
    #===============================================================================================================================
    name = input('Please enter your full name: ')
    age = input('Please enter your age in years: ')
    # validate age
    while (not age.isnumeric()) or (int(age) < 18) or(int(age) > 140):
        print('Your age must be between 18 and 140')
        age = input('Please enter your age in years: ')
    nationalID = input('Please enter your national identity number: ')
    # validate ID
    while len(nationalID) != 12 or (not nationalID.isnumeric()):
        print('Your national identity number must be a number of 12 digits')
        nationalID = input('Please enter your national identity number: ')
    balance = input('Please enter your inital account balance: ')
    # validate balance
    while (not balance.isnumeric()) or (int(balance) < 500) or (int(balance) > 999999999):
        print('Your balance must be a number between 500 and 99,999,999')
        balance = input('Please enter your inital account balance: ')
    password = input('Please enter password for your account: ')
    # validate password
    while len(password) < 8:
        print('Your password must be at least 8 characters long')
        password = input('Please enter password for your account: ')
    accNo = f'BOK-0{accountIndex}'
    #========================================================================================================================================
    # save to accounts and ledger dictionaries
    accounts[accNo] = [name, int(age), nationalID, int(balance), password]
    ledger[accNo] = []
    ledger[accNo].append((' Deposit', balance, ' Opening balance'))
    print(f'Registered successfully. Your account number is {accNo}')
    # increment
    accountIndex +=1

def loginUser():
    global accounts
    # ask for Login details
    accNo = input('Please enter your account number: ')
    password = input('Please enter your password: ')
    # check if account number is in database
    if accNo not in accounts:
            print('Invalid account number')
            return (False, 0)
    else:
         if accounts[accNo][4] != password:
            print('Invalid password')
            return (False, 0)
         else:
            print('Successfully logged in!')
            return (True, accNo)
# account functions
def checkBalance(accNo):
    global accounts
    print(f'Your account balance is {accounts[accNo][3]} KES')

def depositFunds(accNo): 
    global accounts, ledger 
    amount = int(input('Please enter an amount to deposit: '))
    # validate amount
    while (not amount.isnumeric()) or (int(amount) < 500) or (int(amount) > 99999999):
        print('Your deposit amount must be between 500 and 99,999,999')
        amount = int(input('Please enter an amount to deposit: '))
        # convert to int
        amount = int(amount)
        # save deposit into accounts and ledger
        accounts[accNo][3] += amount
        ledger[accNo].append(('Deposit', amount, 'User deposit'))
        print(f'You successfully deposited {amount} KES')

def withdrawFunds(accNo):
    global accounts, ledger
    amount = int(input('Please enter an amount to withdraw: '))
    # validate amount
    while (not amount.isnumeric()) or (int(amount) < 500) or (int(amount) > 99999999):
        print('Your withrawal should be between 500 and 99,999,999')
        amount = int(input('Please enter an amount to deposit: '))
        # convert to int
        amount = int(amount)
        if amount > accounts[accNo][3]:
            print(f'Insufficient funds, your balance is {accounts[accNo][3]} KES')
        else:
            #Save to accounts and ledger
            accounts[accNo][3] -= amount
            ledger[accNo].append(('Withdrawal', amount, 'User withdrawal'))
            print(f"You successfully withrew {amount} KES")


def transferFunds(accNo):
    global accounts, ledger
    amount = int(input('Please enter amount to transfer: '))
    while (not amount.isnumeric()) or (int(amount) < 500) or (int(amount) > 99999999):
        print('Your transfer should be between 500 and 99,999,999')
        amount = int(input('Please enter an amount to transfer: '))
        # convert to int
        amount = int(amount)
        if amount > accounts[accNo][3]:
            print(f'Insufficient funds, your balance is {accounts[accNo][3]} KES')
        else:
            # ask for recipient
            rx = input('Please enter the recipient account number: ')
            if rx not in accounts:
                print('Invalid account number')
            else:
            # save to accounts and ledger
                accounts[accNo][3] -= amount
                accounts[rx][3] += amount
                ledger[accNo].append(('Transfer', amount, f'User transfer to {rx}'))
                ledger[rx].append(('Received', amount, f'from user {accNo}'))
                print(f"You have successfully transferred {amount} KES to {rx}")
            
def lastTransactions(accNo, cuttOff):
    global accounts, ledger
    #show last cut off txn
    cutOff *= -1
    for t in ledger[accNo][cuttOff:]:
        #display txn
        print(f'{t[0]} of {t[1]} SEK. {t[2]}')


def userLoop(accNo):
    global accounts, ledger
    #user while loop
    uchoice = userMenu()
    while uchoice != 6:
        if uchoice == 1:
            checkBalance(accNo)
        elif uchoice == 2:
            depositFunds(accNo)
        elif uchoice == 3:
            withdrawFunds(accNo)
        elif uchoice == 4:
            transferFunds(accNo)
        elif uchoice == 5:
            lastTransactions(accNo)
        else:
            print('Invalid option')
            #Get next selection
            uchoice = int(input(userMenu))
    print(f'Goodbye {accounts[accNo][0]}')

choice = mainMenu()
while choice != 3:
    if choice == 1:
        registerUser()
    elif choice == 2:
        result = loginUser()
        if result[0] == True:
            userLoop(result[1])
    else:
        print('Invalid option')
    choice = int(input(mainMenu))
print('Virtual Bank is now closed. Thank you. Come again!')