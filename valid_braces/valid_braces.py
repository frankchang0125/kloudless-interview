def solution(string):
    s = []

    for i in range(len(string)):
        c = string[i]

        if len(s) == 0:
            if c == ')' or c == '}' or c == ']':
                return False
            s.append(c)
        else:
            top = s[-1]
            if c == ')':
                if top != '(':
                    return False
                else:
                    del s[-1]
            elif c == '}':
                if top != '{':
                    return False
                else:
                    del s[-1]
            elif c == ']':
                if top != '[':
                    return False
                else:
                    del s[-1]
            else:
                s.append(c)

    if len(s) == 0:
        return True
    else:
        return False
