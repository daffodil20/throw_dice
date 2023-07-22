import random
# user = input("Please choose an integer between 1 and 6:")

# computer = [1,2,3,4,5,6]
# random_input = random.choice(computer)
# players = [user,computer]
num = input("Please input the times of this game(1/3/5):")
a = 0
x = 0
y = 0
while True:
    user = input("Please choose an integer between 1 and 6:")
    computer = [1,2,3,4,5,6]
    random_input = random.choice(computer)
    players = [user,computer]
    num = input("Please input the times of this game(1/3/5):")
    match players:
        case _ if int(user)< random_input:
            if num == "1":
                print('computer wins')
                break
            elif num == "3" and a<2:
                a+=1
                y+=1
                True
            elif num == "5" and a<4:
                a+=1
                y+=1
                True
            else:
                y+=1
                if x<y:
                    print('computer wins')
                    break
                elif x>y:
                    print('user wins')
                    break
        case _ if int(user) > random_input:
            if num == "1":
                print('user wins')
                break
            elif num == "3" and a<2:
                a+=1
                x+=1
                True
            elif num == "5" and a<4:
                a+=1
                x+=1
                True
            else:
                x+=1
                if x<y:
                    print('computer wins')
                    break
                elif x>y:
                    print('user wins')
                    break
           
        case "int(user) == random_input":
            print("no one wins")
            True
            