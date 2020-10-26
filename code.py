from PIL import Image
import random
imgs=['1.png','2.png','3.png','4.png','5.png','6.png']
print("\t\t\t\tWelcome to Dice Simulator\n")
while True:
    print("\t\t\tIf you wish to proceed further press enter\n\t\t\tIf you wish to exit the simulator, press E")
    inp=input()
    if inp=='e' or inp=='E':
        break
    else:
        print("You are here!!!")
        img=Image.open('./images/'+random.choice(imgs))
        img.show()  