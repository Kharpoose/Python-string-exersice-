def remove_char(str, x):
    
    first = str[:x]
    
    last = str[x+1:]
    
    return first + last 


print(remove_char('pasta in italy', 3))