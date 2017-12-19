def merge(line):  
    for i in range(line.count(0)):
        line.remove(0)
        line.append(0)
    for i in range(1,len(line)):
        if line[i]==line[i-1]:
            line[i-1]*=2
            del line[i]
            line.append(0)
            break
    return line

def merge2(line):
    is_merged=False
    for i in range(len(line)):
        if line[i]==0:
            del line[i]
            line.append(0)
        elif i!=len(line)-1 and not is_merged:
            if line[i]==line[i+1]:
                line[i]*=2
                line[i+1]=0
                is_merged=True
    return line
    
print merge([8,4,4,4]) 