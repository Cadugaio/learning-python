import getpass
import os

accounts_list = {
        '0001-01': {
            'password': '123456',
            'name': 'Fulano da Silva',
            'value': 100,
            'adm': False
        },
        '0002-01': {
            'password': '123456',
            'name': 'Ciclano da Silva',
            'value': 50,
            'adm': False
        },
        '0003-01': {
            'password': '123456',
            'name': 'Adm',
            'value': 1000,
            'adm': True
        }
    }
money_slips = {
        '20': 5,
        '50': 5,
        '100': 5,
    }

while True:
    print('------------------------------------')
    print('----------- ATM - Carlos -----------')
    print('------------------------------------')
    account_typed = input('Account number: ')
    password_typed = getpass.getpass('Password: ')
    # print(account_typed)
    # print(password_typed)

    if account_typed in accounts_list and password_typed == accounts_list[account_typed]['password']:
        clear = 'cls' if os.name == 'nt' else 'clear'
        os.system(clear)

        print('------------------------------------')
        print('---------------- ATM ---------------')
        print('------------------------------------')
        print('1 - Balance')
        print('2 - Plunder')
        if accounts_list[account_typed]['adm']:
            print('10 - Include ballots')
        option_typed = input('Chose an option above: ')
        if option_typed == '1':
            print('Your balance is %s' % accounts_list[account_typed]['value'])
        elif account_typed == '10':
            amount_typed = input('How many ballots: ')
            money_bill_typed = input('Value of ballots: ')
            money_slips[money_bill_typed] += int(amount_typed)
            print(money_slips)
        elif option_typed == '2':
            value_typed = input('Enter the amount to be withdrawn: ')

            money_slips_user = {}
            value_int = int(value_typed)

            if value_int // 100 > 0 and value_int // 100 <= money_slips['100']:
                money_slips_user['100'] = value_int // 100
                value_int = value_int - value_int // 100 * 100
            if value_int // 50 > 0 and value_int // 50 <= money_slips['50']:
                money_slips_user['50'] = value_int // 50
                value_int = value_int - value_int // 50 * 50
            if value_int // 20 > 0 and value_int // 20 <= money_slips['20']:
                money_slips_user['20'] = value_int // 20
                value_int = value_int - value_int // 20 * 20
            if value_int != 0:
                print('The cashier does not have banknotes available in this value')
            else:
                for money_bill in money_slips_user:
                    money_slips[money_bill] -= money_slips_user[money_bill]
                print('Take the banknotes: ')
                print(money_slips_user)
    else:
        print('Invalid account')

    input('Press enter to continue...')  # paused program
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)
