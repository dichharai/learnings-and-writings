import functools

# function being assigned to a variable
def square(number):
    return number*number

get_square = square
print(get_square(2))

def cube(function):
    number_to_cube = 2
    return function(number_to_cube)*number_to_cube

print(cube(square))


def double(number):
    def multiply_by_two():
        return number * 2
    result = multiply_by_two()
    return result

print(double(3))


def double_func(number):
    def multiply_by_two():
        return number * 2
    # returning a reference to a function
    return multiply_by_two

# assigning a function to a variable
doubled = double_func(3)
print(doubled()) # prints 6

def lowercase_decorator(function):
    def wrapper():
        val = function()
        make_lower = val.lower()
        return make_lower
    return wrapper

def replace_space_with_dash(function):
    def wrapper():
        val = function()
        dashed_val = val.replace(' ', '-')
        return dashed_val
    return wrapper

'''
def say_bye():
    return 'HASTA LA VISTA'

# assigning returned function to a variable
decorate = lowercase_decorator(say_bye)
print(decorate()) # prints 'hasta la vista'

'''

@replace_space_with_dash
@lowercase_decorator
def say_bye():
    return 'HASTA LA VISTA'

print(say_bye())

def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print(f'My arguments are {arg1}, {arg2}.') # prints 'My arguments are avacado-toast, orange-juice.'
        function(arg1, arg2)
    return wrapper_accepting_arguments

@decorator_with_arguments
def breakfast(food_0, food_1):
    print(f'Breakfast I prefer is {food_0} and {food_1}.')

breakfast('avacado-toast', 'orange-juice') # prints 'Breakfast I prefer is avacado-toast and orange-juice.'

def decorator_with_variable_args(function):
    def wrapper_accepting_var_args(*args, **kwargs):
        print(f'Positional argumenrs are {args}.')
        print(f'Keyword arguments are {kwargs}.')
        function(*args, **kwargs)
    return wrapper_accepting_var_args

@decorator_with_variable_args
def variable_breakfast(*args, **kwargs):
    print(f'Number of breakfast food style: {len(args)}')
    print(f'Number of nation breakfast food style: {len(kwargs)}')

variable_breakfast('smoked-salmon', 'fresh-avacado', 'sprouted-whole-grain', Swaziland = "emasi, umncweba, umkhunsu, porridge, corn on the cob")


def decorator_maker_with_args(deco_arg0, deco_arg1, deco_arg2):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(func_arg0, func_arg1, func_arg2):
            """ This is a wrapper function """
            print("The wrapper function can acees all the variables enclosing it. In this case both decorator and function arguments.")
            print(f'Decorator maker arguments: {deco_arg0}, {deco_arg1}, {deco_arg2}.')
            print(f'Function arguments: {func_arg0}, {func_arg1}, {func_arg2}.')

            function(func_arg0, func_arg1, func_arg2)
        return wrapper
    return decorator

@decorator_maker_with_args('Europe', 'Africa', 'South America')
def places_to_travel(place0, place1, place2):
    """This lists some of the country on my travel-list. """
    print(f'This is one of my travel list: {place0}, {place1}, {place2}.')
places_to_travel('Bulgaria', 'Zambia', 'Peru')
print(places_to_travel.__name__)
print(places_to_travel.__doc__)
