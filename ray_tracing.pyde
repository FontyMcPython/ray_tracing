#-------------------------------------------|
#           Ray Tracing Test                |
#           Jose Font 7/2019                |
#                                           |
#                                           |
#___________________________________________|

# Class for the Wall || Builder takes two pairs
#                    || of coordenates for the
#                    || vertex.
class wall:
    def __init__(self, a_x, a_y, b_x, b_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        
    # Shows the Wall
    def show(self):
        # Color of the wall
        stroke(255)
        line(self.a_x, self.a_y, self.b_x, self.b_y)

# Class for the Ray || Builder takes the
#                   || direction of the
#                   || ray in rads.
class ray:
    def __init__(self, dir_rad):
        self.dir_rad = dir_rad
    # Shows the ray. Takes the origin as a
    # pair of coordinates.    
    def show(self, origin_x, origin_y):
        # Max distance of view.
        r = 700
        # Color of the ray
        stroke(255)
        # Find collision with wall or border
        for el in walls:
            # Formula to calculate the distance the ray travels
            if not tan(self.dir_rad)*(el.b_x - el.a_x) == (el.b_y - el.a_y):
                r2 = ((el.a_y - origin_y) + tan(self.dir_rad)*(origin_x - el.a_x))/(tan(self.dir_rad)*(el.b_x - el.a_x) - (el.b_y - el.a_y))
                end_x = el.a_x + r2*(el.b_x - el.a_x)
                end_y = el.a_y + r2*(el.b_y - el.a_y)
                r1 = (end_x - origin_x)/cos(self.dir_rad)
                if r2 >= 0 and r2 <=1:
                    if r1 > 0:
                       if r1 < r:
                           r = r1
       # Plot the ray 
        end_x = origin_x + r*cos(self.dir_rad)
        end_y = origin_y + r*sin(self.dir_rad)
        #point(end_x, end_y)
        line(origin_x, origin_y, end_x, end_y)
# List of walls.        
walls = []  
# List of rays
rays = []
    
def setup():
    # Setting canvas
    size(480, 480)
    background(0)
    # Walls
    walls.append(wall(0, 0, 0,  height-1)) # Muro izquierda
    walls.append(wall(0, height-1, width-1, height-1)) # Muro inferior
    walls.append(wall(width-1, height-1, width-1, 0)) # Muro derecho
    walls.append(wall(width-1, 0, 0, 0)) # Muro superior
    #room
    walls.append(wall(50, 300, 200, 300))
    walls.append(wall(200, 200, 200, 350))
    walls.append(wall(50, 300, 50, 450))
    walls.append(wall(50, 450, 200, 450))
    walls.append(wall(200, 480, 200, 400))
    # Rays
    for i in range(0, 360):
        rays.append(ray(2*PI*i/360))
    
    
def draw():
    # Reset canvas
    background(0)
    # Plot Walls
    #for el in walls:
     #   el.show()
    # Plot rays
    for el in rays:
        el.show(mouseX, mouseY)
