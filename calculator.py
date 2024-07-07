logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1,n2):
    return n1 + n2
def substract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2
tasks = {"+":add,"-":substract,"*":multiply,"/":divide}
function = tasks["*"]
def calculator():
    print(logo)
    num1 = float(input("What is your first number? "))

    for keys in tasks:
        print(keys)
    tasks_symbol = input("Pick an operation from the line above ")
    num2 = float(input("What is your second number? "))
    for keys in tasks:
        if tasks_symbol == keys:
            func = tasks.get(keys)
            answer = (func(num1,num2))
    print(f"{num1} {tasks_symbol} {num2} = {answer}")
    go_or_stop = input(f"type 'y' to continue calculating with {answer}, or type 'n' to exit. ").upper()
    while go_or_stop == "Y":
        tasks_symbol = input("Pick an operation ")
        num3 = float(input("What's the next number? "))
        calculating_function = tasks[tasks_symbol]
        next_answer = calculating_function(answer,num3)
        print(f"{answer} {tasks_symbol} {num3} = {next_answer}")
        go_or_stop = input(f"type 'y' to continue calculating with {next_answer}, or type 'n' to restart calculating. ").upper()
        answer = next_answer
    if go_or_stop == 'N':
        calculator()
calculator()
print('calculator ends')



