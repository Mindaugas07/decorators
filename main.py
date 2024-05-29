# First-Class Functions


# def square(x):
#     return x * x


# f = square

# print(square)
# print(f(5))


# def square(x):
#     return x * x


# def cube(x):
#     return x**3


# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result


# squares = my_map(cube, [1, 2, 3, 4, 5])

# print(squares)


# def logger(msg):

#     def log_message():
#         print("Log:", msg)

#     return log_message


# log_hi = logger("Hi!")
# log_hi()


# def html_tag(tag):

#     def wrap_text(msg):
#         print(f"<{tag}>{msg}<{tag}>")

#     return wrap_text


# # print_h1 = html_tag("h1")
# # print_h1("Test Headline!")
# # print_h1("Another Headline!")

# # print_p = html_tag("p")
# # print_p("Test Paragraph!")
# html_tag("h2")("You can do this way also!")


# # Closures


# def outer_func(msg):
#     message = msg

#     def inner_func():
#         print(message)

#     return inner_func


# # my_func = outer_func()

# # print(my_func.__name__)


# hi_func = outer_func("Hi")
# hello_func = outer_func("Hello")

# hi_func()
# hello_func()
# outer_func("hi")()


# import logging

# logging.basicConfig(filename="example.log", level=logging.INFO)


# def logger(func):
#     def log_func(*args):
#         logging.info(f'Running "{func.__name__}" with arguments {args}')
#         print(func(*args))

#     return log_func


# def add(x, y):
#     return x + y


# def sub(x, y):
#     return x - y


# add_logger = logger(add)
# sub_logger = logger(sub)

# add_logger(3, 3)
# add_logger(4, 5)

# sub_logger(10, 5)
# sub_logger(20, 10)


# Decorators


from typing import Any


# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print(f"wrapper executed this before {original_function.__name__}")
#         return original_function(*args, **kwargs)

#     return wrapper_function


# class DecoratorClass(object):
#     def __init__(self, original_function):
#         self.original_function = original_function

#     def __call__(self, *args: Any, **kwargs: Any) -> Any:
#         print(f"call executed this before {self.original_function.__name__}")
#         return self.original_function(*args, **kwargs)


# @decorator_function
# def display():
#     print("display function ran")


# @decorator_function
# def display_info(name, age):
#     print(f"display_info ran with arguments {name} and {age}")


# display_info("Jogaila", 25)

# display()
# from functools import wraps


# def my_logger(orig_func):
#     import logging

#     logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)

#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         logging.info(f"Ran with args: {args}, and kwargs: {kwargs}")
#         return orig_func(*args, **kwargs)

#     return wrapper


# def my_timer(orig_func):
#     import time

#     @wraps(orig_func)
#     def wrapper(*args, **kwargs):
#         t1 = time.time()
#         result = orig_func(*args, **kwargs)
#         t2 = time.time() - t1
#         print(f"{orig_func.__name__} ran in {t2} sec")
#         return result

#     return wrapper


# # @decorator_function
# # def display():
# #     print("display function ran")

# import time


# @my_logger
# @my_timer
# def display_info(name, age):
#     time.sleep(1)
#     print(f"display_info ran with arguments {name} and {age}")


# # display_info = my_logger(my_timer(display_info))

# display_info("Tom", 36)


def prefix_decorator(prefix):
    def decorator_function(original_function):
        def wrapper_function(*args, **kwargs):
            print(prefix, "Executed before", original_function.__name__)
            result = original_function(*args, **kwargs)
            print(prefix, "Executed after", original_function.__name__, "\n")
            return result

        return wrapper_function

    return decorator_function


@prefix_decorator("WORK: ")
def display_info(name, age):

    print(f"display_info ran with arguments {name} and {age}")


display_info("Jogaila", 36)
display_info("Tom", 78)
