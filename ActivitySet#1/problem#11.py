# Tuples

#filename = "dataset/mbox-short.txt"
name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if line.startswith('From'):
        words = line.split()
        if len(words) > 6:
            time = words[5].split(':')
            counts[time[0]] = counts.get(time[0], 0) + 1
lst = list()
for k,v in counts.items():
    lst.append((k,v))
lst = sorted(lst)
for k,v in lst:
    print(k,v)