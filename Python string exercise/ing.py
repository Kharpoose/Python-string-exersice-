def add_Ing(str):
    leng = len(str)
    
    if leng > 2:
        if str[-3:] == 'ing':
            str += 'ly'
        else: 
            str += 'ing'
            
            
    return str


print(add_Ing('aling'))            