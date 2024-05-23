
def multi(numb):
    k = [num * 5 for num in numb]
    return k

print(multi([1,2,3,4,5]))

numb=[3,4,5,6,7]
def multi_2(numb):
    return list(map(lambda x : x*5, numb))

print(multi_2(numb))