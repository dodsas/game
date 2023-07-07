from wcwidth import wcswidth

def ljustk(str, length):
    if type(str) is int:
        str = str.__str__()

    retVal = f'{str.ljust(length - (wcswidth(str) - len(str)))}'
    return retVal

def rjustk(str, length):
    # if str is int type, convert to str type
    if type(str) is int:
        str = str.__str__()

    retVal = f'{str.rjust(length - (wcswidth(str) - len(str)))}'
    return retVal