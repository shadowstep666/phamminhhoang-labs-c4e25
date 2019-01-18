def is_inside(x,y):
    if x[0]<=x[1]<=x[0]+[2] | y[0]<=y[1]<=y[0]+[2]:
        return True
    else : 
        return False

new_inside=is_inside([200, 120], [140, 60, 100, 200])
if True:
    print("Your function is correct")
else:
    print("Ooops, bugs detected")