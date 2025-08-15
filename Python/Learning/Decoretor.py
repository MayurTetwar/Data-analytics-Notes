import time

def timer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(f'{func.__name__} ran in {end-start} time')
        return result

    return wrapper

@timer                  # when we call exapmle then it call first to timer in which example function is pass
def example(n):
    time.sleep(n)

# example(2)


# the argument decoretor
def debug(func):
    def warpper(*args,**kwargs):
        args_value=' ,'.join(str(arg) for arg in args)
        kwargs_value=' ,'.join(f'{key}={value}' for key,value in kwargs.items())
        print(f'{func.__name__} {args_value} {kwargs_value}')
        return func(*args,**kwargs)
    return warpper

@debug
def greet(name,greeing="Hello"):
    print(f'{greeing}, {name}')

# greet("Mayur",greeing="Hii")





def cache(func):
    cache_value={}
    def warpper(*args):
        if(args in cache_value):
            return cache_value[args]
        result= func(*args)
        cache_value[args]=result
        return result
    return warpper 

@cache
def long_run_func(a,b):
    time.sleep(4)
    return a+b

print(long_run_func(2,3))
print(long_run_func(2,3))