#
(Make Benefit Programming)

# Ruby Tetrahedron Test for Sketchup

(current approach nonfunctional as of 8/5/18)

The goal is to create Tetrahedron from the x,y,z coordinate system.    

The current ideal works from the x,y plane first, creating a equilateral triangle with the following points, with scale being the variable length of one edge:
#

- (0,0,0)
- (scale,0,0)
- (scale/2, scale * (Math.sqrt(3) / 2) , 0)

# New approaches:

….Make the tetrahedron on a tilt then transform its location:  See here:
http://mathworld.wolfram.com/RegularTetrahedron.html

….Or just use angles.
