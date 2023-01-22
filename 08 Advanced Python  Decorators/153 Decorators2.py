# Decorator supercharges our functions
    
def my_decorator(func):
    def wrap_func():
        print('*****')
        func()
        print('*****')
    return wrap_func

@my_decorator
def hello():
    print('hellooo')
    
hello()
