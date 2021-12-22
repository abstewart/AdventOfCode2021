Thinking for day 22 pt 2:

Class for region:
on: T if on, F if off
x1,x2,y1,y2,z1,z2 for the cuboid definition
Adjustments for the list of regions that adjust this region


Each line in the input corresponds to a region, stored as a tuple: (onoff,x1,x2,y1,y2,z1,z2,adjust)
onoff is True if on, False if off. The rest are ints

Go through the regions:
if a region doesn't intersect any other region and it is 'on',
   add the region tuple to the reactor

if a region is on and intersects with another region in the reactor that's on:
   find the intersection between the two regions (including the adjustments to the already present region
   and add that region as off in the adjustments of the new region

if a region is on and intersects with another region in the reactor that's off
