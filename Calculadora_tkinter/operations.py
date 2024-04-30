import math as m
from logger import log

class Calculator:

    @classmethod
    def checking(cls, args):
        special_char = ['\u00F7', 'x', '\u221A']
        numbs = [str(x) for x in range(10)]
        neg_numbs = [str(x-9) for x in range(10)]
        data = ''
        verification = False

        # Verifico si la expresion ingresada es valida
        test = args[0:3]
        log.info(test)
        for end in neg_numbs:
            log.info(end)
            if test in neg_numbs:
                verification = True
            else:
                for sig in numbs:
                    if not sig in numbs:
                        verification = False
                    else:
                        verification = True
        log.info(f'Pass: {verification}')

        # Si la expresion ingresada es valida se procede a realizar la operacion.
        if verification:
            for simb in args:
                if simb in special_char:
                    match simb:
                        case 'x':
                            simb = simb.replace('x', '*')
                        case '\u00F7':
                            simb = simb.replace('\u00F7', '/')
                        case '\u221A':
                            args = args.split("\u221A")
                            log.info(args)
                            return args
                data += simb
        else:
            data = None
        return data

    @classmethod
    def operaciones(cls, operation):
        sty = type(operation)
        try:
            if operation == None:
                raise ValueError('Operacion Valida: False')
            elif sty == str:
                result = eval(operation)
                return result
            elif sty == list:
                numbs = eval(operation[1])
                numbs = abs(int(numbs))
                result = m.sqrt(numbs)
                return f'{result:.8f}'
        except ValueError as e:
            log.error(e)
            return 'e'
        except Exception as e:
            log.error(e)
            return 'e'

if __name__ == '__main__':
    data = ('-*/')
    raiz = Calculator.checking(data)
    print(Calculator.operaciones(raiz))
    m.sqrt(-99)
