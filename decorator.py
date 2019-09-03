
def pre_decorator(pre_arg):
    def hello_decorator(function):
        def decorated_function(*args, **kwargs):
            print(pre_arg)
            print("Decorated")
            function(*args, **kwargs)
        return decorated_function
    return hello_decorator


@pre_decorator("Final")
def hello(arg):
    print(arg)

#hello = hello_decorator(hello)

hello('test')


