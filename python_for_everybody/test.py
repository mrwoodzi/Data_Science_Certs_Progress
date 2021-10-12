dhand = open('mbox.txt')
for line in dhand:
    line = line.rstrip()
    if not 'But' in line:
        continue
    print(line)