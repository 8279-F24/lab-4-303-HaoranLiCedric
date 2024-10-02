import time

#cp.pixels.auto_write = False
#cp.pixels.brightness = 0.3
flag = 1
cp_color = [(0,0,0)]*10
while flag == 1:
    max = 255
    color1 = input("Witch color do you want to show?(Enter 'r' for red or 'g' for green):").lower()
    if color1 == "r":
        while max > 0:
    
            for i in range(10):
                cp_color[i] = (max, 0, 0) 
            #cp.pixels.show()
            print(cp_color)
            time.sleep(0.3)

            max = max - 1
    elif cp_color == "g":
        while max > 0:
    
            for i in range(10):
                cp_color[i] = (0, max, 0) 
            #cp.pixels.show()
            print(cp_color)
            time.sleep(0.3)

            max = max - 1
    else:
        print("Invalid input, please enter r or g.")
        
    restart = input("Do you want to start again?(Enter'q'to stop,any other key to continue):").lower()
    if restart == "q":
    
        #cp_pixels.fill((0, 0, 0))
        #cp.pixels.show()
        flag = 0
        print("Program ended.")
        break
