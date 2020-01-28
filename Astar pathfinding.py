# g cost - distance from node to starting node
# h cost - distance from node to end node
# f cost - sum of g and h

#NO DIAGONAL IN THIS FUNCTION

#Finds distance between two points (manhattan distance)
def distance(x1,y1,x2,y2):
    return abs(x1 - x2) + abs(y2-y1)


class node:
    def __init__(self,g,h,direction):
        self.g = g
        self.h = h
        self.f = g+h
        self.direction = direction
        self.explored = False




class mapi:
    def __init__(self,a,b,map_data):
        #a is start node, b is end node
        self.ax = a[0]
        self.ay = a[1]
        self.bx = b[0]
        self.by = b[1]
        
        self.found = False

        self.map_data = map_data
        self.height = len(map_data)
        self.width = len(map_data[0])
        
        self.branch(self.ax,self.ay)
        
    def branch(self,x,y):
        #Up
        if y != 0:
            if self.map_data[y-1][x] == 0:
                self.map_data[y-1][x] = node(distance(x, y, self.ax, self.ay), distance(x, y, self.bx, self.by) , "d")
        #Down
        if y != self.height - 1:
            if self.map_data[y+1][x] == 0:
                self.map_data[y+1][x] = node(distance(x, y, self.ax, self.ay), distance(x, y, self.bx, self.by) , "u")
        #Left
        if x != 0:
            if self.map_data[y][x-1] == 0:
                self.map_data[y][x-1] = node(distance(x, y, self.ax, self.ay), distance(x, y, self.bx, self.by) , "r")
        #Right
        if x != self.width - 1:
            if self.map_data[y][x+1] == 0:
                self.map_data[y][x+1] = node(distance(x, y, self.ax, self.ay), distance(x, y, self.bx, self.by) , "l")

    def check(self):
        for i in range(self.height):
            for i2 in range(self.width):
                if isinstance(self.map_data[i][i2],node):
                    if i == self.by and i2 == self.bx:
                        self.found = True

    def iterate(self):
        lowest_f = 99999999999999
        lowest_f_cord = [0,0]
        for i in range(self.height):
            for i2 in range(self.width):
                if isinstance(self.map_data[i][i2],node):
                    if self.map_data[i][i2].explored:
                        pass
                    else:
                        if self.map_data[i][i2].f < lowest_f:
                            lowest_f = self.map_data[i][i2].f
                            lowest_f_cord = [i2,i]
                        elif self.map_data[i][i2].f == lowest_f:
                            if self.map_data[i][i2].h < self.map_data[lowest_f_cord[1]][lowest_f_cord[0]].h:
                                lowest_f = self.map_data[i][i2].f
                                lowest_f_cord = [i2,i]

        self.branch(lowest_f_cord[0],lowest_f_cord[1])
        self.map_data[lowest_f_cord[1]][lowest_f_cord[0]].explored = True
    
    def path(self):
        directions = []
        x_cord = self.bx
        y_cord = self.by
        while x_cord != self.ax or y_cord != self.ay:
            direction = self.map_data[y_cord][x_cord].direction
            directions.append(direction)
            if direction == "u":
                y_cord -= 1
            elif direction == "d":
                y_cord += 1
            elif direction == "l":
                x_cord -= 1
            elif direction == "r":
                x_cord += 1
        
        directions.reverse()
        for i in range(len(directions)):
            if directions[i] == "u":
                directions[i] = "d"
            elif directions[i] == "d":
                directions[i] = "u"
            elif directions[i] == "l":
                directions[i] = "r"
            elif directions[i] == "r":
                directions[i] = "l"
        
        return directions

        
    def draw(self):
        for layer in self.map_data:
            draw_layer = ""
            for l in layer:
                if isinstance(l,node):
                    if l.explored:
                        draw_layer += "[E]"
                    else:
                        draw_layer += "[X]"
                else:
                    draw_layer += "[" + str(l) + "]"
            print(draw_layer)
        print("----------------------------")

    def find_path(self):
        while not self.found:
            self.iterate()
            self.check()
        print(self.path())
    
    def find_path_draw(self):
        while not self.found:
            self.iterate()
            self.check()
            self.draw()
        print(self.path())






map_data = [
    [0,0,0,0,0,0,0,0],
    [0,1,1,1,1,0,0,0],
    [0,0,0,0,1,0,0,2],
    [0,0,1,0,0,1,1,1],
    [0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,0]
    ]


map1 = mapi([7,2],[7,5],map_data)
map1.find_path_draw()


