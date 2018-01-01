""" mp1_2048_merge """


def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # Collapse empty grid
    has_merged = False
    for _ in range(line.count(0)):
        line.remove(0)
        line.append(0)
    for index in range(1, len(line)):
        if line[index] == 0:
            break
        if line[index] == line[index - 1]:
            line[index - 1] *= 2
            has_merged = True
            del line[index]
            line.append(0)
    return line, has_merged


print merge([2, 0, 2, 2])
