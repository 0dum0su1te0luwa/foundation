import argparse

if __name__=='__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('n1', type=int)
    parser.add_argument('n2', type=int)
    parser.add_argument('operation', choices=['add','div','sub','mult'])

    arg = parser.parse_args()

    num1 = arg.n1
    num2 = arg.n2

    result = None

    if arg.operation == "add":
        result = num1 + num2
    elif arg.operation == "sub":
        result = num1 - num2
    elif arg.operation == "div":
        try:
            result = num1/num2
        except ZeroDivisionError as e:
            print('unsupported operation:',e)
    elif arg.operation == "mult":
        result = num1 * num2

    print('result = ',result)

