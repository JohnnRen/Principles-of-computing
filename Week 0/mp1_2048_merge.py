""" mp1_2048_merge """


def merge(line):
    """ Merge a line towards left side """
    for _ in range(line.count(0)):
        line.remove(0)
        line.append(0)
    for index in range(1, len(line)):
        if line[index] == line[i - 1]:
            line[index - 1] *= 2
            del line[index]
            line.append(0)
    return line


print merge([2, 0, 2, 4, 8])
