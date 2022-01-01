# def Hello(name):
#     print('Hi', name)
#
#
# def Hello1(name):
#     print(f'Hello,{name}')
#
#
# def Hello2(name, hobby):
#     print(f'Hi, My name is {name}, My hobby is {hobby}')
#
#
# Hello('SEO')
# Hello1('SEO')
# Hello2('SEO', 'game')


def info(name, address, phone):
    print(f'제 이름은 {name}이고, 주소는 {address}입니다\n'
          f'제 전화번호는 {phone}이에요')


info('주영', '달성군', '0101010101')

a, b = 5, 7
print(a, b)
a, b = b, a
print(a, b)
