9.4 Write a program to read through the mbox-short.txt and
figure out who has the sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those
lines as the person who sent the mail. The program creates a Python dictionary
that maps the sender's mail address to a count of the number of times they appear in
the file. After the dictionary is produced,
the program reads through the dictionary using a maximum loop to find the most prolific committer.



name = input("Enter file:")
if len(name) < 1 :
    name = "mbox-short.txt"
handle = open(name)
log = {}
for line in handle:
    temp = line.split()
    if 'From' in temp and len(line.split()) > 2:
        log[temp[1]] = log.get(temp[1],0)+1
largest = None
largest_author = None

for key in log:
    if largest is None:
        largest = log[key]

    if largest < log[key]:
        largest = log[key]
        largest_author = key

print(largest_author, largest)
        

