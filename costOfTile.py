"""
Program to calculate the total cost of tile it
would take to cover a floor plan of width and height,
using a cost entered by the user. Take W, H, and cost from user.
"""

if __name__ == "__main__":

    print "Enter width of the floor:"
    width = input()
    
    print "Enter height of the floor:"
    height = input() 
    
    print "Enter the cost of one tile per square feet:"
    costOfTile = input()
    
    print "\nWidth = %f" %width
    print "\nHeight = %f" %height
    print "\nCost of tile per square feet = %f" %costOfTile
    
    areaOfFloor = width * height
    print "\nareaOfFloor : %f" % areaOfFloor
    
    totalCost =  float(areaOfFloor * costOfTile)
    print "\nTotal cost of tile to cover the floor is : %f" %totalCost
