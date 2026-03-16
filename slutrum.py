import time
import os
def endroom(name):
    points = help_67 + help_amungus + help_tung + help_tralalero
    time.sleep(2)
    print("Du har nu kommit till slutrummet")
    time.sleep(2)
    print("""
             __________     __________
            |  __  __  |   |  __  __  |
            | |  ||  | |   | |  ||  | |
            | |  ||  | |   | |  ||  | |
            | |__||__| |   | |__||__| |
            |  __  __()|   |  __  __()|
            | |  ||  | |   | |  ||  | |
            | |  ||  | |   | |  ||  | |
            | |  ||  | |   | |  ||  | |
            | |  ||  | |   | |  ||  | |
            | |__||__| |   | |__||__| |
            |__________|   |__________|
         
              (Dörr 1)       (Dörr 2)
""")
 
    if points == 0:
        print("Du har hjälp 0/4 brainrots, Du kommer att förlora ifall du avslutar")
    elif points == 1:
        print("Du har hjälp 1/4 brainrots, Du kan avsluta ifall du vill")
    elif points == 2:
        print("Du har hjälp 2/4 brainrots, Du kan avsluta ifall du vill")
    elif points == 3:
        print("Du har hjälp 3/4 brainrots, Du kan avsluta ifall du vill")
    elif points == 4:
       print("Du har hjälp 4/4 brainrots, Du kan avsluta ifall du vill")


    time.sleep(2)
    print("Dörr 1 avslutar spelet")
    time.sleep(4)
    print("Dörr 2 tar dig tillbaka")
    while True:
        val = input("Vilken dörr vill du gå in i  (1/2)\n")
        if val == "1":
            print("Du har avslutat spelet")
            print(f"Dina poäng: {points}/4")
            exit()
            break
        elif val == "2":
            print("du går tillbaka")
            time.sleep(2)
            os.system("cls")
            room_2(name)
            break
        else:
            print("Du har valt något, testa igen")  
