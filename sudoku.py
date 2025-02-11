import sys

def i_and_j_zero(sudoku_list, possibilty_list, i, j):
    # Check and add numbers in the 3x3 grid
    if sudoku_list[i + 1][j + 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 1][j + 1])
    
    if sudoku_list[i + 1][j + 2] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 1][j + 2])

    if sudoku_list[i + 2][j + 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 2][j + 1])

    if sudoku_list[i + 2][j + 2] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 2][j + 2])

def i_zero_j_one(sudoku_list, possibilty_list, i, j):
    # Check and add numbers in the 3x3 grid
    if sudoku_list[i + 1][j - 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 1][j - 1])
    
    if sudoku_list[i + 2][j - 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 2][j - 1])

    if sudoku_list[i + 1][j + 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 1][j + 1])

    if sudoku_list[i + 2][j + 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 2][j + 1])

def i_zero_j_two(sudoku_list, possibilty_list, i, j):
    # Check and add numbers in the 3x3 grid
    if sudoku_list[i + 1][j - 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 1][j - 1])
    
    if sudoku_list[i + 1][j - 2] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 1][j - 2])

    if sudoku_list[i + 2][j - 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 2][j - 1])

    if sudoku_list[i + 2][j - 2] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 2][j - 2])

def i_one_j_zero(sudoku_list, possibilty_list, i, j):
    # Check and add numbers in the 3x3 grid
    if sudoku_list[i - 1][j + 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 1][j + 1])
    
    if sudoku_list[i - 1][j + 2] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 1][j + 2])

    if sudoku_list[i + 1][j + 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 1][j + 1])

    if sudoku_list[i + 1][j + 2] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 1][j + 2])

def i_and_j_one(sudoku_list, possibilty_list, i, j):
    # Check and add numbers in the 3x3 grid
    if sudoku_list[i - 1][j - 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 1][j - 1])
    
    if sudoku_list[i - 1][j + 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 1][j + 1])

    if sudoku_list[i + 1][j + 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 1][j + 1])

    if sudoku_list[i + 1][j - 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 1][j - 1])

def i_one_j_two(sudoku_list, possibilty_list, i, j):
    # Check and add numbers in the 3x3 grid
    if sudoku_list[i - 1][j - 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 1][j - 1])
    
    if sudoku_list[i - 1][j - 2] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 1][j - 2])

    if sudoku_list[i + 1][j - 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 1][j - 1])

    if sudoku_list[i + 1][j - 2] not in possibilty_list:
        possibilty_list.append(sudoku_list[i + 1][j - 2])

def i_two_j_zero(sudoku_list, possibilty_list, i, j):
    # Check and add numbers in the 3x3 grid
    if sudoku_list[i - 1][j + 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 1][j + 1])
    
    if sudoku_list[i - 1][j + 2] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 1][j + 2])

    if sudoku_list[i - 2][j + 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 2][j + 1])

    if sudoku_list[i - 2][j + 2] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 2][j + 2])
    
def i_two_j_one(sudoku_list, possibilty_list, i, j):
    # Check and add numbers in the 3x3 grid
    if sudoku_list[i - 1][j + 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 1][j + 1])
    
    if sudoku_list[i - 1][j - 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 1][j - 1])

    if sudoku_list[i - 2][j + 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 2][j + 1])

    if sudoku_list[i - 2][j - 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 2][j - 1])

def i_two_j_two(sudoku_list, possibilty_list, i, j):
    # Check and add numbers in the 3x3 grid
    if sudoku_list[i - 1][j - 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 1][j - 1])
    
    if sudoku_list[i - 1][j - 2] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 1][j - 2])

    if sudoku_list[i - 2][j - 1] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 2][j - 1])

    if sudoku_list[i - 2][j - 2] not in possibilty_list:
        possibilty_list.append(sudoku_list[i - 2][j - 2])

def looking_row(sudoku_list, possibilty_list, i, j):
    # Check and add numbers in the same row
    temp = 0
    while temp < 9:
        if sudoku_list[i][temp] not in possibilty_list:
            possibilty_list.append(sudoku_list[i][temp])
        temp += 1

def looking_column(sudoku_list, possibilty_list, i, j):
    # Check and add numbers in the same column
    temp = 0
    while temp < 9:
        if sudoku_list[temp][j] not in possibilty_list:
            possibilty_list.append(sudoku_list[temp][j])
        temp += 1
    
def one_possibility(sudoku_list, possibilty_list, i, j, buldum, total, step, output_file):
    #check the possibilty and add it 
    step += 1

    for val in range(1, 10):
        if val not in possibilty_list:
            sudoku_list[i][j] = val
            total += val
            break
    # write to output file
    output_file.write('------------------\n')
    output_file.write(f'Step {step} - {val} @ R{i + 1}C{j + 1}\n')
    output_file.write('------------------\n')
    # write the list line by line
    for i in range(9):
        for j in range(9):
            output_file.write(str(sudoku_list[i][j]) + " ")
        output_file.write("\n")
        
    i = 0
    j = 0
    buldum = True
    return [total, step]

def addition(sudoku_list, total):
    # find the sum of list to check if the sudoku is solved or not
    for u in sudoku_list:
        total += sum(u)
    return total

def solve(sudoku_list, i, j, total, step, output_file):
    # solve suduko,
    while  total < 405:
        buldum = False
        
        while not buldum  and total < 405:
            #  when the code encounter with zero:
            if sudoku_list[i][j] == 0:
                #calculate each possible values
                possibilty_list = []

                looking_row(sudoku_list, possibilty_list, i, j)

                looking_column(sudoku_list, possibilty_list, i, j)
                
                if i % 3 == 0 and j % 3 == 0:
                    i_and_j_zero(sudoku_list, possibilty_list, i, j)
                
                elif i % 3 == 0 and j % 3 == 1:
                    i_zero_j_one(sudoku_list, possibilty_list, i, j)
                
                elif i % 3 == 0 and j % 3 == 2:
                    i_zero_j_two(sudoku_list, possibilty_list, i, j)
                    
                elif i % 3 == 1 and j % 3 == 0:
                    i_one_j_zero(sudoku_list, possibilty_list, i, j)
                
                elif i % 3 == 1 and j % 3 == 1:
                    i_and_j_one(sudoku_list, possibilty_list, i, j)

                elif i % 3 == 1 and j % 3 == 2:
                    i_one_j_two(sudoku_list, possibilty_list, i, j)
                    
                elif i % 3 == 2 and j % 3 == 0:
                    i_two_j_zero(sudoku_list, possibilty_list, i, j)

                elif i % 3 == 2 and j % 3 == 1:
                    i_two_j_one(sudoku_list, possibilty_list, i, j)
                
                elif i % 3 == 2 and j % 3 == 2:
                    i_two_j_two(sudoku_list, possibilty_list, i, j)
                # if possibilty list's length is equal to 9, it means the code encountered with 9 numbers and there is just one number
                if len(possibilty_list) == 9:
                    a = one_possibility(sudoku_list, possibilty_list, i, j, buldum, total, step, output_file)
                    total = a[0]
                    step = a[1]
                    i = 0
                    j = 0
                # go to one column right
                elif j != 8:
                    j += 1
                #it means we checked each item in the row go to new row
                else:
                    i += 1
                    j = 0

            elif j != 8:
                    j += 1
            else:
                i += 1
                j = 0


def main():
    #read input file, and open output file for result
    input_file = open(sys.argv[1], "r")
    output_file = open(sys.argv[2], "w")
    #global variables
    i = 0
    j = 0
    step = 0
    total = 0
    sudoku_list = []
    #sudoku List
    sudoku_list = input_file.readlines()
    sudoku_list = [list(map(int, line.strip().replace(" ", ""))) for line in sudoku_list if line.strip()]
    #evaluate sum of list
    total = addition(sudoku_list, total)
    solve(sudoku_list, i, j, total, step, output_file)

    # I didn't add new line at the end of the - because when I add this, ıt add new empty line to file ! 
    output_file.write("------------------")
    input_file.close()
    output_file.flush()
    output_file.close()

if __name__ == "__main__":
    main()