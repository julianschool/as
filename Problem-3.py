#Problem 3 

inputValue = str(input())

if inputValue == 'volume':
    print('radius = ' + str(round(((3*float(input()))/(4*3.14159))**(1/3), 1)))
elif inputValue == 'radius':
    print('volume = ' + str(round((4/3)*3.14159*(float(input())**3), 1)))
