import string 
from random import * 

def finalstage(w): 
    h=0 
    w = list(w) 
    w.reverse() 
    w = "".join(g for g in w) 
    flag = ''
    while h < len(w): 
        try: 
            flag += w[h+1] + w[h] 
        except: 
            flag += w[h] 
        h+=2 
    return flag 

def finalstage_undo(w):
    h=0 
    
    flag = ''
    while h < len(w):
        try: 
            flag += w[h+1] + w[h] 
        except: 
            flag += w[h] 
        h+=2 
    w = list(flag) 
    w.reverse() 
    w = "".join(g for g in w) 
    return w 


def stage2(b):
    seed(10)
    t = ''
    for q in range(len(b)): 
        t += chr(ord(b[q])-randint(0,5)) 
    return t


def stage2_undo(b):
    seed(10)
    t = ''
    for q in range(len(b)):
        t += chr(ord(b[q])+randint(0,5))
    return t


def stage1(a): 
    a = list(a) 
    for o in range(len(a)): 
        a[o] = chr(ord(a[o])^o) 
    z = "".join(x for x in a) 
    return z


def stage1_undo(a):
    a = list(a)
    for o in range(len(a)):
        a[o] = chr(ord(a[o])^o)
    z = "".join(x for x in a)
    return z


def entry(f): 
    f = list(f) 
    f.reverse() 
    f = "".join(i for i in f) 
    return f


def entry_undo(f):
    return f[::-1]


def do_stage(input, func, func_undo):
    print(f'{func.__name__}')
    print(f'\tinput: {input}')
    output = func(input)
    print(f'\toutput: {output}')
    if func_undo:
        print(f'\tundo: {func_undo(output)}')
    return output


if __name__ == '__main__':
    input = input("Enter Flag: ") 

    print('')
    '''
    a = do_stage(input, entry, entry_undo)
    b = do_stage(a, stage1, stage1_undo)
    c = do_stage(b, stage2, stage2_undo)
    d = do_stage(c, finalstage, finalstage_undo)
    '''

    a = do_stage(input, finalstage_undo, finalstage)
    b = do_stage(a, stage2_undo, stage2)
    c = do_stage(b, stage1_undo, stage1)
    d = do_stage(c, entry_undo, entry)
    
    
    
