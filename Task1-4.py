iplist = []
keylist = ['address', 'counter']
counter = 0
for line in open('/home/student/access.log.simulation'):
        ip = line.split(' ')[0]
        iplist.append(ip)
print(iplist)
uniques = [iplist[0]]
for i in iplist:
    if i not in uniques:
        uniques.append(i)
print(uniques)
counterlist = [0]*len(uniques)
fulllist = []
for j in range(len(uniques)):
    for i in iplist:
        if i == uniques[j]:
            counter += 1
    counterlist[j] = counter
    counter = 0
for x in range(len(uniques)):
    fulllist.append((uniques[x], counterlist[x]))
print(fulllist)