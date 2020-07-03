7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
        X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average
of those values and produce an output as shown below.
You can download the sample data at http://www.pythonlearn.com/code/mbox-short.txt when 
you are testing below enter mbox-short.txt as the file name.


# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count_line = 0
float_num = 0.0
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    float_num = float_num + float(line[20:])
    count_line = count_line + 1
average = float_num/count_line
print('Average spam confidence:',average)

