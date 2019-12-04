def getInputs():
    #open file
    puzzle_input_file = open("input.txt", "r")
    inputs = []

    #load each line into array
    for line in puzzle_input_file.readlines():
        inputs.append(str(line))

    #close file, not neccesary when read only
    return inputs

def checkWordOcc(word, number):
    checked_chars = []
    index = 0
    
    for char in word:
        #skip already checked chars
        if char not in checked_chars:
            occurences = 0

            #count occurences of current char in the word
            for i in range(index, (len(word)-1)):
                if word[i] == char:
                    occurences += 1

            #if current word occurs the number of times
            if occurences == number:
                return 1
            index += 1

            #add to list of checked chars
            checked_chars.append(char)

    return 0

#returns strings where char at location is the same
def strMatch(str1, str2):
    out = ""
    for i in range(len(str1)):
        if(str1[i] == str2[i]):
            out += str1[i]
    return out

def getCommonID():

    boxes = getInputs()

    #compare each box with all the other boxes
    for i in range(len(boxes)):
        cur_box = boxes[i]

        #I heard you liked nestled loops
        for x in range(i+1, len(boxes) - 1):

            str_match = strMatch(cur_box, boxes[x])
            #check if the string of matching chars is one char shorter
            if (len(boxes[i]) - len(str_match)) == 1:
                return str_match


def getChecksum():
    twos = 0
    threes = 0

    #
    for word in getInputs():
        twos += checkWordOcc(word, 2)
        threes += checkWordOcc(word, 3)
    return twos * threes

if __name__ == '__main__':
    print("Anser part 1: " + str(getChecksum()))
    print("Anser part 2: " + str(getCommonID()))