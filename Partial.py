from functools import partial
# create a new function that multiplies by 2
def multiply(a,b):
    return a*b

dbl = partial(multiply,2)
print dbl(4)

#Following is the exercise, function provided:
def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function

dl = partial(func,5,6,7)  # this means that u=5, v=6, w=7
print dl(8)        # this means x = 8