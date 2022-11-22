output = []
operator = []

#giving priority
priority = {'(':0,'+':1,'-':1,'*':2,'/':2,'^':3}

#taking input expression
exp = input("Enter the expression: ")

#traversing throught the expression
for ch in exp:
    if (ch=='('):
        operator.append(ch) # add element in the stack [LIFO]
    elif (ch==')'):
        while (operator[-1]!='('): # until we reach to left most index [-1] = top
            element = operator.pop() # pop -> deleter karenge and then,
            output.append((element)) # push thosed poped elements into operator
        operator.pop #closing parenthesis tak pop kardo
    elif (ch == '^' or ch == '*' or ch == '/' or ch == '+' or ch == '-'):
        if(len(operator)>0):
            while(priority[operator[-1]]>=priority[ch]):
                element = operator.pop()
                output.append((element))
                if(len(operator)==0):
                    break
        operator.append(ch)
    else:
        output.append(ch)

while(len(operator)!=0):
    element = operator.pop()
    output.append(element)
print("infix expression =",exp)
print("postfix expression =", end = ' ')
for element in output:
    print(element,end='')
