class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount instance.
        :param initial_balance: (float) optional starting balance, defaults to 0.
        """
        self.__account_balance = initial_balance  # encapsulated attribute

    def deposit(self, amount):
        """
        Deposit the specified amount into the account.
        :param amount: (float) amount to deposit
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if funds are sufficient.
        :param amount: (float) amount to withdraw
        :return: True if successful, False otherwise
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Display the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
