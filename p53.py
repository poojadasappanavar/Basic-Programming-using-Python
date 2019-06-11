def func(a):
    if type(a) !=int:
        raise TypeError('Expected int')
    elif a<0:
        raise ValueError('Got negative int')