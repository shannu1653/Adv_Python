from functools import lru_cache
import time
from functools import wraps

# Python Decorators Guide - From Basic to Advanced

# 1. Basic Function Decorator
def simple_decorator(func):
    def wrapper():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

# 2. Decorator with Parameters
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Hello {name}")

# 3. Class Decorator
class Timer:
    def __init__(self, func):
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print(f"Function {self.func.__name__} called {self.calls} times")
        return self.func(*args, **kwargs)

@Timer
def compute_something(x):
    return x * 2

# 4. Method Decorator (for class methods)
def validate_input(func):
    def wrapper(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Input must be numeric")
        return func(self, value)
    return wrapper

class Calculator:
    @validate_input
    def square(self, number):
        return number ** 2

# 5. Real-life Examples

# 5.1 Caching Decorator

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 5.2 Authentication Decorator
def require_auth(func):
    def wrapper(*args, **kwargs):
        # Simulate authentication
        is_authenticated = True  # In real case, check user session/token
        if is_authenticated:
            return func(*args, **kwargs)
        else:
            raise PermissionError("Authentication required")
    return wrapper

@require_auth
def sensitive_operation():
    print("Performing sensitive operation")

# 5.3 Rate Limiting Decorator

def rate_limit(calls_limit, time_limit):
    def decorator(func):
        calls = []
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            calls_in_window = [call for call in calls if call > now - time_limit]
            if len(calls_in_window) >= calls_limit:
                raise Exception("Rate limit exceeded")
            calls.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(calls_limit=3, time_limit=60)
def api_call():
    print("API called")

# 6. Advanced Concepts

# 6.1 Decorator with State
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Call {wrapper.calls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

# 6.2 Decorator Chaining
@simple_decorator
@count_calls
def combined_decorated():
    print("Function with multiple decorators")

# Usage Examples
if __name__ == "__main__":
    # Basic decorator
    say_hello()
    
    # Decorator with parameters
    greet("Alice")
    
    # Class decorator
    result = compute_something(5)
    
    # Method decorator
    calc = Calculator()
    print(calc.square(4))
    
    # Caching decorator
    print(fibonacci(10))
    
    # Rate limiting
    try:
        for _ in range(4):
            api_call()
    except Exception as e:
        print(f"Rate limit error: {e}")