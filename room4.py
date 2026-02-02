import time
import os

def room_4 (name , been_here=False):
    print(f"Hej {name} du är nu i vardagsrummet")
    time.sleep(2)
    print("när du kommer in i köket ser du din kompis tralalero tralala")
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
                    time.sleep(2)
                    break
                elif not pokemon == "pikachu":
                    print("Det var inte rätt försök igen")
                    time.sleep(2)
            break
        elif help =="N":
            print("oh ok")
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
      from room2 import room_2
      room_2(name)
    elif door == "2":
      time.sleep(4)
      os.system("cls")