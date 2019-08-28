def decorator(function):
    def decorated(value):
        print("Some Decorated Function")
        function(value)
    
    return decorated


@decorator
def test(value):
    print(value)


test(6)