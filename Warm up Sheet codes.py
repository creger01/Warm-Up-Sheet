#PT1
for item in range(3):

#PT2

total = 0
for letter in x:
    if letter == "o":
        total = total + 1

#PT3
if len(x) <= 140:
    print("text is okay")
else:
    print("text is too big")

#PT4
for element in ["fan", "fame", "foo", "figaro", "fig"]:
    print(element)
    if element  == "fig":
        print("there is fig in the basket")

#PT5
for element in range(len(word)):
    print(word[element])

#PT6
if len(word_1) == len(word_2):
    print("words have same length")

#PT7
for i in range(len(word)):
    print(word[i])

#PT8 - I DIDNT DO A FOR LOOP ... DO I NEED TO SINCE THE DIRECTION SAID "FOR ITEM IN [...], IF ITEM IS "EGG" REPLACE IT WITH "PEANUT BUTTER"
breakfast = ["egg","milk","bread","jam","butter", "apple","banana","kale"]
for item in breakfast:
    if item  == "egg":
        breakfast[0] = "peanut butter"

#PT9 - PRINTED HAMPSTER 4 TIMES, HOW DO I GET IT TO JUST ONCE?
my_list =  ["mouse", "rat", "squirrel","chipmunk"]
x = "hamster"
if x in my_list:
    print("hamster is in the list")
else:
    my_list.append("hamster")

#PT10
for ch in "happiness":
    print(ch)
    if ch == "p":
        print("found p")
