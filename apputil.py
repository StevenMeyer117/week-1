

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

def is_parentheses_balanced(sequence):
    """
    Checks if the number of opening and closing parentheses match.
    """
    return sequence.count("(") == sequence.count(")")


# Test program
if __name__ == "__main__":
    test_1 = "(here is a word) and (here is another word) and (here is not"
    test_2 = "(But here is a word) and (here is another word) and (here is the last word)"

    print(is_parentheses_balanced(test_1))
    print(is_parentheses_balanced(test_2))