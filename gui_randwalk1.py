from tkinter import *
from matplotlib import pyplot as plt
#import tkinter.font as tkFont
from my_nr_random_walk import MyNRRandomWalk 
from my_saw1 import SAW
from my_nr_random_walk3D import NRRandomWalk3D
from mpl_toolkits.mplot3d import Axes3D

root = Tk()
root.title(" Random walk GUI")

# Add a grid Dropdown
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 20, padx = 20)

Label(mainframe, text="number of steps",font=40).grid(row = 1, column = 1) 
steps_entry = Entry(mainframe)
steps_entry.grid(column=2,row=1)
Label(mainframe, text="# of trials for SAW:",font=40).grid(row = 3, column = 1) 
samples_entry = Entry(mainframe)
samples_entry.grid(column=2,row=3)

def randwalk():
    print('hello random walk')

def dialog():
    #box.showinfo('Greetings','Welcome ' + entry.get())
    numc = steps_entry.get()
    num_steps=int(numc)
    z=tkvar.get()  # type of random walk
    print('steps: '+numc + '  walktype: '+z+'\n')
    if (z=='NR RANDOM WALK'):
        rw=MyNRRandomWalk(num_steps)
        rw.fill_walk()
        xwalk=rw.get_x()
        print(xwalk)
        plt.figure(figsize=(6,6))
        plt.title("NR random walk: green dot- start, red dot- finish")
        plt.plot(rw.x_val,rw.y_val,'b-')
        max_x=max(rw.x_val)
        min_x=min(rw.x_val)
        max_y=max(rw.y_val)
        min_y=min(rw.y_val)
        size_x=max(max_x,abs(min_x))
        size_y=max(max_y,abs(min_y))
        size=max(size_x,size_y) 
        #print("max min:",max_x,min_x)
        plt.axis([-size-1,size+1,-size-1,size+1])
        		
        #point_numbers=list(range(rw.num_points))
        #plt.scatter(rw.x_val,rw.y_val,c=point_numbers,cmap = plt.cm.Blues,edgecolor='none',s=15)
        #plt.axis([-30,30,-30,30])
        plt.scatter(0,0,c='green',edgecolors='none',s=40)
        plt.scatter(rw.x_val[-1],rw.y_val[-1],c='red',edgecolors='none',s=40)
        plt.show()
         
    elif(z=='NR RAND WALK 3D'):
        # non-returning random walk in 3 dimensions 	
        print(z)	
        rw=NRRandomWalk3D(num_steps)
        rw.fill_walk()
        fig = plt.figure(figsize=(6,6))
        ax = fig.add_subplot(111,projection='3d')
        print(rw.x_val[0],rw.y_val[0],rw.z_val[0])
        ax.plot(rw.x_val,rw.y_val,rw.z_val, zdir='z')
        point_numbers=list(range(rw.num_points))
        #plt.scatter(rw.x_val,rw.y_val,c=point_numbers,cmap = plt.cm.Blues,edgecolor='none',s=15)
        max_x=max(rw.x_val)
        min_x=min(rw.x_val)
        max_y=max(rw.y_val)
        min_y=min(rw.y_val)
        min_z=min(rw.z_val)
        max_z=max(rw.z_val)
        size_x=max(max_x,abs(min_x)) 
        size_y=max(max_y,abs(min_y))
        size_z=max(max_z,abs(min_z))
        size=max(size_x,size_y,size_z) 

        plt.axis([-size-1,size+1,-size-1,size+1])
        ax.set_zlim3d(bottom=-size-1,top=size+1)
        plt.scatter(0,0,zs=0,c='green',edgecolors='none',s=30)
        plt.scatter(rw.x_val[-1],rw.y_val[-1],zs=rw.z_val[-1],c='red',edgecolors='none',s=20)
        plt.title("NR random walk: green dot- start, red dot- finish")
        #plt.axes().get_xaxis().set_visible(False)
        #plt.axes().get_yaxis().set_visible(False)
        plt.show()			
       		
          		
    elif (z=='SELF AVOIDING WALK'):
        print(z)
        num_steps_c = steps_entry.get()
        num_steps=int(num_steps_c)	
        num_samples_c=samples_entry.get()
        num_samples=int(num_samples_c)
        #num_samples=3 # should be monotonic growing function:
        # for example, power or exp. depends on statistics of a snake biting its tail
        mysaw = SAW(num_samples,num_steps)
        mysaw.fill_walk()
        walk_x, walk_y = mysaw.walk()
        plt.title('Self avoiding walk: green dot - start, red dot - end')
        max_x=max(walk_x)
        min_x=min(walk_x)
        max_y=max(walk_y)
        min_y=min(walk_y)
        size_x=max(max_x,abs(min_x)) 
        size_y=max(max_y,abs(min_y))
        size=max(size_x,size_y) 
        print("max min:",max_x,min_x)
        plt.plot(walk_x,walk_y,'-b')
        #plt.axis([-30,30,-30,30])
        plt.axis([-size-1,size+1,-size-1,size+1])
        plt.scatter(0,0,c='green',edgecolors='none',s=30)
        plt.scatter(walk_x[-1],walk_y[-1],c='red',edgecolors='none',s=20)         
        if (len(walk_x)<num_steps):
            plt.suptitle('Collision: not enough trials',color='red')
        else:
            plt.suptitle('Success: no collisions ',color='green')

        #plt.text(0,min_y-1,'I am a text!',color='blue')	           		
        plt.show() 
    else:
        print('check the dropdown menu')	
    
btn = Button(mainframe,text='start walking',font=40,command=dialog)
btn.grid(column=2,row=4)


 # Create a Tkinter variable
tkvar = StringVar(root)
 
# Dictionary with options
choices = { 'NR RANDOM WALK','NR RAND WALK 3D','SELF AVOIDING WALK'}
tkvar.set('NR RANDOM WALK') # set the default option
 
popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="choose a walk", font=40).grid(row = 2, column = 1)
popupMenu.grid(row = 2, column =2)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
steps_entry.focus() 

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )
 
# link function to change dropdown
tkvar.trace('w', change_dropdown)


 
root.mainloop()