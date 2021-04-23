#input example --->>>>  5 7 9 13 12 10 1 7
#output ----->>>> A 5 7 7 9 10 Q K
#----------------------------------
x = input("Enter number : ")
inputx = x.split(" ")

container = []
for i in inputx:
    if i == "A":
        container.insert(0,1)
    elif i == "J":
        container.insert(0,11)
    elif i == "Q":
        container.insert(0,12)
    elif i == "K":
        container.insert(0,13)
    else:
        container.insert(0,int(i))

container.sort()

container_new = list(map(str, container))

for k,j  in enumerate(container_new):

    if j == "1":
        container_new[k] = "A"
    elif j == "11":
        container_new[k] = "J"
    elif j == "12":
        container_new[k] = "Q"
    elif j == "13":
        container_new[k] = "K"

def ListToString(s):

    str1 = " "

    return (str1.join(s))

print(ListToString(container_new))

