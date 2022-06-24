


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

#reverse a palindrome using two pointer technique
def palindrome():
    teacher = "madam"
    
    first = 0
    last = len(teacher)-1
    
    while first < last:
        [first],[last] = [last],[first]
        
        first += 1
        last -= 1
        
        names = ""
    print(names.join(teacher))
    
palindrome()

