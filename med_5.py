import math

def euler_to_quaternion(roll,pitch,yaw):
    #convert to radians
    roll=math.radians(roll)
    pitch=math.radians(pitch)
    yaw=math.radians(yaw)

    #computing sin and cos of half angles
    cr=math.cos(roll)
    sr=math.sin(roll)
    cp=math.cos(pitch)
    sp=math.sin(pitch)
    cy=math.cos(yaw)
    sy=math.sin(yaw)

    #computing quaternion
    w=cr*cp*cy+sr*sp*sy
    x=sr*cp*cy-cr*sp*sy
    y=cr*sp*cy+sr*cp*cy
    z=cr*cp*sy-sr*sp*cy

    return (w,x,y,z)

