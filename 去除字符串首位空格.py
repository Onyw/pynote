def trim(s):
    if s=='':
        return s
    elif s[0]!=' 'and s[-1]!=' ':
        return s
    elif s[0]==' ' and s[-1]==' ':
        s=s[1:-1]
        if s=='':
            return s
        else:
            return trim(s)
    elif s[0] == ' ' and s[-1] != ' ':
        s=s[1:]
        return trim(s)
    elif s[0] != ' ' and s[-1] == ' ':
        s=s[:-1]
        return trim(s)
a=input()
print(trim(a))