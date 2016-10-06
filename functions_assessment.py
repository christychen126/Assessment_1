# PART ONE

# 1. We have some code which is meant to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5% 

def tax_calculator(state, cost, tax = 0.05):
    """Calculates total_cost of an item, state tax figure"""

    if state == "CA":
        tax = 0.07

    total_cost = cost + cost * tax

    return total_cost


#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.


def is_berry(fruit):
    """Determines if the fruit is in berry list"""

    if fruit in ["strawberry", "cherry", "blackberry"]:
        return True
    else:
        return False


def shipping_cost(fruit):
    """Calculates shipping cust of fruit"""

    if is_berry(fruit) is True:
        return "0"
    else:
        return "5"




# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#
#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.
#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.


def is_hometown(hometown):
    """check if unser input hometown is the same as my hometown"""

    return hometown == "Kaohsiung"


def full_name(firstname, lastname):
    """Construct user full name""" 

    return firstname + " " + lastname


def hometown_greeting(hometown, firstname, lastname):
    """Output greetings depends on is_hometown function"""

    user_hometown = is_hometown(hometown)
    user_full_name = full_name(firstname, lastname)

    if user_hometown:
        print "Hi, %s, we're from the same place!" % (user_full_name)
    else:
        print "Hi %s, where are you from?" % (user_full_name)



#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()``
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.


def increment(x = 1):
    """ Create function that increment a fixed number"""

    def add(y):
        return x + y

    return add



# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call
#    addfive with y = 5. Call again with y = 20.


addfive = increment(5)
addfive(5)
addfive(20)


# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def append_number(number, a_list):
    """Append the given number to the end of the list """
    a_list.append(number)
    return a_list





#####################################################################