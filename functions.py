# this is a long winded version
def print_two(*args):
    arg1, arg2 = args
    print(f'arg1: {arg1}, arg2: {arg2}')

# the arguments can be passed into the parenthesis 
def print_two_again(arg1, arg2):
    print(f'arg1: {arg1}, arg2: {arg2}')

def print_one(arg1):
    print(f'arg1: {arg1}')

def print_none():
    print('I got nothing!')

print_two('George', 'Barrett')
print_two_again('Zed', 'Shaw')
print_one('One ring to rule them all')
print_none()