class Celula:
    def __init__(self, value):
        
        self.value   =  value
        self.visited = False

        self.up    =  None
        self.down  =  None
        self.left  =  None
        self.right =  None


    def __repr__(self):
        return self.value

    
    def set_up(self, cell):
        self.up = cell
    
    def set_down(self, cell):
        self.down = cell

    def set_left(self, cell):
        self.left = cell

    def set_right(self, cell):
        self.right = cell


    def get_value(self):
        return self.value