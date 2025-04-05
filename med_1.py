def final_marker_position(x,y,z):
    y_final=y+55
    return (x,y_final,z)
def calculate_distance(x1,y1,z1,x2,y2,z2):
    distance=((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5
    return distance

if __name__=="__main__":
    # Get user input and convert to floats
    (x,y,z)=tuple(map(float,input().split(',')))

    #assigning camera position , the axis in which camera is there is considered as z axis
    camera_x,camera_y,camera_z=x,y,0

    (x_final,y_final,z_final)=final_marker_position(x,y,z)

    #calculating distances
    distance_before=calculate_distance(camera_x,camera_y,camera_z,x,y,z)
    distance_after=calculate_distance(camera_x,camera_y,camera_z,x_final,y_final,z_final)

    #printing results
    print("corrected marker position: ",x_final,y_final,z_final)
    print("distance between camera and marker before correction: ",distance_before)
    print("distance between camera and marker after correction: ",distance_after)





