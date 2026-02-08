# Write your program here
"""
Docstring for fivestar:
The program will take in input from the user to determine the number of new videos,
and oldies and output the cost.
It will multiply the cost for each oldies by the number of oldies and add them
to the number of videos multiplied by the cost for each video

"""

newVideos = int(input("Enter the number of new videos: "))
oldies = int(input("Enter the number of oldies: "))
VIDEOSCOST = 3.00
OLDIESTCOST = 2.00
cost = (oldies * OLDIESTCOST) + (newVideos * VIDEOSCOST)
print("The total cost is $" + str(cost))
