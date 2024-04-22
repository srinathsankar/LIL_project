import csv
celiac = "flour, soy sauce, beer, breadcrumbs, bread, wheat, barbecue sauce, yeast, mustard, wheat flour, farina, triticale".split(", ")
lactose = "milk, cheese, butter, yogurt, ice cream, buttermilk, sour cream, cheese, cheesy, waffle, pancake, muffin, cake, cake mix, cereal, hot dog, bacon, sausage, cold cut".split(", ")
diabetes = "white sugar, brown sugar, sugar, honey, agave, maple syrup, corn syrup, fructose corn syrup, white flour, white rice, instant oatmeal, margarine, syrup, chocolate, sweetened yogurt".split(", ")

print(celiac)
print(lactose)
print(diabetes)
with open('tag.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Food", "Tag"]
    writer.writerow(field)
    for i in celiac:
        writer.writerow([i, "celiac"])
    for i in lactose:
        writer.writerow([i, "lactose"])
    for i in diabetes:
        writer.writerow([i, "diabetes"])
    
