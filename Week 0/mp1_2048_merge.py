""" mp1_2048_merge """


def merge(line):
    """ Merge a line towards left side """
    for _ in range(line.count(0)):
        line.remove(0)
        line.append(0)
    for i in range(1, len(line)):
        if line[i] == line[i - 1]:
            line[i - 1] *= 2
            del line[i]
            line.append(0)
    return line


print merge([2, 0, 2, 4, 8])
