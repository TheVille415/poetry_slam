# Function to get the lines from our text file
def get_file_lines(filename):
    #open and reads the lines of the file we insert
    file_line = open(filename, 'r').readlines()
    return file_line
    file_line.close()
    
print(get_file_lines("poem.txt"))

# Function to print the lines from our text file backwards
def lines_printed_backwards(lines_list):
    #takes the file and flips whats inside
    lines_list = lines_list[::-1]
    line_number = len(lines_list)

    for i in range(line_number):
        #made a variable to count down from the highest until its over 
        # and prints the lines in the order from line_list 
        reverse = str(line_number - i) + " " + lines_list[i]
        print(reverse)
#variable to open the file
poem = open('poem.txt', 'r')
#open, read, split, and closes the file we give 
lines_printed_backwards(poem.read().splitlines())
poem.close()

