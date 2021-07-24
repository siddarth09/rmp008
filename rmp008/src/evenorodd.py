def even_or_odd(n):
    if n%2==0:
        return "EVEN"
    else:
        return "ODD"

if __name__=="__main__":
    number=int(input("ENTER THE NUMBER"))
    result=even_or_odd(number)
    print(result)