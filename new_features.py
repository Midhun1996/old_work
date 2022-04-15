from typing import Any

#pattern matching

# def http_error(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 401 | 403:
#             return "Not allowed"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"

# ans = http_error(404)

# print(ans)


def greet(name:str) -> Any:
    print(f"good morning, {name}")
    
    
greet("Midhun")