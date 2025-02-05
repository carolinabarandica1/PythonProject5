fp=open('text.txt','r')
print(fp.read())
fp.close()

#SAME EXACT THING WITH CONTEXT MANAGER
with open("text.txt","r") as fp:
    print(fp.read())

#let's read from the same file line by line
print("read the file line by line")
line_number = 1
with open ("text.txt", "r") as fp:
    for line in fp:
        print(f"{line_number}. {line}", end="")
    line_number += 1

    print("done printing")


