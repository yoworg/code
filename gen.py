list = [1,2,3,4,5]

def gen():
    for i in range(5,10):
        yield i



g = gen()

next(g)