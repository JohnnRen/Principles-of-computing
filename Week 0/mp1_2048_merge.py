""" mp1_2048_merge """


def merge(line):
    """ Merge a line towards left side """
    for i in range(line.count(0)):
        line.remove(0)
        line.append(0)
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            line[i - 1] *= 2
            del line[i]
            line.append(0)
            break
    return line


def merge2(line):
    """ Merge a line towards left side """
    is_merged = False
    for index, element in enumerate(line):
        if element == 0:
            del element
            line.append(0)
        elif index != len(line) - 1 and not is_merged:
            if line[index] == line[index + 1]:
                line[index] *= 2
                line[index + 1] = 0
                is_merged = True
    return line


print merge([8, 4, 4, 4])
