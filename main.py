####################################
######### Ganugula Vardhan #########
####################################

print("Simple Arithmetic Calculator")

try:
        num1 = int(input("Enter the number: "))
        num2 = int(input("Enter the number: "))
        print("""
####################################################
#                                                  #
#        +-*/^%~ Aritmetic Calculator ~%^/*-+      #
#                                                  #
#        Addition          ( + )                   #
#        Substraction      ( - )                   #
#        Multiplication    ( * )                   #
#        Division          ( / )                   #
#        Remainder/Modulo  ( % )                   #
#        Exponent          ( ^ )                   #
#        Floor Division    ( ~ )                   #
#                                                  #
####################################################

        """)
        operator = input('Enter the operator: ')

        match(operator):
                case '+': print(str(num1+num2))
                case '-': print(str(num1-num2))
                case '*': print(str(num1*num2))       
                case '/': print(str(num1/num2))
                case '%': print(str(num1%num2))
                case '^': print(str(num1**num2))
                case '~': print(str(num1//num2))
                case _ : print("Operator Not found") 
except ZeroDivisionError:
        print("Denominator should not be Zero 0 ")
except Exception as e:
        print("Exception Occured : " + str(e))
