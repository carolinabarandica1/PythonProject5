#let's create a virtual diary

with open("diary.txt","w")as fp:
    while True:
        text = input("how do you feel today?(type q to quit):")
        if text == "q":
            break
        fp.write(f"{text}\n")
        fp.write(text+ "\n")

