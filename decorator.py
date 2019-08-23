def hello_decorator(function):
    def decorated_function(arg):
        print("Decorated")
        function(arg)
    return decorated_function


@hello_decorator
def hello(arg):
    print(arg)

#hello = hello_decorator(hello)

hello('test')
