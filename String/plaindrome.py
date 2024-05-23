
def is_palindrome(st):
    a = st
    reversed_a = st[::-1]
    if a == reversed_a:
        return True
    else:
        return False
    
def is_symmetrical(st):
    a = st
    
    leng = int(len(st) /2)
    first= st[:leng]
    last = st[leng:]
    print(first, last)
    if first == last:
        return True
    else:
        return False
    

def plaindrome_logic(st):
    n = len(st)
    start = 0
    if n % 2:
        mid = (n/2 ) +1
    else:
        mid = n/2
    last = n-1
    flag = 0
    while (start < mid):
        if st[start] == st[last]:
            start +=1
            last -=1
        else:
            flag +=1
            break

    if flag == 0:
        return True
    else:
        return False


def symmetric_logic(st):
    n = len(st)
    start = 0
    if n % 2:
        mid = (n//2 )+1
    else:
        mid = n//2
    last = n-1
    flag = 0
    start2= mid

    while (start < mid and mid < last):
        if st[start] == st[start2]:
            start+=1
            start2+=1
        else:
            flag +=1
            break
    if flag == 0:
        return True
    else:
        return False
    



print(is_palindrome("poojajffoop"))
print(plaindrome_logic("khokho"))
print(is_symmetrical("khokho"))
print(symmetric_logic("amaama"))
print(plaindrome_logic("amaama"))