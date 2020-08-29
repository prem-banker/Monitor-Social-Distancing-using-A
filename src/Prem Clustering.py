import math

transformed_downoids = [[175.44165, 443.59726], [229.03697, 257.28705], [176.62459, 464.86932], [202.55417, 109.712585], [175.46881, 448.9137], [221.66188, 275.20853]]

#transformed_downoids = [[1,1] , [2,2] , [3,3], [5,5], [9,9], [15,15], [15,16]] 
distance_minimum = 110
height = 400
width = 500

def isneighbour(pair, distance_minimum):   # all the points less than threshold
    if math.sqrt( (pair[0][0] - pair[1][0])**2 + (pair[0][1] - pair[1][1])**2 ) < int(distance_minimum):
            # Change the colors of the points that are too close from each other to red
            if not (pair[0][0] > width or pair[0][0] < 0 or pair[0][1] > height+200  or pair[0][1] < 0 or pair[1][0] > width or pair[1][0] < 0 or pair[1][1] > height+200  or pair[1][1] < 0):
                    return True
    return False

def getneighbour(point, downdroids):   
    x = []
    for i in range(len(downdroids)):
            pair = [point, downdroids[i]]
            if point != downdroids[i] and isneighbour(pair, distance_minimum):
                    x.append(downdroids[i])
    return x


    
for i in range(6):
    print(getneighbour(transformed_downoids[i], transformed_downoids))


def formcluster(temp, pnt, visited, transformed_downoids):
    for x in range(len(transformed_downoids)):
        if transformed_downoids[x] == pnt:
            index = x
            break
    visited[index] = True
    temp.append(pnt)

    nbors = getneighbour(pnt, transformed_downoids)
    for n in nbors:
        for x in range(len(transformed_downoids)):
            if transformed_downoids[x] == n:  # index find kr raha hai
                index = x
                break
        if visited[index] == False:
            temp = formcluster(temp, n, visited, transformed_downoids)
    return temp


def getcluster(points):
    visited = {}
    cc = []
    for i in range(len(points)):
        visited[i] = False
    for v in range(len(points)):
        if visited[v] == False:
            temp = []
            cc.append(formcluster(temp, points[v], visited, points))
    return cc



def clusterindex(clusters, downoids):
    index = []
    for cls in clusters:
        x = []
        for pnt in cls:
            for i in range(len(downoids)):
                if downoids[i] == pnt:
                    x.append(i)
                    break
        index.append(x)
    return(index)


answer = getcluster(transformed_downoids)

indexes = clusterindex(answer, transformed_downoids)
print(' the clusters are : ')
for x in answer:
    print(x)
#print(formcluster([], transformed_downoids[0] ))

