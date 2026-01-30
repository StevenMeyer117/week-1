

# add code below ...

# Exercise 1:

# Create a function palindrome(word) that receives a string and returns True or False depending on whether it is a palindrome.
# You can design the function to change all letters to lowercase and ignore spaces.

def palindrome(word):
    """
    Checks if a string is a palindrome while ignoring case or spaces.
    """
    word = word.lower()
    word = "".join(char for char in word if char.isalnum())
    return word == word[::-1]

if __name__ == "__main__":
    print(palindrome("Can NAc"))



# Exercise 2:

# Write a function parentheses(sequence) that takes a string and returns True if the string's parentheses are balanced, False if not.
# Try to come up with a second way to complete the problem.

def parentheses(sequence):
    """
    Checks if parentheses are balanced by ensuring the running count
    never drops below zero and ends at exactly zero.
    """
    balance = 0
    for char in sequence:
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1
            
        # If balance drops below zero, there are unmatched closing parentheses
        if balance < 0:
            return False
        
    return balance == 0


# Test program
if __name__ == "__main__":
    test_1 = "(here is a word) and (here is another word) and (here is not"
    test_2 = "(But here is a word) and (here is another word) and (here is the last word)"

    print(parentheses(test_1))
    print(parentheses(test_2))
