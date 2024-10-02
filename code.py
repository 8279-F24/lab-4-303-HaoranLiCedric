import time
from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.3
flag = 1

while flag == 1:
    max_value = 255 

    while True: 
        try:

            cp_color = int(input("Which color do you want to show? (Enter '1' for red, '2' for green, '3' for blue): "))
            if cp_color not in [1, 2, 3]:
                print("Invalid input, please enter '1', '2', or '3'.")
            else:
                break 
        except ValueError:
            print("Wrong input, you should enter a number.")

    if cp_color == 1:
        while max_value > 0:
            for i in range(10):
                cp.pixels[i] = (max_value, 0, 0)
            cp.pixels.show()
            time.sleep(0.3)
            max_value -= 1
    elif cp_color == 2:
        while max_value > 0:
            for i in range(10):
                cp.pixels[i] = (0, max_value, 0) 
            cp.pixels.show()
            time.sleep(0.3)
            max_value -= 1
    elif cp_color == 3:
        while max_value > 0:
            for i in range(10):
                cp.pixels[i] = (0, 0, max_value) 
            cp.pixels.show()
            time.sleep(0.3)
            max_value -= 1

    restart = input("Do you want to start again? (Enter 'q' to stop, any other key to continue): ").lower()
    if restart == "q":
        cp.pixels.fill((0, 0, 0))
        cp.pixels.show()
        flag = 0
        print("Program ended.")
        break