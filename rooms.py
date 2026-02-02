import time
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
        open_were = input("Vad vill du göra öppna dörren eller öppna garderoben?\n").lower()
        if open_were == "dörren" or open_were =="öppna dörren":
            print("Du öppnar dörren och går in till hallen")
            been_here + 10
            os.system("cls")
        elif open_were == "garderob" or open_were =="öppna garderoben":
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
        
        
        
        
def room_2(name):
    print(f"Hej {name} du är nu i hallen  (Rum 6)")
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
        room_1(name, 10)
    elif open_door == "dörr 2" or open_door == "2":
        print("Du går in i dörr 2")
        time.sleep(3)
        os.system("cls")
        room_3(name)
    elif open_door == "dörr 3" or open_door == "3":
        print("Du går in i dörr 3")
        time.sleep(3)
        os.system("cls")
        room_4(name)
    elif open_door == "dörr 4" or open_door == "4":
        print("Du går in i dörr 4")
        time.sleep(3)
        os.system("cls")
    return()



def room_3(name, been_here):
    print(f"Hej {name} du är nu i köket  (Rum 3)")
    time.sleep(2)
    print("när du kommer in i köket ser du din kompis tung tung sahur")
    time.sleep(2)
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠐⢂⠐⡒⠂⣐⡢⠤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⢁⣺⣿⣿⣿⣿⣿⣿⣿⣶⠈⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠃⠼⢽⣿⣿⠿⠻⠛⠻⢿⣿⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣵⠁⠀⠀⠀⠙⠁⠀⠀⢠⡀⠀⢬⠃⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⠀⠀⠻⡄⠀⣇⠀⠃⠀⠘⡇⠀⠄⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⢈⢸⡿⣦⣀⢀⣀⣴⣷⡆⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠙⠳⠞⠁⠸⠷⠦⠈⠉⠉⠉⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢫⣦⠀⠀⠆⠀⠀⠤⠿⠂⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣧⡄⠀⠀⠀⠈⣠⡼⠃⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃⠀⠀⠀⠛⠉⠀⢀⠠⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⠠⠀⠀⠀⠀⢤⠘⠤⠁⢰⡆⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⢠⠋⠤⡉⠐⡀⠀⢿⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠄⠀⠀⡘⢀⠆⠡⠀⠀⣈⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡐⠈⠤⢁⠂⠀⡟⢰⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⡀⠀⠀⠀⠠⠁⠂⠄⠀⣸⠁⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠁⠀⠀⠀⠀⠀⠀⠀⠈⠁⢰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⢁⠆⠀⠀⠀⢀⣐⠀⠀⠀⢀⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠐⡁⠁⣼⡇⠀⠀⣿⣿⠀⡀⢀⣷⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠁⡔⠀⣼⣿⡇⣀⠀⣿⣿⡆⣡⠘⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⢠⡞⢀⣾⣿⣿⣇⠀⠀⢿⣿⡇⠁⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⣴⡇⢠⣾⠋⠠⢸⣿⠀⠀⢸⣿⣧⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠌⣼⠍⢀⣿⡇⢐⠘⢸⣿⡀⠀⢸⣿⣿⡀⠀⣻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠊⡸⠁⢀⣾⠟⣀⢂⠀⢰⣿⣇⢀⠈⣿⣿⡇⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠜⠁⠄⠀⢠⡾⠫⢀⠸⠠⣴⣿⣿⡟⠀⠀⢿⡿⠁⠀⠘⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⣠⣾⢁⡆⢚⠼⠛⣛⣹⡏⠀⠀⠀⠀⢠⣾⣆⠀⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⢀⡀⠀⢰⡏⣴⢯⡂⠄⠤⡶⠋⠉⣁⣠⣴⡆⠰⠛⠻⠻⠢⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠑⠋⠘⢑⠻⣿⣷⣶⣶⣾⡿⢟⢩⣯⣁⣀⡊⣘⣀⣀⣤⣿⠀
""")
    help = input("Skulle du kunna hjälpa mig med en sak? J/N\n").upper()
    time.sleep(2)
    if help == "J":
        print("jag har tappat bort min katt kan du hjälpa mig att hitta den?")
        time.sleep(2)
        print(""" 
Den ser ut så här:
  ^~^  ,
 ('Y') )
 /   \/
(\|||/)
""")
        print("senaste gånger jag såg han försökte han leka med en gamal fotboll")
        time.sleep(2)
        while True:
          svar = input("Vilket rum är katten i ?\n")
          if svar == "1":
            print(f"tack så myckte {name} han betyder väldigt mycket för mig")
            time.sleep(2)
            print(f"DU har nu hjälp Tung tung sahur")
            help_tung = 1
            break
          elif not svar =="1":
            print("Katten var inte i det rummet försök igen tack")
    elif help == "N":
      help_tung = 0
      print("Du hjälpte inte din kompis och fick inte något poäng han blev lite ledsen")
      time.sleep(2)
    print("nu efter du har pratat med personen ser du 2 dörrar")
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
    print("Dörr 1 Går tillbaka till Hallen")
    time.sleep(2)
    print("Dörr 2 Går till nästa rum")
    door = input("vilken dörr vill du gå in i\n")
    time.sleep(2)
    if door == "1":
      time.sleep(4)
      os.system("cls")
      from old.room2 import room_2
      room_2(name)
    elif door == "2":
      time.sleep(4)
      os.system("cls")
      
    return(help_tung)

def room_4 (name , been_here):
    print(f"Hej {name} du är nu i vardagsrummeto  (Rum 4)")
    time.sleep(2)
    print("när du kommer in i vardahsrummet ser du din kompis tralalero tralala")
    time.sleep(2)
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⡟
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢟⣝⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡟⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣴⣭⣝⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⡞⣛⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⣮⣽⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⢷⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⣖⣋⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣻⡷⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⡿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣠⣶⣿⣷⢾⣿⣿⣿⣿⣿⣛⣿⢿⣿⣿⣿⣿⣿⣿⣽⣿⣿⠛⣿⣿⣿⣿⣿⣿⣷⡄⠉⢳⣦⣀⠀⠀⠀⠀⢀⡄⠀⠀⠀⢀⣾⣟⣿⠁⠀⠀⠀⠀
⠀⠀⢀⣠⣴⣾⣿⢿⣭⣉⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⠿⣿⢿⢻⣿⣿⣿⣷⣿⣿⡀⣯⢙⡻⣿⣿⣦⡈⣙⣿⣶⣤⣀⣤⣾⡁⠀⢀⣀⣾⣿⣿⡏⠀⠀⠀⠀⠀
⠰⠿⣿⡿⠿⣟⠻⣶⠉⠿⠟⠉⢉⣉⣤⠤⠶⠶⢤⠀⡀⠙⢀⡈⠎⠊⠃⢻⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣧⣼⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠃⢻⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠻⠛⠛⠿⠥⠤⠶⠖⠊⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠀⠀⢿⠛⠿⣿⣿⣿⢿⡇⠀⠈⠉⠉⠻⠿⣷⣿⣿⣉⠻⡿⢛⣹⠟⠛⠳⣤⣿⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠲⠶⠶⠤⠤⠤⣤⠀⠀⠀⠀⠀⠀⠀⠈⠛⠷⣶⡾⣿⣿⣾⣻⣦⡀⠤⢄⣰⣂⣈⣿⣿⣿⣦⡙⠻⢧⠀⠀⠀⠉⡻⢿⠤⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠂⠰⢦⣤⠽⠦⢤⣄⣀⣀⣀⣀⣲⣿⣿⣷⣹⣧⡙⠿⠿⣿⣿⠋⠛⠺⣿⡿⢷⣾⣇⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠀⠀⡼⠃⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⢹⣿⣿⣿⣧⡀⠀⠈⠛⠀⠀⠀⣽⣿⣿⣏⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣤⣾⠇⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣧⠀⠀⠀⠀⠀⠺⢻⣿⣿⣧⣽⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡿⣿⣾⣰⢿⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣟⣿⠂⠀⠀⠀⠾⢿⣿⣿⡿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡀⢈⣿⡿⣫⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣧⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠟⢹⡇⠻⣫⣽⡿⢟⣛⣻⡀⠀⠀⠀⠀⠀⠀⣼⣿⠛⠻⢿⣿⣿⣿⡿⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⡾⠛⠁⣠⣼⢿⣿⣵⡤⠴⠚⠋⠉⠀⠀⠀⠀⠀⢀⡴⠯⣌⠻⠿⢮⡭⣸⣿⣧⢾⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⢿⣿⣿⣿⡿⠭⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠛⠀⣀⠀⢀⣼⣿⣿⣿⠟⣡⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⠀⠀⠀⠀⣼⠃⠛⠛⣡⣾⠟⢛⡁⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠞⣹⡇⢀⠉⠀⠀⠀⢸⣷⣴⠞⠉⢀⣠⡿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣄⣾⡿⠷⠟⠋⠀⠀⢀⣀⣠⣶⠾⣋⣡⡶⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣶⣶⣶⣶⣶⣛⣋⣉⣩⠶⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀
""")
    while True:
        time.sleep(2)
        help = input("Skulle du kunna hjälpa mig med en sak? J/N\n").upper()
        time.sleep(2)
        if help == "J":
            print("det är en gåta jag tänker på. Vilken pokemon är det som är gul med röda kinder som Ash har?")
            time.sleep(2)
            while True:
                print("Jag tror att det kan vara pikachu, Charizard eller bulbasaur")
                time.sleep(2)
                pokemon = input().lower()
                if pokemon == "pikachu":
                    print(f"Tack så mycket {name} det var rätt")
                    time.sleep(2)
                    print(f"DU har nu hjälp tralalero tralala")
                    help_tralalero = 1
                    time.sleep(2)
                    break
                elif not pokemon == "pikachu":
                    print("Det var inte rätt försök igen")
                    time.sleep(2)
            break
        elif help =="N":
            print("oh ok")
            help_tralalero = 0
            break
        else:
            print("Du skrev fel skriv J/N tack")
            time.sleep(2)
    print("nu efter du har pratat med personen ser du 2 dörrar")
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
    print("Dörr 1 Går tillbaka till Hallen")
    time.sleep(2)
    print("Dörr 2 Går till nästa rum")
    door = input("vilken dörr vill du gå in i\n")
    if door == "1":
      time.sleep(4)
      os.system("cls")
      from old.room2 import room_2
      room_2(name)
    elif door == "2":
      time.sleep(4)
      os.system("cls")
    return(help_tralalero )