
def decorator(function):
    def decorated(value):
        print("Decorated Function")
        function(value)
    
    return decorated

def test(value):
    print(value)



decorated = decorator(test)


decorated(6)