n1 = input("what is your first number: ")
n2 = input("what is your second number: ")
n3 = input("what is your operation: ")
def awnser(n1,n2):
    if n3 == "+":
        print(int(n1)+int(n2))
    if n3 == "-":
        print(int(n1)-int(n2))
    if n3 == "*":
        print(int(n1)*int(n2))
    if n3 == "/":
        print(int(n1)/int(n2))
return(awnser)