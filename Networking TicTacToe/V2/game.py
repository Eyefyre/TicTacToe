class Game:
    def __init__(self,id):
        self.WhoseTurn = 1
        self.Winner = 0
        self.board = [[0 for i in range(3)] for j in range(3)]
        self.id = id
        self.ready = False
        self.players = 0

    def updateTurn(self, turn):
        pass

    def updateBoard(self, x,y,v):
        self.board[x][y] = v

    def updateWinner(self, Winner):
        pass

    def update(self, i,j):
        self.board[i][j] = self.WhoseTurn
        self.WhoseTurn = self.WhoseTurn * -1
        self.Winner = self.checkWinCondition()


    def checkWinCondition(self):
        DiagSum = 0
        for x in range(3):
            sum = 0
            for y in range(3):
                sum += self.board[x][y]
                if(sum == 3):
                    return 1
                if(sum == -3):
                    return -1
        for x in range(3):
            sum = 0
            for y in range(3):
                sum += self.board[y][x]
                if(sum == 3):
                    return 1
                if(sum == -3):
                    return -1
        for x in range(3):
            for y in range(3):
                if x == y:
                    DiagSum += self.board[x][y]
                if(DiagSum == 3):
                    return 1
                if(DiagSum == -3):
                    return -1
        DiagSum = 0
        for x in range(3):
            for y in range(3):
                if x + y == 2:
                    DiagSum += self.board[x][y]
                if(DiagSum == 3):
                    return 1
                if(DiagSum == -3):
                    return -1
        Draw = True
        for x in range(3):
            for y in range(3):
                if(self.board[x][y] == 0):
                    Draw = False
        if(Draw):
            return 2
        return 0

    def resetGame(self):
        self.board = [[0 for i in range(3)] for j in range(3)]
        self.Winner = 0
        self.WhoseTurn = 1

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)