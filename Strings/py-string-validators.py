s = raw_input()
isalnum, isalpha, isdigit, isupper, islower = False, False, False, False, False
for i in s:
    if i.isalnum() == True:
        isalnum = True
    if i.isalpha() == True:
        isalpha = True
    if i.isdigit() == True:
        isdigit = True
    if i.islower() == True:
        isupper = True
    if i.isupper() == True:
        islower = True
print isalnum
print isalpha
print isdigit
print isupper
print islower
