# ray_ellipsoid_intersection.py
#
# Usage: python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z
# Finds the intersection point (if it exists) between a ray and the earth reference ellipsoid
#
# Equations from AOE 4414 class at Virginia Tech
# Parameters:
# c_in: input channel count
# n_wv: number of weight vectors
#
# Output:
# Prints the x, y, and z components of the intersection
# Written by Brooklyn Beck
#
# import Python modules
import math # math module
import sys # argv
# "constants"
R_E = 6378.1363
E_E = 0.081819221456
# helper functions

#magnitude
def mag(v):
  sum_of_squares = 0.0
  for i in range(0,len(v)):
    sum_of_squares += v[i]**2
  return math.sqrt(sum_of_squares)

#scalar multiplication
def smul(s,v):
  sprod = []
  for i in range (0, len(v)):
    sprod.append(s*v[i])
  return sprod

#vector addition
def add(v1,v2):
  if len(v1) != len(v2):
    return None
  else:
    v3 = []
    for i in range(0,len(v1)):
      v3.append(v1[i]+v2[i])
    return v3

#vector subraction
def sub(v1,v2):
  if len(v1) != len(v2):
    return None
  else:
    v3 = []
    for i in range(0,len(v1)):
      v3.append(v1[i]-v2[i])
    return v3

#dot product
def dot(v1,v2):
  if len(v1) != len(v2):
    return float('nan')
  else:
    dp = 0.0
    for i in range(0,len(v1)):
      dp += v1[i]*v2[i]
    return dp

# initialize script arguments
d_l_x = float('nan') # x-component of origin-referenced ray direction
d_l_y = float('nan') # y-component of origin-referenced ray direction
d_l_z = float('nan') # z-component of origin-referenced ray direction
c_l_x = float('nan') # x-component offset of ray origin
c_l_y = float('nan') # y-component offset of ray origin
c_l_z = float('nan') # z-component offset of ray origin
# parse script arguments
if len(sys.argv)==7:
  d_l_x = float(sys.argv[1])
  d_l_y = float(sys.argv[2])
  d_l_z = float(sys.argv[3])
  c_l_x = float(sys.argv[4])
  c_l_y = float(sys.argv[5])
  c_l_z = float(sys.argv[6])
else:
  print(\
  'Usage: '\
  'python3 ray_ellipsoid_intersection.py d_l_x d_l_y d_l_z c_l_x c_l_y c_l_z'\
  )
  exit()
# main script below

d_l = [d_l_x,d_l_y,d_l_z]
c_l = [c_l_x,c_l_y,c_l_z]

#discriminant
a = d_l_x**2 + d_l_y**2 + d_l_z**2/(1-E_E**2)
b = 2.0*(d_l_x*c_l_x + d_l_y*c_l_y + d_l_z*c_l_z/(1-E_E**2))
c = c_l_x**2 + c_l_y**2 + c_l_z**2/(1-E_E**2) - R_E**2
discr = b**2 - 4.0*a*c

if discr >= 0.0:
  d = (-b - math.sqrt(discr))/(2*a)
  if d < 0.0:
    d = (-b + math.sqrt(discr))/(2*a)
  l_d = add(smul(d,d_l),c_l)

# print outputs
print(l_d[0]) # x-component of intersection point
print(l_d[1]) # y-component of intersection point
print(l_d[2]) # z-component of intersection point
