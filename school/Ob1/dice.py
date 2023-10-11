import random as r


randnum = r.randint(1,6)

def dice(num):
    sidedotR = " "
    sidedotL = " "
    centdot = " "
    topSideDotL = " "
    topSidedotR = " "
    Tcentdot = " "
    if num == 1:
        centdot = "*"
    if num == 2:
        sidedotL = "*"
        sidedotR = "*"
    if num == 3:
        sidedotL = "*"
        sidedotR = "*"
        centdot = "*"
    if num == 4:
        sidedotR = "*"
        topSideDotL = "*"
        topSidedotR = "*"
        centdot = "*"
    if num == 5:
        sidedotL = "*"
        sidedotR = "*"
        topSideDotL = "*"
        topSidedotR = "*"
        centdot = "*"
    if num == 6:
        sidedotL = "*"
        sidedotR = "*"
        topSideDotL = "*"
        topSidedotR = "*"
        centdot = "*"
        Tcentdot = "*"
    print("###########")
    print("#         #")
    print(f"#  {topSidedotR} {Tcentdot} {topSideDotL}  #")
    print(f"#         #  you rolled a {num}")
    print(f"#  {sidedotL} {centdot} {sidedotR}  #")
    print("#         #")
    print("###########")

dice(randnum)