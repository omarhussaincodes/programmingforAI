filedata = open('pairing.txt', "r")
print(type(filedata))

data = []

for line in filedata:
    data.append(line.strip())
print(data)

result = []

for i in range(1, len(data) - 1, 2):
    if ((i+1) == len(data) - 1):
        result.append(tuple((data[i-1], data[i], data[i+1])))
    else:
        result.append(tuple((data[i-1], data[i])))

print(result)
