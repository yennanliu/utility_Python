class TicTacToe:

    def __init__(self):
        self.matrix = [ [None]*3 for _ in range(3) ]

    def check_x_axis(self):
        # x axis
        for i in range(len(self.matrix)):
            if (self.matrix[i].count("x") == 3 ):
                print (" {} win the game".format("x"))
                return True, "x"

            elif (self.matrix[i].count("y") == 3 ):
                print (" {} win the game".format("y"))
                return True, "y"

    def check_y_axis(self):
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

    def check_left_diagonal(self):
        # left diagonal  
        sum_of_left_d_X = sum([self.matrix[i][i] == "x" for i in range(len(self.matrix))])
        sum_of_left_d_y = sum([self.matrix[i][i] == "y" for i in range(len(self.matrix))])

        if sum_of_left_d_X == 3:
            return True, "x"
        elif sum_of_left_d_y == 3:
            return True, "y"

    def check_right_diagonal(self):
        # right diagonal
        sum_of_left_d_X = sum([self.matrix[i][len(self.matrix)-i-1] == "x" for i in range(len(self.matrix))])
        sum_of_left_d_y = sum([self.matrix[i][len(self.matrix)-i-1] == "y" for i in range(len(self.matrix))])

        if sum_of_left_d_X == 3:
            return True, "x"
        elif sum_of_left_d_y == 3:
            return True, "y"

    def check_win(self):
        if self.check_x_axis():
            return self.check_x_axis()

        elif self.check_y_axis():
            return self.check_y_axis()

        elif self.check_left_diagonal():
            return self.check_left_diagonal()

        elif self.check_right_diagonal():
            return self.check_right_diagonal()

        #elif self.check_occupied():
        #    return (False, "even")

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
            print (" {} win the game".format(result[1]))
            return "{} win!".format(result[1])
        else:
            return "even"
  
if __name__ == '__main__':
    t_game = TicTacToe()
    t_game.operate_game()