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



def item_cost_after_tax(state, item_cost, tax = 0.05):
    """ Calculate the after tax cost of item dependent on state """

    if state == "CA" or state == "Ca" or state == "ca":
        total_cost = item_cost * 0.07 + item_cost
        return total_cost
        print total_cost
    else: 
        total_cost = item_cost * tax + item_cost
        return total_cost
        print total_cost


# state = raw_input("Hello, what state are you from? ")
# tax = float(raw_input("What is your tax rate? (If you don't know, put 0) "))
# item_cost = float(raw_input("How much was your item? "))

# print item_cost_after_tax(state, item_cost, tax=0.05)

#####################################################################
# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or 
#        "blackberry".

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function 
#        within the `shipping_cost()` function and returns `0` if ``is_berry()
#        == True``, and `5` if ``is_berry() == False``.

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

def is_berry(name):
    """ Returns True if input name is strawberry, cherry, or blackberry else False. """
    name = name.lower()
    if name == "strawberry" or name == "cherry" or name == "blackberry":
        return True
    else:
        return False

print is_berry("Orange")

def shipping_cost(name):
    """ Calculates shipping cost by calling is_berry() function. 

    If is_berry() is true, return 0. Otherwise return 5. 
    """

    if is_berry(name) == True: 
        return 0 
    else: 
        return 5

print shipping_cost("strawberry")

def is_hometown(town):
    """ If hometown is equal to San Francisco, return True """

    if town == "San Francisco": 
        return True
    else: 
        return False

def full_name(first, last):
    """ Returns first and last name """

    return first + last

def hometown_greeting(town, first, last):
    """ If hometown is San Francisco, print "We're from the same place" otherwise ask where user is from """

    if is_hometown(town) == True: 
        print "Hi, {} {}, we're from the same place!".format(first,last)
    else:
        print "Hi, {} {}, wehere are you from?".format(first,last)

print hometown_greeting("Chicago", "James", "Stu")



#####################################################################

# PART THREE

# 1. Write a function ``increment()`` with a nested inner function, ``add()`` 
#    inside of it. The outer function should take ``x``, an integer which
#    defaults to 1. The inner function should take ``y`` and add ``x`` and ``y`` together.

# 2. Call the function ``increment()`` with x = 5. Assign what is returned to a variable name, addfive. Call 
#    addone with y = 5. Call again with y = 20. 

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.

#####################################################################

def increment(x = 1):
    """ Outer function takes a parameter x that defaults to 1 """

    def add(y): 
        """ Inner function takes parameter y and returns x from outer function added to y """

        #inner function returns x + y 
        return x + y
    #outer function returns the inner add function    
    return add

    #calling increment with parameter 5 setting to variable addfive 
addfive = increment(5)

print addfive(5)
print addfive(20)



def add_num_to_list(num, num_list):
    """ Append a number to an existing list of numbers. """ 

    #Append num to num_list
    num_list.append(num)
    return num_list

print add_num_to_list(5, [1,2,3,4])
    



