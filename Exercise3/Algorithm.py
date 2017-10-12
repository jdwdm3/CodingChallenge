################################################################inp##########
##                                                                      ##
##          Jeremy Warden -- Gateway Blend Coding Challenge             ##
##                                                                      ##
##########################################################################

####### Import Section #######
import sys
import itertools
##############################

def worker(word):

    #Retrieve our list 
    perm = itertools.permutations(word)
    
    return_list = []

    #Combine our tuple's into a single word and add it to a list (easier to manage)
    for word in perm:
        return_list.append(''.join(word))

    #sort our list based on following criteria
    return_list.sort()

    return return_list

def readFile(file):

    #Open the file in read only mode
    try:
        file_object  = open(file,"r")
    except FileNotFoundError:
        print("File " + file + "Does not exist, or at very least does not exist in the directory you are running this script from")

    #Loop through the file:
        #For each line, make sure there is only one word
            #for each word, make sure it contains no special characters
    #Add each word to a list

    #list data structure
    word_list = []

    #Count the lines in the file for User purposes
    line_number = 0
    
    for line in file_object.readlines():

        #Make sure there is just one word
        if(len(line.split()) > 1):

            print("Line number: " + str(line_number) + " is invalid, must contain only one word: " + line)

            line_number = line_number + 1

        #Line has only one word, check to make sure it doesn't contain any special characters
        else:

            #Error flag for invalid character
            error_flag = False
            
            for letter in line:
                if(letter.isdigit() == False and letter.isalpha() == False and letter != "\n"):

                    #Error Message
                    print("Line number: " + str(line_number) + " contains a special character: " + line)

                    #Increment Line number we are on
                    line_number = line_number + 1

                    #Set error flag to true
                    error_flag = True

            #Error flag is false, we have a single word with no special characters
            if(error_flag == False):

                    #increment line number 
                    line_number = line_number + 1

                    #remove new line character and add the word to our list
                    word_list.append(line.rstrip())

    print(word_list)
    print("Total lines read in our file: " + str(line_number))

    return word_list

def main():

    #Ensure the Program is run with the correct command line use
    if(len(sys.argv) != 2):
        print("Invalid use of program.\nCorrect use -- Algorithm <input_file>")
        return

    #Read in each line from our input file into a list
    word_list = readFile(sys.argv[1])


    print("\nFINAL PRODUCT\n")
    #Pass each word to our worker function, worker returns a complete list representing all the permutations in alphabetical order
    for word in word_list:
        print(",".join(worker(word)))



#########
main()
