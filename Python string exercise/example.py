def sting_change(str):
    leng = len(str)
    
    if leng < 2:
        return ''
    
    return str[0:2] + str[-2:]


print(sting_change('sempla'))
print(sting_change('se'))
print(sting_change('xali'))