#https://codeclubprojects.org/en-GB/python/rock-paper-scissors/
from random import randint
#-------------func--------------
def outcome():
    if   player==computr:
        print("DRAW!")
#-------------rock------------------   
    elif player=="r" and computr=="s":
        print("Playe win")
    elif player=="r" and computr=="p":
        print("Computr win")
#-------------paper-----------------
    elif player=="p" and computr=="r":
        print("Playe win")
    elif player=="p" and computr=="s":
        print("Computr win")
#-------------scissors--------------
    elif player=="s" and computr=="p":
        print("Playe win")
    elif player=="s" and computr=="r":
        print("Computr win")

#-------------Main--------------
player=input("rock (r), paper (p), or scissors (s)? ")
print(player,"vs",end=" ")

chosen=randint(1,3)
if chosen==1:
    computr="r"
if chosen==2:
    computr="p"
if chosen==3:
    computr="s"

print(computr)
outcome()
