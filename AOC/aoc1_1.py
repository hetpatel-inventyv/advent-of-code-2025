def solver(input):
    zero_points = 0
    start = 50

    for rotation in input.splitlines():
        rotation = rotation.strip()
        if not rotation:
            continue
        
        amount = int(rotation[1:])
        
        if rotation.startswith("R"):
            start = (start + amount) % 100
        else:
            start = (start - amount) % 100

        if start == 0:
            zero_points += 1
    
    return zero_points

if __name__ == "__main__":
    with open("day1.txt", "r") as file:
        input = file.read()
    print(solver(input))
