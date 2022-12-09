from Attributes import Treasure


class Map:
    Map_small = """
    [X] [X] [X] [X]
    [X] [X] [X] [X]
    [X] [X] [X] [X]
    [X] [X] [X] [X]

    (1, 1):
    (1, 2): 
    (1, 3):
    (1, 4):
    (2, 1):
    (2, 2): 
    (2, 3):
    (2, 4):
    (3, 1):
    (3, 2): 
    (3, 3):
    (3, 4):
    (4, 1):
    (4, 2): 
    (4, 3):
    (4, 4):
    """

    print("Enter coordinates: ")

#    gridline = []
#for i in range(4):
#   gridline.append("")
#grid = []
#for i in range(4):
#    grid.append(list(gridline))

nums = []
for i in range(3):
    nums.append([])
    for j in range(1, 4):
        nums[i].append(j)
print("3X3 grid with numbers:")
print(nums)