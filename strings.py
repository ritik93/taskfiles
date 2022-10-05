def reverse_iterative(s):
    s1 = ""
    for i in s:
        s1 = i + s1
    return s1


def reverse_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursive(s[1:]) + s[0]
