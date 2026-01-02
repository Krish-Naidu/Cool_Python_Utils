import re

def is_valid_email(email):
    pattern = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    if email == pattern:
        return "correct"
    else:
        return "wrong"

print(is_valid_email("krish.28.naidu@gmail.com"))
