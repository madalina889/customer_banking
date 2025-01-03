"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    account = account(balance)
    # Calculate interest earned
    # ADD YOUR CODE HERE
    monthly_rate = interest_rate / 12 / 100  # Convert APR to monthly interest rate
    interest_earned = balance * (1 + monthly_rate) ** months - balance
    # Update the CD account balance by adding the interest earned
    # ADD YOUR CODE HERE
    updated_balance = balance + interest_earned
    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    account.set_balance(updated_balance)
    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE
    account.set_interest(interest_earned)
    # Return the updated balance and interest earned.
    return  updated_balance, interest_earned # ADD YOUR CODE HERE
   