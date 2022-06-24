# # take two inputs from the user,check if they are equal.
# from cmath import e
# from re import A, I


# def check_inputs():
#     num1 = int(input('enter first number'))
#     num2 = int(input('enter second number'))
    
#     if num1 == num2:
#         print("number 1 is  equal to number 2")
    
#     else:
#         print("number 1 is not equal to number 2")
        
# check_inputs()

#check if the number is square 
#def check_square():
    
#in a string change the other part of the string to lower case and then another to upper case
# def check_lower_case():
#     school = "Akirachix"
#     length = len(school)
#     for i in  length:

#take a string and reverse the string , in which "I am akirachix should be "Akirachix am I""
from calendar import c
from cmath import e
from operator import ne
import string




def rev():
    school_statement= "I am akirachix"
    reverse= school_statement.split()
   
    
    start = 0
    end = len(reverse)-1
    
    while start < end:
      reverse[start],reverse[end] = reverse[end],reverse[start]
        
    start+= 1
    end -= 1
    strings = ""
        
    print(strings.join(reverse))

rev()
     
class Solution():
    
    def __init__(self, s : List[str]) -> None:
        
        def reverse(l,r):
            if l < r:
                s[l],s[r] = s[r], s[l]
                reverse(l+1,r-1)
        reverse(0,len(s)-1)
        
def reverse_a_string_more_slowly(a_string):
    new_strings = []
    index = len(a_string)
    while index:
        index -= 1                       
        new_strings.append(a_string[index])
        
    return ''.join(new_strings)
reverse_a_string_more_slowly("I am akirachix")
def reverse_a_string(string: str) -> str:
    # """
    # This method is used to reverse a string.
    # Args:
    #     string: a string to reverse

    # Returns: a reversed string
    # """
    if type(string) != str:
        raise TypeError("{0} This not a string, Please provide a string!".format(type(string)))
    string_place_holder = ""
    start = 0
    end = len(string) - 1
    if end >= 1:
        while start <= end:
            string_place_holder = string_place_holder + string[end]
            end -= 1
        return string_place_holder
    else:
        return string


a = "madam"
rev = reverse_a_string(a)
print(rev)
            
        
        
    
        
        

    