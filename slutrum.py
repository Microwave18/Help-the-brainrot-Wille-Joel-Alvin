import time
import os
def endrum(hjälpt, val):
    print("Du har nu kommit till slutrummet")
    time.sleep(2)
    print("""__________     __________
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
  
    if hjälpt == "0":
        print("Du har hjälp 0/4 brainrots, Du kommer att förlora ifall du avslutar")
    elif hjälpt == "1":
        print("Du har hjälp 1/4 brainrots, Du kan avsluta ifall du vill")
    elif hjälpt == "2":
        print("Du har hjälp 2/4 brainrots, Du kan avsluta ifall du vill")
    elif hjälpt == "3":
        print("Du har hjälp 3/4 brainrots, Du kan avsluta ifall du vill")
    elif hjälpt == "4":
       print("Du har hjälp 4/4 brainrots, Du kan avsluta ifall du vill")
    
    Lista = ["Dörr 1 avslutar spelet", "Dörr 2 så går du tillbaka", "exit"]
    for item in Lista:
        print(item)
    while True:
        if val.lower == "Dörr 1":
            print("Du har avslutat spelet")
        elif val.lower == "Dörr 2":
            print("du går tillbaka")
        elif val.lower == "exit":
            print("är du säker att du vill avsluta spelet?")
        else:
            print("Du har valt något, testa igen")
