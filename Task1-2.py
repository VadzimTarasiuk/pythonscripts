#otherstring = 'abc12321cba'
otherstring = 'this is not a polyndrome'
stringLength = len(otherstring)
center = stringLength//2
for i in range(center + 1):
    print(str(otherstring[center - i]) + ' ' + str(otherstring[center]) + ' ' + str(otherstring[center + i]))
    if otherstring[center + i] != otherstring[center - i]:
       print('Not a Polyndrome')
       exit(0)
print('Polyndrome = True')
