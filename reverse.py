


from re import L
import string


def Statement():
    school_statement= "I am akirachix"
    x= school_statement.split()
   
    start = 0
    end = len(x)-1
  

    
    while start < end:
        x[start],x[end] = x[end],x[start]
        
        start+= 1
        end -= 1
        strings = " "
        
    print(strings.join(x))
    
Statement()

# #reverse a palindrome using two pointer technique
# def palindrome():
#     teacher = "madam"
    
#     first = 0
#     last = len(teacher)-1
    
#     while first < last:
#         [first],[last] = [last],[first]
        
#         # if (first == last):
#         #     print("this is a palindrome")
            
        
#         first += 1
#         last -= 1
        
#         names = ""
#     print(names.join(teacher))
    
# palindrome()

def palindrome_test():
    
    s = input("Enter a word;").lower()
    
   # s ==reverse of s then its a palindrome
   
    point1 = 0
    point2 = len(s)-1
    
    
    
    reverse = s[point1],s[point2] == s[point2], s[point1]
    
    if (s != reverse):
        print("its a palindrome")
        
    else:
        print("its not palindrome")
 
palindrome_test()
    

