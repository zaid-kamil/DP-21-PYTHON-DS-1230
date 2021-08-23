# parameterized functions take input when you call them
# there are 5 ways to call a parameterized function
# 1. with required parameters ✔
# 2. with keyword/named parameters ✔
# 3. with default parameters ✔
# 4. with variable arguments ✔
# 5. with keyword arguments ✔
#########################################################
'''
def showMessage(msg):
    print('*' * 30)
    print(msg)
    print('*' * 30)
'''

def showMessage(msg, symbol):
    print(symbol*30)
    print(msg)
    print(symbol*30)

if __name__ == '__main__':
    # directly parameterized function call
    showMessage('The Stormlight Archives',">>")
    showMessage("Brandon Sanderson",'*')

    # user input based parameterized function call
    quote = input('enter your quote: ')
    showMessage(quote,'#')