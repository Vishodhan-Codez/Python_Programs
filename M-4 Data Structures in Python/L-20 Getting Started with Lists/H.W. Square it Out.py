def square_and_separate(start, end):
    squares = []
    for x in range(start, end + 1):
        squares.append(x**2)
    os = []
    es = []
    for x in squares:
        if x % 2 == 0:
            es.append(x) #even
        else:
            os.append(x) #odd
    print("Odd Squares:", os) 
    print("Even Squares:", es)

sr = int(input("Enter the start of the range: "))
er = int(input("Enter the end of the range: "))
square_and_separate(sr, er)

