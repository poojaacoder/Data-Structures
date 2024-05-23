

# string alphabest total are 26
#  ascii code 65 = A, 90 = Z
# ascii code 97= a, 122 = z
# 
def reverse_1():
    string = "geeks quiz practice code"
    s = string.split()[::-1]
    print(' '.join(s))

    string = "my name is pooja"
    print(string.split(' '))

reverse_1()

def remove_int():
    s= "hfugdowdfkbbsd6773ndfjhkds879232"
    return ''.join([char for char in s if not char.isdigit()])

print(remove_int())


