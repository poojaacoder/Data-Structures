
def find_duplicates(list1):

    unique = []
    duplicates = []
    for i in list1:
        if i not in unique:
            unique.append(i)
        elif i not in duplicates:
            duplicates.append(i)
            if i in unique:
                unique.remove(i)
    print("duplicates", duplicates)
    print("unique", unique)

def if_duplicate(list1):
    if len(list1) == len(set(list1)):
        return True
    
    else:
        return False
    
k = [1,2,3,3,4, 4, 6, 6, 9, 10]
h = [1,7,8,9,5]
print(if_duplicate(k))
print(if_duplicate(h))
find_duplicates(k)