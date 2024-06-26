import requests
from bs4 import BeautifulSoup
from recipe_scrapers import scrape_me
import time
import random as rd

import webbrowser
def isPresent(myList, food, submit):
    for item in myList.ingredients():
        if food in item:
            return True
    try:
        submit.append([myList.title(), myList.site_name(),myList.canonical_url()])
        
#        choice = input(f"Recipe without {food} found. Open?")
#        if choice == 'y':
#            webbrowser.open(myList.canonical_url(), new=2)
#        else:
#            print("End")
#        return False
    except:
        return True
def scrape_google_search_results(query, num_results):
    url = f"https://www.google.com/search?q={query}&num={num_results}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    search_results = soup.select("div.g")

    urls = []
    for result in search_results:
        link = result.select_one("a")
        if link:
            try:
                url = scrape_me(link["href"])
                if url.title() is not None:
                    #urls.append(url)
                    print(url.title())
                    try:
                        with open("pizza_cheesecake_casserole.txt", "a") as f:
                            f.write(f"{url.title()}\n")
                            for j in url.instructions().split('. '):
                                f.write(f"{j}\n")
                            for k in url.ingredients():
                                f.write(f"{k}\n")
                    except Exception as e:
                        print(e)
                        print("Could not write to file")
                        continue
                    time.sleep(rd.randint(2,5))
            except Exception as e:
                print(e)
                print("Denied")
                time.sleep(rd.uniform(2,5))
                continue

    return urls

#query -> get food from user using input -> font color = red
#query = input("Enter food: ")   
num_results = 500
similarRecipes = []
submit = []
c = 0
while True:
    try:
        similarRecipes = scrape_google_search_results('"recipe" (pizza OR cheesecake OR casserole) site:allrecipes.com OR site:foodnetwork.com OR site:bbcgoodfood.com OR site:delish.com OR site:epicurious.com OR site:tasteofhome.com OR site:seriouseats.com OR site:marthastewart.com OR site:bonappetit.com OR site:myrecipes.com', num_results)
        c += 1
    except Exception as e:
        print("Server down :(")
        print(e)
        time.sleep(60)
        continue
    if c == num_results: break
    
"""
for i in similarRecipes:
    try:
        with open("egg_sandwich.txt", "a") as f:
            print(i.ingredients())
            print(i.instructions())
            f.write(f"{i.title()}\n")
            for j in i.ingredients():
                f.write(f"{j}\n")
            for k in i.instructions().split('. '):
                f.write(f"{k}\n")
            print("done!")

    except Exception as e:
        print(e)
        print("Error")
        continue
#foodConstraint = input("Foods to avoid: ")

print("Recommendation Conceptual Demonstration")
#inputRecipe = scrape_me(input())
#for i in inputRecipe.ingredients():
#    if foodConstraint in i:
#        print(foodConstraint.capitalize() + " found in the recipe " + inputRecipe.title())
print("Search alternative recipes: ")
#similarRecipes = [scrape_me("https://www.allrecipes.com/recipe/17981/one-bowl-chocolate-cake-iii/"), scrape_me("https://www.foodnetwork.com/recipes/food-network-kitchen/basic-chocolate-cake-recipe-2120876"), scrape_me("https://handletheheat.com/best-chocolate-cake/"), scrape_me("https://www.indianhealthyrecipes.com/eggless-chocolate-cake-moist-and-soft/#Ingredients_and_substitutions"), scrape_me("https://www.mybakingaddiction.com/eggless-chocolate-cake/")]

state = 0
for i in similarRecipes:
    
    for j in i.ingredients():
        if foodConstraint in j:
            state = 1
            break
    if state == 1:
        print(foodConstraint + " in " + i.title() + " from " + i.site_name())
    else:
        print(foodConstraint + " not in " + i.title() + "from" + i.site_name())
    
    try:
        a = isPresent(i, foodConstraint, submit)
    except:
        print("oops")
        continue
for i in submit:
    print(i[0]) 
    print(i[1])
    print(i[2])
    print('-------------------------')
"""


print("End")
