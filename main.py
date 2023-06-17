from utils import clear, header
import operation
from file import load_bank_data
from bank_account_variables import money_slips, account_list


def main():
    load_bank_data()
    print(money_slips)
    print(account_list)
    header()
    account_auth = operation.auth_account()

    if account_auth:
        clear()

        header()
        option_typed = operation.get_menu_options_typed(account_auth)
        operation.do_operation(option_typed, account_auth)
    else:
        print('Invalid account')


if __name__ == '__main__':
    while True:
        main()

        input('Press enter to continue...')  # paused program

        clear()
