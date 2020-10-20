# Prompts user
file_name = input("Enter the file name: ")

# Easter Egg
if file_name == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()

# Checks if file exists
try :
    open_file = open(file_name, 'r')
except :
    print("File does not exist.")
    quit()

# Counts lines
count = 0
for line in open_file :
    count += 1;
count = str(count)
print("There are " + count + " lines in the file.")
