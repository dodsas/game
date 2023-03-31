
def test():
    raise Exception("ERROR 테스트")

def test2():
    return 1, 2

# try:
#     test()

# except Exception as e:
#     print(e)

a, b =test2()
print(a)
print(b)
