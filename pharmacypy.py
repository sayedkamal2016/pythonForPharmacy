def start():
    password = ''

    while password != 'admin':
        password = input('input your password: ')
        if password == 'admin':
            print('welcome maam')
            main()
        else:
            print('incorrect password please try again')


def main():
    print("""welcome what would you 
             like to do today:
             1. add a product
             2. remove a product""")

    ask = int(input('what would you like to do: '))

    if ask == 1:
        add()
    elif ask == 2:
        sub()
    elif ask != 1 or 2:
        print('no such operation found')
        start()


def add():
    dict = {'cosmetics' : ['eye shadow' , 'foundation' , 'powder' , 'lip stick' , 'blush' ,'eye liner' , 'contour'] , 'pharmacuticals': ['cough syrups' , 'malaria drugs' , 'vitamins' , 'condom' , 'panadol' , 'eye drop' ]}
    print('''would you like to see the list of
             1. cosmetics 
             2. pharmacuticals''')

    ans = int(input('what would you like to check: '))

    if ans == 1:
        print(dict['cosmetics'])
        ee = input('what is the name of product you would like to add: ')
        print(ee,'has been added to your list of cosmetics')
    elif ans == 2:
        print(dict['pharmacuticals'])
        bb = input('what is the name of product you would like to add: ')
        print(bb,'has been added to your list of pharmacuticals')
    elif ans != 1 or 2:
        print('no such operation found')


def sub():
    dict = {'cosmetics': ['eye shadow', 'foundation', 'powder', 'lip stick', 'blush', 'eye liner', 'contour'],
            'pharmacuticals': ['cough syrups', 'malaria drugs', 'vitamins', 'condom', 'panadol', 'eye drop']}
    print('''
            where would you like 
            to remove your the product
            from the
             1. cosmetics section
             2. pharmacuticals section''')

    lam = int(input('what is your decision: '))

    if lam == 1:
        print(dict['cosmetics'])
        lde = input('what would you like to remove from your cosmetics items: ')
        print(lde,'has been removed from the list of your cosmetics')

    elif lam == 2:
        print(dict['pharmacuticals'])
        edf = input('what you like to remove from your pharmacuticals items: ')
        print(edf,'has been removed from your list of pharmacuticals')

    elif lam != 1 or 2:
        print('no such operation found')

# start = input('would you like to continue y/n: ')
#
# if start == 'y':
#     start()
#
# elif start == 'n':
#     exit()


start()