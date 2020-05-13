def add_num(num1, num2):
    return num1 + num2

result = add_num(2,4)
print(result+10)

# max and min
print(max([1,4,7,12,100]))
print(min([1,4,7,12,100]))

# enumerate
mylist = ['a','b', 'c']

for index,letter in enumerate(mylist):
    print(letter)
    print("is at index {}".format(index))
    print('')

# .join
mylist = ['a','b','c','d']
print('--'.join(mylist))

def secret_check(mystring):
    return 'secret' in mystring.lower()

def code_maker(mystring):
    output = list(mystring)
    for index, letter in enumerate(mystring):
        for vowel in 'aeiou':
            if letter.lower()==vowel:
                output[index] = 'x'
    output = ''.join(output)
    return output

print(secret_check('this is a Secret'))
print(code_maker('Sammy'))