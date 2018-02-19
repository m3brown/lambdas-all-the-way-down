import random

def appender(suffix):
    '''
    Return a function that appends text
    to the end of a provided string
    '''
    return lambda text: text + suffix

def biased_number_generator(bias_word):
    '''
    Return a function that is a random number generator,
    except it prefers one key that gets a high value
    '''
    return lambda x: 225 if x == bias_word else random.randint(1, 101)
