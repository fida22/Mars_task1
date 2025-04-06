def arena_map(obstacles):
    #estimating size of matrix 
    global n 
    n=max(max(row)for row in obstacles)

    #creating matrix
    arena=[[1 for i in range((2*n+1))] for j in range((2*n+1))]

    #positioning brick at the center
    arena[n][n]="B"

    #marking obtacles
    for obstacle in obstacles:
        #north-south
        vertical_movement=obstacle[0]-obstacle[2]
        #east-west
        horizontal_movement=obstacle[1]-obstacle[3]

        #calculating vertical and horizontal distances from center to get row and column
        row=n-vertical_movement
        column=n+horizontal_movement

        #marking the obstacle
        arena[row][column]=0

    return arena
if __name__=="__main__":

    #extracting data from text file
    # Initialize an empty list to store obstacle data
    obstacles=[]
    # Open the text file and read its contents
    with open ("sample.txt") as f:
        # Read each line, convert it to a list of integers, and add to obstacles
        for x in f:
            row=list(map(int,x.strip().split( )))
            obstacles.append(row)
    
    #create arena map
    arena=arena_map(obstacles)
    #printing map
    print("_"*(4*n+4))
    for row in arena:
        print("|",end="")
        for element in row:
            print(element,end=" ") 
        print("|",end="")    
        print()   
    print("_"*(4*n+4))
  
        
        

    