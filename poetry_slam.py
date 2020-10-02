# Function to get the lines from our text file
def get_file_lines(filename):
    file_line = open(filename, 'r').readlines()
    return file_line
