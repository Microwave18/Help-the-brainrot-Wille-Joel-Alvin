import time


def rules():
    return(print("Du kommer spela som dig själv där ditt mål är att hjälpa så många av dina kompisar som möjligt ifall du kan någon fråga kan du skippa den finns ingen tids gräns så ha inte brottem lycka till "))

def get_data():
    print("Välkomen till vårat spel")
    print("Har du spleat förut?")
    while True:
        rules = input("J/N").upper()
        if rules == "J":
            pass
            break
        elif rules =="N":
            rules()
            time.sleep(5)
            break
        else:
            print("Du skrev inte rätt skriv om tack")
        
    name = input("Vad heter du?\n")
    return(name)

def six_seven(name):
    print(f"Hej {name} skulle du kunna hjälpa mig med något?")
    help = input ("J/N\n").upper()
    if help == "J":
        help_six_seven = True
        while True:
            print("Jag tänkte gå och spela fotboll ifall det tar 30 minuter att gå till fotbollsplan och jag spelar 37 minuter hur många minuter har jag varit ute?")
            question = input("")
            if question == "67":
                print(f"Tack så mycket för hjälpen {name}")
                break
            else: 
                print("Tror inte det blir det?")
                print("försök igen")
    elif help == "N":
        help_six_seven = False
        print(f"jaha jag förstår hej då då hoppas vi syns sen {name}")
    return(help_six_seven)
        
        
name = get_data()
#help_six_seven = six_seven(name)
#if help_six_seven == True:
#    print("Du har hjälp Six Seven")
#elif help_six_seven == False: 
#    print("Du hjälpte inte Six Seven")
#else:
#    print("ERROR")
    