file = open("day2.txt", "r")
data = file.read()
file.close()

groups = data.split(",")
total = 0

for group in groups:
    parts = group.split("-")
    start = int(parts[0])
    end = int(parts[1])

    for num in range(start, end + 1):
        s = str(num)
        length = len(s)

        if length % 2 != 0:
            continue

        half = length // 2
        first = s[0:half]
        second = s[half:length]

        if first == second:
            total = total + num

print(total)
