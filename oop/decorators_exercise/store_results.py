class store_results:
    def __init__(self, func):
        self._func = func

    def __call__(self, *args):
        with open('results.txt', 'a') as file:
            file.write(f"Function '{self._func.__name__}' was called. Result: {self._func(*args)}\n")