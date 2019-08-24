def decorator(function):
    def decorated(value):
        print("That Decorated Function")
        function(value)
    
    return decorated


@decorator
def test(value):
    print(value)


test(6)