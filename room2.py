import time 
from room4 import room_4 
import os

def room_2(name):
    print(f"Hej {name} du är nu i hallen")
    time.sleep(2)
    print("du har 4 dörrar runt omkring dig")
    time.sleep(2)
    print("""    

 __________         __________         __________         __________
|  __  __  |       |  __  __  |       |  __  __  |       |  __  __  |
| |  ||  | |       | |  ||  | |       | |  ||  | |       | |  ||  | |
| |  ||  | |       | |  ||  | |       | |  ||  | |       | |  ||  | |
| |__||__| |       | |__||__| |       | |__||__| |       | |__||__| |
|  __  __()|       |  __  __()|       |  __  __()|       |  __  __()|
| |  ||  | |       | |  ||  | |       | |  ||  | |       | |  ||  | |
| |  ||  | |       | |  ||  | |       | |  ||  | |       | |  ||  | | 
| |  ||  | |       | |  ||  | |       | |  ||  | |       | |  ||  | |
| |  ||  | |       | |  ||  | |       | |  ||  | |       | |  ||  | | 
| |__||__| |       | |__||__| |       | |__||__| |       | |__||__| | 
|__________|       |__________|       |__________|       |__________|  
  (Dörr 1)           (Dörr 2)           (Dörr 3)          (Dörr 4)
""")
    time.sleep(2)
    print("Dörr 1 går tillbaka till ditt rum")
    time.sleep(1)
    print("Dörr 2 går till köket")
    time.sleep(1)
    print("Dörr 3 går till vardagsrummet")
    time.sleep(1)
    print("Dörr 4 går går du ut från huset")
    time.sleep(2)
    open_door = input("Vilken dörr vill du gå in i? 1,2,3,4?\n").lower()
    if open_door == "dörr 1" or open_door == "1":
        print("Du går in i dörr 1")
        time.sleep(3)
        os.system("cls")
        from room1 import room_1
        room_1(name, 10)
    elif open_door == "dörr 2" or open_door == "2":
        print("Du går in i dörr 2")
        time.sleep(3)
        os.system("cls")
        from room3 import room_3
        room_3(name, False)
    elif open_door == "dörr 3" or open_door == "3":
        print("Du går in i dörr 3")
        time.sleep(3)
        os.system("cls")
        room_4(name, False)
    elif open_door == "dörr 4" or open_door == "4":
        print("Du går in i dörr 4")
        time.sleep(3)
        os.system("cls")
    return()