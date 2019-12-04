

def get_inputs():
    #open file
    puzzle_input_file = open("input.txt", "r")
    inputs = []

    #load each line into array
    for line in puzzle_input_file.readlines():
        inputs.append(int(line))

    #close file, not neccesary when read only
    return inputs

def chronal_calibration(starting_sum):
    
    sum = starting_sum
    #add each change to sum
    for x in get_inputs():
        sum = sum + x
    
    return sum

#this solution has horrible time complexity
#takes a couple of minutes to reach answer
def chronal_calibration_repetition():

    inputs = get_inputs()
    out = 0
    sum = 0
    
    #collection of sums already visited
    sum_collection = [sum]
    
    run = True
    while(run):
        for x in inputs:
            sum = sum + x
            if sum in sum_collection and run:
                out = sum
                run = False
                break
            else:
                sum_collection.append(sum)
    return out
    

if __name__ == '__main__':
    print("Result part 1: " + str(chronal_calibration(0)))
    print("Result part 2:  " + str(chronal_calibration_repetition()))