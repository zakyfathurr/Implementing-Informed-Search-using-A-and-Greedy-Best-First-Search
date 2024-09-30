import heapq
graf = {}

class PriorityQueue:
    def __init__(self) -> None:
        self.cities = []

    def isEmpty(self):
        if self.cities == []:
            return True
        return False

    def check(self):
        print(self.cities)

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city))
    
    def pop(self):
        return heapq.heappop(self.cities)[1]
class CityNode:
  def __init__(self, city, distance) -> None:
    self.city = str(city)
    self.distance = str(distance)
def makeDict():
    file = open("Path.txt", 'r')
    for line in file:
        delimeter = line.strip().split(',')
        if len(delimeter) >= 3:  # Ensure there are at least 3 parts (city1, city2, distance)
            city1 = delimeter[0].strip()
            city2 = delimeter[1].strip()
            dist = delimeter[2].strip()
            graf.setdefault(city1, []).append(CityNode(city2, dist))
            graf.setdefault(city2, []).append(CityNode(city1, dist))
        else:
            print(f"Warning: Skipped invalid line - {line.strip()}")
    file.close()

        
def makeHeuristicDict():
    h = {}
    file = open("HeuristicSurabaya.txt", 'r')
    for str in file:
        delimeter = str.strip().split(',')
        node = delimeter[0].strip()
        sld  = int(delimeter[1].strip()) # Jalan lurus
        h[node] = sld
    return h

def heuristic(node, values):
    return values[node]
def aStar(start, end):
    path = {}
    distance = {}
    q = PriorityQueue()
    h = makeHeuristicDict()

    q.push(start, 0)
    distance[start] = 0
    path[start] = None
    expandList = []

    while q.isEmpty() == False:
        curr = q.pop()
        expandList.append(curr)

        if curr == end:
            break

        for new in graf[curr]:
            graph_cost = distance[curr] + int(new.distance)
            # print(new.city, new.distance, "now : " + str(distance[curr]), graph_cost)

            if new.city not in distance or graph_cost < distance[new.city]:
                distance[new.city] = graph_cost
                f_cost = graph_cost + heuristic(new.city, h)
                q.push(new.city, f_cost)
                path[new.city] = curr
    
    printOutput(start, end, path, distance, expandList)


def printOutput(start, end, path, distance, expandList):
    finalpath = []
    i = end

    while (path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()

    print("Membuat Program A* (A star) sederhana")
    print("\tBandung TO Surabaya")
    print("==============================================================================================================")
    print("Kota yg mungkin dijelajah \t\t: " + str(expandList))
    print("Jumlah kemungkinan kota \t\t: " + str(len(expandList)))
    print("==============================================================================================================")
    print("Kota yg dilewati dg jarak terpendek\t: " + str(finalpath))
    print("Jumlah kota yang dilewati \t\t: " + str(len(finalpath)))
    print("Total Jarak yang ditempuh \t\t: " + str(distance[end]))
    print("==============================================================================================================")
def main():
    src = "Bandung"
    dst = "Surabaya"
    makeDict()
    aStar(src, dst)

if __name__ == "__main__":
    main()