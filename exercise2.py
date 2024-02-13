# exercise2
from math import pi, degrees, radians
# deg2rad
# Write a program that takes an array/list of angles in degrees and 
# converts them to radians.The Result should be placed in a list of tuples.
#  73°, 18.34°, 240°

# rad2deg
# Write a program that takes an array/list of angles in radians and 
# converts them to degrees.The result should be placed in a dictionary. 
# 3.721 rad, 7π/6 rad ,11π/12 rad

def deg2rad(deg_angles:list)-> tuple:
    rad = (deg_angles,)
    for i in range(len(deg_angles)):
        rad[0][i-1] = deg_angles[i-1]*(pi/180)
    return(rad)

def rad2deg(rad_angles:list)-> dict:
    deg = {}
    for x in rad_angles:
        deg[x] = degrees(x)
    return(deg)

def main():
    print('Wazz up')
    print(deg2rad([30,45,90,360]))
    print(rad2deg([3.141519281928, 3.721, 7*pi/6, 11*pi/12]))

if __name__ == '__main__':
    main()