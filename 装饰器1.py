# import logging
#
#
# def use_logging(func):
#     def wrapper(*args,**kwargs):
#         logging.warn("%s is running"% func.__name__)
#         return func(*args,**kwargs)
#     return wrapper
#
# @use_logging
# def bar():
#     print('i am bar')
#
# @use_logging
# def foo():
#     print('i am foo')
#
#
# foo()
# bar()
#
#
# # 装饰器就是一个'平常不过'的函数
# def my_decorator(func):
#     print("I am an ordinary function")
#     def wrapper():
#         print("I am function returned by the decorator")
#         func()
#     return wrapper
#
# # 因此你可以不用"@"也可以调用他
# @my_decorator
# def lazy_function():
#     print("zzzzzzzz")
#
# lazy_function()

# def decorator_maker():
#
#     print("I make decorators! I am executed only once: "+\
#           "when you make me create a decorator.")
#
#     def my_decorator(func):
#
#         print("I am a decorator! I am executed only when you decorate a function.")
#
#         def wrapped():
#             print("I am the wrapper around the decorated function. "
#                   "I am called when you call the decorated function. "
#                   "As the wrapper, I return the RESULT of the decorated function.")
#             return func()
#
#         print("As the decorator, I return the wrapped function.")
#
#         return wrapped
#
#     print("As a decorator maker, I return a decorator")
#     return my_decorator
#
# @decorator_maker()
# def decorated_function():
#     print("I am the decorated function.")
#
#
# decorated_function()
def dec(f):
    n = 3
    def wrapper(*args,**kw):
        return f(*args,**kw) * n
    return wrapper

@dec
def foo(n):
    return n * 2

print(foo(2))