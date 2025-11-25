# Solution: Even or Odd
def even_or_odd(number):
        '''Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.'''
        try:
            if number % 2 == 0:
                return "Even"
            else:
                return "Odd"
        except:
            return "Your input must be an integer."

# Solution: Convert a Number to a String    
def number_to_string(num):
    return str(num)

# Solution: Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

# Solution: Vowel Count
def get_count(sentence):
    return sum(letter in "aeiou" for letter in sentence)
