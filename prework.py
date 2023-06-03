#Question 1: 
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function

def hello_user(user_name):
    """Display a simple greeting."""
    print("hello_" + user_name.upper() +"!")

#Above is basic greeting formatting with a specialized .upper because of the nature of the output wanted
# can easily be .title or just username if funciton needed

#Below is largely unnecessary if the assignment allows the following:
#hello_name(USERNAME) as the last input. 
# The version below asks for the required input and then converts it to the format of the requested output

user = input("Please enter USERNAME: ")
hello_user(user)


#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """Print the odd numbers from 1-100"""
    for num in range(1,100):
        if int(num) % 2 == 0:
            continue
        else:
            print(num)
    


first_odds()

#this print function shows that there is no return but isn't as clean as the print function above
# in particular, the function itself performs the printing so another print function just spits 
# out the None at the bottom. 

# print(first_odds())


# The entire above function sucks a bit if the range needs to be changed from 1-100 to something else but 
# that would be solved by inserting an input function like below between lines 2 and 3 and altering the range on
# line 3 to read range(int(l_num),int(h_num)):


#def first_odds():
#     """Print the odd numbers from 1-100"""
    
#     l_num = input("What is the low number of your desired range? ")
#     h_num = input("what is the high number of your desired range? ")
    
#     for num in range(int(l_num),int(h_num)):
#         if int(num) % 2 == 0:
#             continue
#         else:
#             print(num)

#Question 3: Please write a Python function, max_num_in_list to return the max number of a given list. 
# The first line of the code has been defined as below.

#pretty direct set of commands
def max_num_in_list(a_list):
    high_num = max(a_list)
    return high_num

#less straightforward but lets us sort and then pop the last number. This version becomes tricky when including mixed 
#str and int lists rather than the version above

# def max_num_in_list(a_list):
#     a_list.sort()
#     high_num = a_list.pop() 
#     return high_num


#prover to print the sorted list, sample list given

a_list = [4,2,6,7,8,11,36,7,8,333,43,89]
print(max_num_in_list(a_list))


#Question 4: Write a function to return if the given year is a leap year.The return should be boolean Type (true/false)



def is_leap_year(a_year):
    a_year = int(a_year)
    if a_year % 4 == 0:
        if a_year % 100 == 0 and a_year % 400 != 0:
            return False
        return True  
    else:
        return False

#version above returns a boolian response, version below prints an actual response to the given year.

def is_leap_year(a_year):
    a_year = int(a_year)
    if a_year % 4 == 0:
        if a_year % 100 == 0 and a_year % 400 != 0:
            print("No, " + str(a_year) + " is not a leap year!")
        else:
            print("Yes, " + str(a_year) + " is a leap year!")  
    else:
         print("No, " + str(a_year) + " is not a leap year!")


#UX/UI interface for checking the year in question

a_year = input("Which year would you like to test to see if it is a leap year?" )
is_leap_year(a_year)


#Question 5: Write a function to check to see if all numbers in list are consecutive numbers. For example,
#  [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers.
#  The return should be boolean Type

#The question does not say that the list to be checked should be manipulated (namely, sorting it before checking) 
#so this program will check to see if a raw info list is consecutive rather than being a list made of up consecutive numbers
# that are out of order within the list. Also am assuming the list is a list made entirely of integers rather than being fed
#a list of mixed integers and strings or even one of only strings...As far as I know, I will likely cause an error if I try and 
#manipulate a string like an integer and I don't think I can convert unless it is a numerical string.
        

#this function returns a false if there are repeats
#also returns false if the list is made up of consecutive numbers that are out of order

def is_consecutive(a_list):
    """Checks to see if a list of integers are consecutive and in order"""
    #checks for repeats and returns false
    if len(a_list) != len(set(a_list)):
        return False
    #counter set to provide compare variable with correct ascending value
    n=0
    while True:
        for i in a_list:
            compare = a_list[1] + n
            if compare - i != 1:
                return False
            else:
                n += 1 
        return True

#Test Lists

print(is_consecutive([10,2,3,4,5,6,7,8,9,1]))
                   
print(is_consecutive([1,2,3,4,5,6,7,8,9,10]))

print(is_consecutive([-2,-1,0,1,2,3,4,5,6,7,8]))
    
print(is_consecutive([13,46,7,3,2,3,4]))

print(is_consecutive([-11,2,34,7,3,100]))

print(is_consecutive([1,2,3,4,5,6,7,7,8,10]))

print(is_consecutive([1,20,36,44,53,67,37,58,97,10]))
