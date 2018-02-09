def parenthesis_properly_closed(expression):
    a = evaluate_expression(expression)
    if a == 0:
        return 'Parenthesis are properly closed'
    else:
        return 'Parenthesis are not properly closed'
    
def evaluate_expression(expression):
    a = 0
    if expression != "":
        for c in expression:
            a += evaluate_character(c)
            if a < 0:
                break
    return a

def evaluate_character(c):
    if c == '(':
        return 1
    else:
        return (-1)

def main():
    expression = input('Enter an expression to evaluate (or exit to quit): ')
    if expression != 'exit':
        print(parenthesis_properly_closed(expression))
        main()

main()

