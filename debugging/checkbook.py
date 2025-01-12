class Checkbook:
    """
    A simple Checkbook class to manage a balance with deposit and withdrawal functionality.
    
    This class provides methods to deposit and withdraw money from the balance, 
    check the current balance, and handle simple error cases like insufficient funds.

    Attributes:
    balance (float): The current balance in the checkbook account.
    """
    
    def __init__(self):
        """
        Initializes the Checkbook instance with a balance of 0.0.
        
        No parameters are required for initialization.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Deposits a specified amount into the checkbook balance.

        Parameters:
        amount (float): The amount to deposit. It must be a positive value.

        Returns:
        None: This method does not return a value, but prints the deposit details and updated balance.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the checkbook balance if sufficient funds are available.

        Parameters:
        amount (float): The amount to withdraw. It must be less than or equal to the current balance.

        Returns:
        None: This method does not return a value, but prints the withdrawal details and updated balance. 
              If insufficient funds are available, it prints an error message.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Prints the current balance of the checkbook.

        Parameters:
        None

        Returns:
        None: This method does not return a value, but prints the current balance.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function that runs a simple checkbook management system.
    
    This function allows the user to choose between depositing, withdrawing, checking the balance, or exiting the program.
    Error handling is included for invalid input (e.g., non-numeric values).
    
    Parameters:
    None

    Returns:
    None
    """
    cb = Checkbook()
    
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        
        # Handle exit condition
        if action.lower() == 'exit':
            break
        
        # Deposit money
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                if amount < 0:
                    print("Amount must be positive. Please try again.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Withdraw money
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                if amount < 0:
                    print("Amount must be positive. Please try again.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Check balance
        elif action.lower() == 'balance':
            cb.get_balance()
        
        # Invalid command
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
