class wall:
    def __init__(self, a_x, a_y, b_x, b_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        
    
    def show(self):
        stroke(255)
        line(self.a_x, self.a_y, self.b_x, self.b_y)
        
class ray:
    def __init__(self, dir_rad):
        self.dir_rad = dir_rad
        
    def show(self, origin_x, origin_y):
        r = 700
        stroke(255)
        # Find collision with wall or border
        for el in walls:
            if not tan(self.dir_rad)*(el.b_x - el.a_x) == (el.b_y - el.a_y):
                r2 = ((el.a_y - origin_y) + tan(self.dir_rad)*(origin_x - el.a_x))/(tan(self.dir_rad)*(el.b_x - el.a_x) - (el.b_y - el.a_y))
                end_x = el.a_x + r2*(el.b_x - el.a_x)
                end_y = el.a_y + r2*(el.b_y - el.a_y)
                r1 = (end_x - origin_x)/cos(self.dir_rad)
                if r2 >= 0 and r2 <=1:
                    if r1 > 0:
                       if r1 < r:
                           r = r1 
        end_x = origin_x + r*cos(self.dir_rad)
        end_y = origin_y + r*sin(self.dir_rad)
        line(origin_x, origin_y, end_x, end_y)
        
walls = []  
rays = []
res = 0.003
    
def setup():
    size(480, 480)
    background(0)
    # Muros
    walls.append(wall(0, 0, 0,  height-1)) # Muro izquierda
    walls.append(wall(0, height-1, width-1, height-1)) # Muro inferior
    walls.append(wall(width-1, height-1, width-1, 0)) # Muro derecho
    walls.append(wall(width-1, 0, 0, 0)) # Muro superior
    walls.append(wall(30, 60, 120, 230))
    walls.append(wall(width/2, height, width, 400))
    # Rayos
    for i in range(0, 90):
        rays.append(ray(2*PI*i/90))
    
    
def draw():
    background(0)
    for el in walls:
        el.show()
    for el in rays:
        el.show(mouseX, mouseY)
    
