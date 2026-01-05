def solver(input):
    zero_points = 0
    start = 50

    for rotation in input.split():
        amount = int(rotation[1:])
        direction = rotation[0] 
        
        if direction == "R":
            for i in range(amount):
                start = (start + 1) % 100
                if start == 0:
                    zero_points += 1
        elif direction == "L":
            for i in range(amount):
                start = (start - 1) % 100
                if start == 0:
                    zero_points += 1
    
    return zero_points

if __name__ == "__main__":
    with open("day1.txt", "r") as file:
        input = file.read()
    
    print(solver(input))
