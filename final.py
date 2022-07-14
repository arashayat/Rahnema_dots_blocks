



class Player:
    wins = 0
    boxes = 0
    def __init__(self, id) -> None:
        self.id = id
    
    def addBox(self, m, k):
        self.boxes.append((m, k))

class Playground:
    
    boxes = 0
    def initialize(self, m, k) -> None:
        self.m = m
        self.k = k
        self.map_h = [[0]*(k) for _ in range(m+1) ]
        self.map_v = [[0]*(k+1) for _ in range(m) ]

    def isBoxFull(self, m, k):
        if self.map_h[m][k] and self.map_h[m+1][k] and self.map_v[m][m] and self.map_v[m][k+1]:
            return 1
        else:
            return 0
        
    def setLine(self, isHorizontal, m, k):
        if isHorizontal:
            self.map_h[m][k] = 1
        else:
            self.map_v[m][k] = 1
    
    def showMap(self):
        
        for i in range(2*self.m+1):
              
            if i%2 == 0:
                print("*", end="") 
                for j in range(self.k):
                    if self.map_h[int(i/2)][j]:
                        print("---", end="*")
                    else:
                        print("   ", end="*")
            else:
                for j in range(self.k+1):
                    if self.map_v[int((i-1)/2)][j]:
                        print("|", end="   ")
                    else:
                        print(" ", end="   ")
                print(' ', end="")
            print()





    def endGame(self):
        self.boxes = 0
        self.initialize(self.m, self.k)
        return True

    def move(self, person, isHorizontal, m, k):
        self.setLine(isHorizontal, m, k)
        cnt = 0

        if isHorizontal:
            if m == 0:
                cnt += self.isBoxFull(m, k)
            elif m == self.m:
                cnt += self.isBoxFull(m-1, k)
            else:
                cnt += self.isBoxFull(m, k)
                cnt += self.isBoxFull(m-1, k)
        else:
            if k == 0:
                cnt += self.isBoxFull(m, k)
            elif k == self.k:
                cnt += self.isBoxFull(m, k-1)
            else:
                cnt += self.isBoxFull(m, k)
                cnt += self.isBoxFull(m, k-1)
        self.boxes += cnt
        person.boxes += cnt

        self.showMap()

        if self.boxes >= self.m*self.k:
            return self.endGame()
        else:
            return False
    
    def calculateWinner(players):
        max = 0
        max_p = 0
        for i in players:
            if i.boxes > max:
                max = i.boxes
                max_p = i

            i.boxes = 0
        
        return max_p
            





line = input("Please enter variables: n m k\n").split()
line = list(map(int, line))

n = line[0]
m = line[1]
k = line[2]

players = []
playground = Playground()
playground.initialize(m, k)

for i in range(n):
    players.append(Player(i))

playground.showMap()

while(True):
    for i in range(n):
        print(f"player {i+1} go your move: horizontal m k")
        line = input().split()
        line = list(map(int, line))
        if playground.move(players[i], line[0], line[1], line[2]):
            winner = playground.calculateWinner(players)
            players[winner].wins+=1
            print("winner is number: ", winner+1)


