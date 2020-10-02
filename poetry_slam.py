import random
# Function to get the lines from our text file
def get_file_lines(filename):
    #open and reads the lines of the file we insert
    file_line = open(filename, 'r').readlines()
    return file_line
    file_line.close()
    
print(get_file_lines("/Users/Jordan/dev/Make School Courses/CS-1.0-Introduction-To-Programming/Assignments/Poetry Slam/poem.txt"))
# -----------------------------------------------------

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
poem = open('/Users/Jordan/dev/Make School Courses/CS-1.0-Introduction-To-Programming/Assignments/Poetry Slam/poem.txt', 'r')
#open, read, split the lines from the file, and closes the file we give 
lines_printed_backwards(poem.read().splitlines())
poem.close()

# -----------------------------------------------------

#Function to print the lines from our text file randomly
def lines_printed_random(lines_list):
    lines_list_length = len(lines_list)
    for i in range(lines_list_length):
        #loops for random line in the list 
        #then prints until the number of lines has been reached
        random_line = lines_list[random.randint(i, lines_list_length -1)]
        print(random_line)

#variable to open the file
poem = open('/Users/Jordan/dev/Make School Courses/CS-1.0-Introduction-To-Programming/Assignments/Poetry Slam/poem.txt', 'r')
#open, read, split the lines from the file, and closes the file we give 
lines_printed_random(poem.read().splitlines())
poem.close()
# -----------------------------------------------------

def lines_printed_custom(lines_list):
  i = 1
  second_lines = open(lines_list)
  for line in second_lines.readlines():
      if i % 2 == 0 :
          print(line)
      i += 1

print(lines_printed_custom('/Users/Jordan/dev/Make School Courses/CS-1.0-Introduction-To-Programming/Assignments/Poetry Slam/poem.txt'))
        
