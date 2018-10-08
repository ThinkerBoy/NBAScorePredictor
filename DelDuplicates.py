# Removes extra links from list

year = 2000

while year < 2019:
    # File containing possible duplicates
    file = open("..\DataSets\Regular Season Only\BoxScoreLinks\\" + str(year) + ".txt", "r")

    # New file to be written to
    writeTo = open("..\DataSets\Regular Season Only\BoxScoreLinks\\" + str(year) + "v2" + ".txt", "w")

    # Array to store non-duplicate values
    arr = []

    cont = False

    # Puts non duplicates into the arrays
    for i in file:
        cont = False
        for j in range(0, len(arr)):
            if(i == arr[len(arr) - 1 - j]):
                cont = True
                break
        if(cont):
            continue
        else:
            arr.append(i)

    # Writes non duplicates into new file
    for i in arr:
        writeTo.write(i)

    writeTo.close()
    file.close()
    year += 1
    
        
    
