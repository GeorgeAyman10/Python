def myfunc(strn):
    my_list=[]
    str=''
    for i in range(0,len(strn)):
        if i%2==0:
            my_list.append(strn[i].lower())
        else:
            my_list.append(strn[i].upper())
    return str.join(my_list)
            
