def rev(s, i, j):
    if i >= j:
        return
    s[i], s[j] = s[j], s[i]
    return rev(s, i + 1, j - 1)

a = 'asdf'
s = list(a)
i = 0
j = len(s) - 1
rev(s, i, j)
print("".join(s))