class FunctionRegistry:
    def __init__(self):
        self.functions = {}

    def __iter__(self):
        return iter(self.functions.items())

    def register(self, function):
        name = function.__name__[9:]
        self.functions[name] = function
        return function

    def __call__(self, function):
        return self.register(function)


haystack_functions = FunctionRegistry()
