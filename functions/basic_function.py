def greet(username): #username e un parameter
    return ("Hello from function!" + username)

hello = greet('Paola') #Paola e un argument
print(hello)


# Default value

def describe_animal(name, animal_type='dog'):
    print(animal_type + name)

describe_animal('Iron')

#optional parameter

def build_person(first, middle, last, age=''):
    return(first + middle + last + age)

def get_formatted_name(first_name, last_name):

    full_name = first_name + ' ' + last_name
    while True:
        print("\nPlease tell me your name:")
        print("(enter 'q' at any time to quit)")

        f_name = input("First name: ")
        if f_name == 'q':
            break
        l_name = input("Last name: ")
        
        if l_name == 'q':
            break
    
    return full_name.title()

name = get_formatted_name('ilinca', 'andrei')
print(name)

# print_models(unprinted_designs[:], completed_models) vogliamo mandare una lista che pero non vogliamo che la fun
# la cambi percio con [:] mandiamo uno slice cioe una copia

def build_profile(first, last, *user_info): # due un solo * mi permette di passare quanti args voglio ma non crea
    pass                                    # nessun dictionary or list
def build_profile_2(first, last, **user_info): # due ** creano un dictionaries che key value pairs 
    pass

# Import a function from a module and give it an alias
# from module_name import function_name as alias
# from pizza import make_pizza as mp
# mp('peperoni', 'mushrooms')

#oppure si puo importare tutto il modulo dandogli un alias
# import module_name as mn