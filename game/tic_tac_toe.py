class TicTacToe:

    def __init__(self):
        self.matrix = [ [None]*3 for _ in range(3) ]

    def check_win(self):
        # x axis
        for i in range(len(self.matrix)):
            if (self.matrix[i].count("x") == 3 ):
                print (" {} win the game".format("x"))
                return True, "x"

            elif (self.matrix[i].count("y") == 3 ):
                print (" {} win the game".format("y"))
                return True, "y"

        # y axis
        for j in range(len(self.matrix[1])):
            count_x, count_y = 0, 0 
            for i_ in range(len(self.matrix)):
                if self.matrix[i_][j] == 'x':
                    count_x += 1 
                elif self.matrix[i_][j] == 'y':
                    count_y += 1 
                if count_x == 3:
                    return True, "x"
                elif count_y == 3:
                    return True, "y"

        # diagonal axis 
        # pass 

        #return False, "even"

    def check_occupied(self):
        for i in range(len(self.matrix)):
            if None in self.matrix[i]:
                return False
        return True

    def operate_game(self):
        # start from "x", then "o". so the process is : x -> o -> x....
        while ( not self.check_win()) and ( not self.check_occupied() ):

            input_x = input("plz input x : ")
            input_y = input("plz input y : ")
            x, y = int(input_x), int(input_y)

            print ("x, y = ", x, y) 
        
            round_ = 1 
            if x < 0 or x > 3 or y < 0 or y > 3:
                print ("out of range, plz select x, y again")

            if round_ % 2 == 1:
                icon = "x"
                round_ += 1 

            elif round_ % 2 == 1:
                icon = "o"
                round_ += 1 

            print ("player put {} at [{}, {}]".format(icon, x, y))
            self.matrix[x][y] = icon
            print ("current matrix :", self.matrix)
            print ("self.check_win() ", self.check_win())

        if self.check_win():
            result =  self.check_win()
            return "{} win!".format(result[1])
        else:
            return "even"

if __name__ == '__main__':
    t_game = TicTacToe()
    t_game.operate_game()