import time
from room2 import room_2
import os

def room_1(name, been_here):
        if been_here <= 0:
          time.sleep(2)
          print("""
             .           .
            /|__________/|
          .// /       .//|     
          |/_/________|//|  
          |_|_________|/    
          |           |      

                """)
          time.sleep(2)
          print(f"Hej {name} välkomen till spelet du är just nu hemma och har precis vaknat")
          time.sleep(2)
          print("Sedan kom du på att du skulle hjälpa dina kompisar")
          time.sleep(2)
          print("Ditt mål nu är att utforska ditt hus och hjälpa alla kompisar på vägen")
          time.sleep(4)
        print("""
             __________
            |  __  __  |
            | |  ||  | |
            | |  ||  | |
            | |__||__| |
            |  __  __()|
 _______    | |  ||  | |
|_o_|_o_|   | |  ||  | |
|___o___|   | |  ||  | |   ^~^  ,
|___o___|   | |  ||  | |  ('Y') )
|___o___|   | |__||__| |  /   \/
 ||   ||    |__________| (\|||/)
          """)
        time.sleep(2)
        print("Du ser en dörr och din garderob framför dig")
        time.sleep(2)
        open_were = input("Vad vill du göra öppna dörren eller öppna garderob?\n").lower()
        if open_were == "door":
            print("Du öppnar dörren och går in till hallen")
            been_here + 10
            os.system("cls")
        elif open_were == "garderob":
            print("Du går till garderoben och öppnar den")
            time.sleep(3)
            print("du hittar inte jätte många saker i den förutom dina kläder och en gamal fotboll")
            time.sleep(3)
            print("""
    ,==c==.
    |_/|\_|
    |  |  |     _._
    |  |  |   .'--.`.
    |  |  |   |  .' |
    |__|__|    `--`'
                  """)
            time.sleep(2)
            print("du väljer nu att öppna dörren och går ut till hallen")
            been_here + 10
            time.sleep(4)
            os.system("cls")
            return(been_here)



name = "wille"
room_1(name, 0)
room_2(name)