from random import choice

class MyNRRandomWalk():
    """ Random walk on square lattice """
    
    def __init__(self,num_points=10):
        """ init random walk"""	
        self.num_points = num_points
        self.x_val = [0]
        self.y_val = [0]
    
    def fill_walk(self):
        """ calc the random walk points"""	
        while len(self.x_val) < self.num_points:
            die = choice([1,2,3,4])
            if die == 1:
                x_step = 1
                y_step = 0                          				
            elif die == 2:
                x_step = 0
                y_step = 1                     				
            elif die == 3:
                x_step = -1
                y_step = 0            
            elif die == 4:
                x_step = 0
                y_step = -1
              
            next_x = self.x_val[-1] + x_step
            next_y = self.y_val[-1] + y_step
            if ((len(self.x_val)>1) and ((next_x,next_y) ==(self.x_val[-2],self.y_val[-2]))):
                continue			
              			
            self.x_val.append(next_x)
            self.y_val.append(next_y)
     
    def get_x(self):
        return self.x_val

    #def get_y_val		
		