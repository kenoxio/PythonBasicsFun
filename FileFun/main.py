# Files
# a file stores data on your file system
# "on disk"

# goal: read the contents of data.csv into
# our python program memory
# and store the contents in a 2D list

# 3 part file processing template
# 1. open the file
# 2. process the file (e. g. read or write)
# 3. close the file

# lets using functiosn for practice
def load_lines_from_file(filename):
    # filename is a string
    # representing a "path" to the file we want to open
    # 1. absolute path
    # starts with C:\ (drives) on windows or
    # / root on (mac/linux...)
    # example: /home/nhayes3/Documents/CPSC 222/ PythonBasicsFun/FileFun
    # # uniquely identifies files/folders 
    # 2. relative path
    # don't start with drive or root
    # they are relative to the current workign directory
    # check VS Code's cwd (current working directory) or terminal's cwd
    # example: FileFun/data.csv
    # 1.
    infile = open(filename, "r") # "r" is the file mode
    # 2.
    lines = infile.readlines()
    # 3.
    infile.close()
    return lines

def clean_lines(lines):
    for i in range(len(lines)):
        # lines[i] is a strong
        lines[i] = lines[i].strip() # remove leading/trailing whitespace

def restructure_data_into_table(lines):
    # lines is 1D
    table = [] # 2D
    for line in lines:
        #lines is a stringi n the CSV format
        # we are going to split line by ","
        values = line.split(",")
        # print(values)
        table.append(values)
    return table

def convert_column_to_numeric(table, col_index): 
    # convert all the values in the table at this column index
    # to a numeric type
    for row in table:
        row[col_index] = int(row[col_index])

file_lines = load_lines_from_file("data.csv") # relative path
print(file_lines)
# we need to remove the newlines (\n)
clean_lines(file_lines)
print(file_lines)
# we need to restructure our 1D list of strings into a 2D list of strings
table = restructure_data_into_table(file_lines)
print(table)
# last step.. we should convert numeric columns to a numeric type
# store the header separately from the data
header = table.pop(0)
print(header)
print(table)
convert_column_to_numeric(table, 1)
convert_column_to_numeric(table, 2)
print(table)
# TASK: define/call pretty_print(header, table)
# print out the column names and the data values in a nice grid like
# structure
