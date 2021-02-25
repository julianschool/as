# Problem 4, Not finished

n = int(input())
names = []
for i in range(0, n):
    names.append(str(input()).split(" "))

class Ballots:
    def __init__(self, array):
        self.arr = array
        # for i in range(len(array)):
        #     for j in range(len(array[i])):
    def display(self):
        print("President: " + "\nVice President: " + "\nSecretary: " + "\nTreasurer: " + "\nReporter: " + "\nSergeant-at-Arms: ")
        
a = Ballots(names)
a.display()
