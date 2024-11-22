class bank:
    
    def __init__(self,initial_balance=0.00):
        self.balance = initial_balance
        
    def transaction(self,trans):
        with open('transactions.txt','a') as file:
            file.write(f'{trans} \t\t\t Balance: {self.balance}\n')
            
    def deposit(self,amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
        if amount:
            self.balance = self.balance + amount
            self.transaction(f'Deposit: {amount}')
            
    def withdrawal(self,amount):
        try:
            amount = float(amount)
        except ValueError:
            amount = 0
                
        if amount:
            self.balance = self.balance - amount
            self.transaction(f'Withdrawal: {amount}')
            
account = bank()
while True:
    
    try:
        action = input('What kind of action do you want take ? ')
        
    except KeyboardInterrupt:
        print('Your are leave the ATM.')
        break
    
    if action in ['deposit','withdrawal']:
        if action == 'deposit':
            
            try:
                amount = int(input('How moch do you want to put in ? '))
                account.deposit(amount)
            except ValueError:
                print('string is not a number.')
            
        else:
            
            try:
                amount = int(input('How much do you want to take out ? '))
                account.withdrawal(amount)
            except ValueError:
                print('string is not a number.')
            
        print(f'Accout Balance is : {account.balance}')
       
    else:
        print('input not valid, try again...')