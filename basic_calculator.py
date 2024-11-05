title_ = '''
Basic Calculator

    python: v3.12

    code version: 1.0.0
    creation date: 02-11-2024 (dd-mm-yyyy)
    created by: Amit Raichurkar 

    SCOPE: 
        Basic Math operations over two operands (real numbers)
        [Addition, Subtraction, Multiplication, Division, Power, Modulus,...]
'''


def add(a:float,b:float) ->float:
    '''addition of two numbers'''
    return a+b


def sub(a:float,b:float) ->float:
    '''subtraction of two numbers'''
    return a-b


def mul(a:float,b:float) ->float:
    '''multiplication of two numbers'''
    return a*b


def div(a:float,b:float) ->float:
    '''division of two numbers'''
    return a/b


def pow(a:float,b:float) ->float:
    '''exponentiation of two numbers'''
    return a**b


def mod(a:float,b:float) ->float:
    '''exponentiation of two numbers'''
    return a%b


if __name__ == '__main__':

    print(title_)

    dict_math = {
        '1': ('Addition',add,'+'),
        '2': ('Subtraction',sub,'-'),
        '3': ('Multiplication',mul,'x'),
        '4': ('Division',div,'/'),
        '5': ('Power',pow,' raised to '),
        '6': ('Modulus',mod,'%'),
        '7': ('Exit',None,None),
    }

    while True:

        print('\nMath operations in Calculator (only two operands) ->')
        for data in [f'{k} -> {v[0]}' for k,v in dict_math.items()]:
            print(f'''   {data}''')

        op = input(f'\nSelect the math operation: ')

        math_func = dict_math.get(op,None)
        if math_func == dict_math['7']:
            break
        elif math_func is None:
            print('Invalid Entry, please try again')
            continue

        try:
            ai = input('Enter the first number: ')
            a = float(ai)
            bi = input('Enter the second number: ')
            b = float(bi)

            result_ = dict_math[op][1](a,b)
        except BaseException as err:
            print(f'''<< ERROR >> {err}''')
            continue
        
        operation_ = dict_math[op][0]
        operator_ = dict_math[op][2]
        print(f'''==> {operation_}: {ai}{operator_}{bi} = {result_}''')

        input('\n Press <Enter> to continue...')
