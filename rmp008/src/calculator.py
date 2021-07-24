def basic_calculator (nb1, nb2, op):
    result = 0 # write your code to perform the operation & return the good result
    #if nb2==0:
        #print("Can’t divide by 0")
    if  op =='+':
        result=nb1+nb2
        
    elif op=='-':
        result=nb1-nb2
       
    elif op=='*':
        result=nb1*nb2
        
    elif op=='/':
        try:
            result=nb1/nb2
            
        except ZeroDivisionError:
            result="Can’t divide by 0"
    
    return result
        
if __name__=="__main__":
    

    first_no=float(input("ENTER FIRST NUMBER:"))
    second_no=float(input("ENTER SECOND NUMBER:"))
    operation=input("ENTER THE OPERATION to be performed:")

    result=basic_calculator(first_no,second_no,operation)
    print("{0} {1}  {2} = {3}".format(first_no,operation,second_no,result))