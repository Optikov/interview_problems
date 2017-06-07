def check(s):
    while s:
        s = s.replace("()", "")
        if s.find("()") == -1 and len(s) != 0:
            return "bad!"
    return "good!"

s = "((()()))"
print(check(s))

