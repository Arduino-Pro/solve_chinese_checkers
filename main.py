

while True:
    dots = 0
    row_number = int(input("Enter the number of rows for the starting pen (even numbers only): "))
    if row_number % 2 != 0:
        print("Please enter an even number.")
        continue
    total_dots_in_pen = row_number*(row_number+1)/2
    total_dots_all_pens = total_dots_in_pen*6
    print(f"Total dots in pen: {total_dots_in_pen}")
    print(f"Total dots in all pens: {total_dots_all_pens}")
    for i in range(row_number+1):
        
        dots += row_number+1 + i
    dots = (2*dots) - (row_number+row_number+1)
    print(f"Total dots in hexagon: {dots}")
    print(f"Total dots: {dots + total_dots_all_pens}")