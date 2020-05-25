from bs4 import BeautifulSoup
import requests
from datetime import date

def main():
    
    print("\n" + str(date.today()) + "\n")

    Jester = requests.get("http://hf-food.austin.utexas.edu/foodpro/shortmenu.aspx?sName=University+Housing+and+Dining&locationNum=12&locationName=Jester+2nd+Floor+(J2)+Dining&naFlag=1")
    Kins = requests.get("http://hf-food.austin.utexas.edu/foodpro/shortmenu.aspx?sName=University+Housing+and+Dining&locationNum=03&locationName=Kinsolving+Dining&naFlag=1")

    #print(J2Menu.status_code)
    def Salad_Detector(menu):

        src = menu.content
        soup = BeautifulSoup(src, 'lxml')
        items = soup.find_all("div", class_="shortmenurecipes")

        for item in items:
            item = item.text
            if "Fiesta Salad" in item:
                return True
            return False


    diningHalls = [[Jester,"J2"],[Kins,"Kins"]]
    for menu, hall in diningHalls:
        if Salad_Detector(menu) == True:
            print("They have bomb ass salads at", hall, "today")
        else:
            print(hall, "is dead to me")

    input("\nPress [ENTER] to exit...")

main()
