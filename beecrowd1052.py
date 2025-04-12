month = int(input())
monthsList = ['January','February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
for x in range(1,13):
    match month:
        case x:
            chosenMonth =(monthsList[x - 1])
print(chosenMonth)