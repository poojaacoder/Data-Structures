def is_anagram(st1, st2):
    if len(st1) != len(st2):
        return False
    n = len(st2)
    st1_dict = {}
    st2_dict= {}

    for i in range(n):
        st1_dict[st1[i]] = st1_dict.get(st1[i], 0) + 1
        st2_dict[st2[i]] = st2_dict.get(st2[i], 0) + 1
    
    print(st2_dict, st1_dict)
    return st1_dict == st2_dict

print(is_anagram("pooja", "ajoop"))
