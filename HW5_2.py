names = ["Ryley", "Edan", "Reagan", "Henry", "Caius", "Jane", "Guto","Sonya", "Tyrese", "johnny"]
print("input a positive or negative number: ")
index = int(input())

try:
    print("Name: {}".format(names[index]))
except IndexError as excpt:
    print("Exception! {}".format(excpt))
    if index < 0:
        print("the closest name is: {}".format(names[0]))
    else:
        print("the closest name is: {}".format(names[9]))
