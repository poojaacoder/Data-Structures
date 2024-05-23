"""Python program to capitalize
the first character and the last character
of each word in the string"""

# Taking the strign input
test_str = "welcome to geeksforgeeks"


# Without any changes in the string
print("String before:", test_str)
# Creating an empty string
string = ""

print(test_str.title().split())

st =[]
for i in test_str.title().split():
    i = i[:-1] + i[-1].upper()
    st.append(i)


print(' '.join(st))


def word_cap(x):

    return ' '.join(map(lambda x: x[0].upper()+x[1:-1]+x[-1].upper(), x.split()))

print(word_cap("hello world"))



