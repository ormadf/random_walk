from random import randint
from my_nr_random_walk import MyNRRandomWalk

class NRRandomWalk3D(MyNRRandomWalk):
    """ Random walk on 3D square lattice """
    
    def __init__(self,num_points=10):
        """ init random walk"""	
        super().__init__(num_points)		
        self.num_points = num_points
        self.x_val = [0]
        self.y_val = [0]
        self.z_val = [0]
		
    def stepf(self):
        die = randint(1,6)
        if die == 1:
            x_step, y_step, z_step = 1,0,0                          				
        elif die == 2:
            x_step, y_step, z_step =-1,0, 0                      				
        elif die == 3:
            x_step, y_step, z_step = 0,1,0            
        elif die == 4:
            x_step, y_step, z_step = 0 , -1, 0
        elif die == 5:
            x_step, y_step, z_step = 0,0,1
        elif die == 6:
            x_step, y_step, z_step =0, 0, -1
        else:
            print('check stepf function')    			
        
        return x_step, y_step, z_step
			
    def fill_walk(self):
        """ calc the random walk points"""	
        while len(self.x_val) < self.num_points:
            x_step, y_step, z_step = self.stepf()              
            next_x = self.x_val[-1] + x_step
            next_y = self.y_val[-1] + y_step
            next_z = self.z_val[-1] + z_step
            #print("x_val: ",self.x_val)
            #print("y_val: ",self.y_val)
            #print("z_val",self.z_val)  			
            if ((len(self.x_val)>1) and ((next_x,next_y,next_z) ==(self.x_val[-2],self.y_val[-2],self.z_val[-2]))):
                continue			
              			
            self.x_val.append(next_x)
            self.y_val.append(next_y)
            self.z_val.append(next_z)
			
    def get_x(self):
        return self.x_val

    #def get_y_val		
		