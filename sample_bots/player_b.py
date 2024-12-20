import sys
import math

# Grow and multiply your organisms to end up larger than your opponent.

# width: columns in the game grid
# height: rows in the game grid
width, height = [int(i) for i in input().split()]
print(f"w={width}, h={height}", file=sys.stderr, flush=True)

# game loop
while True:
    grid = [[-100 for x in range(width)] for y in range(height)]
    my_organ_id = -1

    entity_count = int(input())
    for i in range(entity_count):
        inputs = input().split()
        x = int(inputs[0])
        y = int(inputs[1])  # grid coordinate
        _type = inputs[2]  # WALL, ROOT, BASIC, TENTACLE, HARVESTER, SPORER, A, B, C, D
        owner = int(inputs[3])  # 1 if your organ, 0 if enemy organ, -1 if neither
        organ_id = int(inputs[4])  # id of this entity if it's an organ, 0 otherwise
        organ_dir = inputs[5]  # N,E,S,W or X if not an organ
        organ_parent_id = int(inputs[6])
        organ_root_id = int(inputs[7])
        grid[y][x] = owner
        if owner == 1:
            my_organ_id = organ_id

    # my_d: your protein stock
    my_a, my_b, my_c, my_d = [int(i) for i in input().split()]
    # opp_d: opponent's protein stock
    opp_a, opp_b, opp_c, opp_d = [int(i) for i in input().split()]
    required_actions_count = int(input())  # your number of organisms, output an action for each one in any order
    cmd = "WAIT"
    for y in range(height):
        for x in range(width):
            if cmd == "WAIT":
                if grid[y][x] == -100:
                    cmd = f"GROW {my_organ_id} {x} {y} BASIC"

    # print(cmd)
    print("WAIT")

