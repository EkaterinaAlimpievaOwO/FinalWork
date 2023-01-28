userList = []
print("Введите количество элементов массива: ")
elNum = int(input())

for i in range(elNum):
    print("Введите", i+1, "элемент массива:")
    userInput = input()
    userList.append(userInput)
print("Ваш массив: ","\n", userList)

newList = []
for i in range(len(userList)):
    if len(userList[i]) <= 3:
        newList.append(userList[i])
print("Массив элементов с длиной равной или меньшей, чем три символа: ", "\n", newList, sep=" ")