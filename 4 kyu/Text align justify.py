def justify(text, width):
    text = text.split()
    list = []
    while len(text) > 0:
        number = 0
        matrix = ''
        while len(matrix) < width:
            matrix = ' '.join(text[a] for a in range(0, number + 1))
            if len(matrix) == width:
                list.append(matrix)
                text = text[number + 1:]
                break
            elif len(matrix) > width:
                list.append(' '.join(text[a] for a in range(0, number)))
                text = text[number:]
                break
            elif len(matrix) < width and text[-1] == text[number]:
                list.append(matrix)
                text = []
                break
            number += 1

    last = list[-1]
    list = list[:-1]
    for a in range(0, len(list)):
        spaces = [b for b, d in enumerate(list[a]) if d == ' ']
        while len(list[a]) < width:
            if spaces == []:
                break
            else:
                number = 0
                for c in spaces:
                    list[a] = list[a][:c + number] + ' ' + list[a][c + number:]
                    if len(list[a]) == width: break
                    number += 1
                spaces = [spaces[a] + a + 1 for a in range(0, len(spaces))]

    return '\n'.join(a for a in list) + '\n' + last


print(justify('Your task in this Kata is to emulate text justification in monospace font.', 15))