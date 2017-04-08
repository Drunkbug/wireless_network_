from random import randint
# generate access points for step 1
def init():
    L = []
    x, y = 0, 0
    for i in range(10):
        for j in range(10): 
            locationX = [randint(x, x + 200)]
            locationY = randint(y, y+200)
            locationX.append(locationY)
            L.append(locationX)
            y += 200
        x += 200
        y = 0
    print (L)
    print ("adding duplicates ... ")

    for i in range(len(L)):
        dupL = [randint(0, 2000), randint(0, 2000)]
        L.append(dupL)

    print (L)
    print ("=======================================")
    return L

# Heuristic H0
# start with empty L', if AP in L not covered in L'
def heuristic0():
    # clean file content
    # test for 10 times
    h0file = open("heuristic0.txt", "w+")
    h0file.close()
    for j in range(100):
        L = init()
        L_acc = []
        coveredX, coveredY = 0, 0
        for k in range(10):
            for i in range(len(L)):
                apX = L[i][0]
                apY = L[i][1]
                if (apX > coveredX) and ((apX - 200) <= coveredX) and (L[i] not in L_acc) and (coveredX < 2000) and (apY > coveredY) and (apY - 200 <= coveredY) and (coveredY < 2000):
                    coveredY = apY + 200
                    L_acc.append(L[i]) 
            coveredX += 200
            coveredY = 0
        print (L_acc)
        print ("writing to heuristic0.txt file ... ")
        h0file = open("heuristic0.txt", "a")
        h0file.write(str(j+1) + "\t" + str(len(L_acc)) + "\n")
        h0file.close()
        print ("done.")
    



# Heuristic H1
# sort the list
def heuristic1():
    # clean file content
    # test for 10 times
    h1file = open("heuristic1.txt", "w+")
    h1file.close()
    for j in range(100):
        L = sorted(init())
        L_acc = []
        coveredX, coveredY = 0, 0
        for k in range(10):
            for i in range(len(L)):
                apX = L[i][0]
                apY = L[i][1]
                if (apX > coveredX) and ((apX - 200) <= coveredX) and (L[i] not in L_acc) and (coveredX < 2000) and (apY > coveredY) and (apY - 200 <= coveredY) and (coveredY < 2000):
                    coveredY = apY + 200
                    L_acc.append(L[i]) 
                    #break
            coveredX += 200
            coveredY = 0
        print (L_acc)
        print ("writing to heuristic1.txt file ... ")
        h1file = open("heuristic1.txt", "a")
        h1file.write(str(j+1) + "\t" + str(len(L_acc)) + "\n")
        h1file.close()
        print ("done.")

# Heuristic H2
# use greedy algorithm to select the ap with least duplicate area
def heuristic2():
    # clean file content
    h2file = open("heuristic2.txt", "w+")
    h2file.close()
    # test for 10 times
    for j in range(100):
        L = sorted(init())
        L_acc = []
        coveredX, coveredY = 200, 200
        bestY = 0
        for k in range(10):
            for i in range(len(L)):
                apX = L[i][0]
                apY = L[i][1]
                if (apX < coveredX) and (apX + 200 >= coveredX) and (L[i] not in L_acc) and (coveredX < 2000) and (apY < coveredY) and (apY + 200 >=  coveredY) and (coveredY < 2000):
                    bestY = max(apY, bestY)
                    L_acc.append(L[i]) 
                coveredY = bestY + 200
            coveredX += 200
            coveredY = 200
        print (L_acc)
        print ("writing to heuristic2.txt file ... ")
        h2file = open("heuristic2.txt", "a")
        h2file.write(str(j+1) + "\t" + str(len(L_acc)) + "\n")
        h2file.close()
        print ("done")

heuristic0()
heuristic1()
heuristic2()




