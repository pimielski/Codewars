def operators(list):
    list.reverse()
    while '^' in list:
        list.insert(list.index('^') -1, list.pop(list.index('^') + 1))
        list[list.index('^') - 2: list.index('^') + 1] = [''.join(list[list.index('^') - 2: list.index('^') + 1])]
    list.reverse()

    while '*' in list or '/' in list:
        for x in list:
            if x == '*':
                list.insert(list.index('*') + 1, list.pop(list.index('*')))
                list[list.index('*') - 2: list.index('*') + 1] = [''.join(list[list.index('*') - 2: list.index('*') + 1])]
                break
            if x == '/':
                list.insert(list.index('/') + 1, list.pop(list.index('/')))
                list[list.index('/') - 2: list.index('/') + 1] = [''.join(list[list.index('/') - 2: list.index('/') + 1])]
                break

    while '+' in list or '-' in list:
        for x in list:
            if x == '+':
                list.insert(list.index('+') + 1, list.pop(list.index('+')))
                list[list.index('+') - 2: list.index('+') + 1] = [''.join(list[list.index('+') - 2: list.index('+') + 1])]
                break
            if x == '-':
                list.insert(list.index('-') + 1, list.pop(list.index('-')))
                list[list.index('-') - 2: list.index('-') + 1] = [''.join(list[list.index('-') - 2: list.index('-') + 1])]
                break
    return list


def to_postfix(infix):
    list = ''
    for x in infix:
        if x == '(': list += '( '
        elif x == ')': list +=' )'
        elif x in '+-/*^': list += ' ' + x + ' '
        else: list += x
    list = list.split()

    while '(' in list:
        matrix = ''
        matrix2 = []
        for x in range(len(list)):
            if list[x] in '()':
                matrix += list[x]
                matrix2.append(x)
                if matrix == '()':
                    list[matrix2[0] + 1: matrix2[1]] = operators(list[matrix2[0] + 1: matrix2[1]])
                    list.pop(matrix2[0])
                    list.pop(matrix2[0] + 1)
                    break
                if len(matrix) == 2:
                    matrix = matrix[1]
                    matrix2 = [matrix2[1]]

    list = operators(list)

    return ''.join(x for x in list)

print(to_postfix("5+(6-2)*9+3^(7-1)"))