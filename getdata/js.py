import pandas as pd
import time
import re
import json
table = pd.read_csv('tag.csv')
js = {}
rowset = set()
js['classes'] = []
js['annotations'] = []
for index,row in table.iterrows():
    rowset.add(row['Tag'].upper())
js['classes'].append(list(rowset))

print(js)
print(table)
with open('pizza_cheesecake_casserole.txt', 'r', newline='', encoding = 'utf-8') as file:
    for i in file:
        try:
            #print(i)
            li = [i, {"entities":[]}]
            print(li[1]['entities'])
            #time.sleep(1)
            #print(js)
            for index, row in table.iterrows():
                print(row['Food'],i.lower())
                #time.sleep(1)
                if row['Food'] == 'sugar':
                    #time.sleep(1)
                    if row['Food'] in i:
                        print("yes")
                        #time.sleep(1)
                
                if row['Food'] in i:
                    print("yes")
                    #print(js)
                    #time.sleep(1)
                    
                    for m in re.finditer(row['Food'], i.lower()):
                        print(m.start(),m.end())
                        #time.sleep(1)
                        
                        print(i)
                        #time.sleep(3)
                        li[1]["entities"].append([m.start(),m.end(),row['Tag'].upper()])
                        print(li[1])
                        #time.sleep(1)
                        if li[1]["entities"] and li[1]["entities"][2] != 'LACTOSE':
                            print(li[1]["entities"])
                            #time.sleep(2)
                    #indices[(m.start(),m.end()) for m in re.finditer(row['Food'], i.lower())])
                    print(li)
                    #time.sleep(5)
            
            #time.sleep(2)
            js['annotations'].append(li)
            if li[1]["entities"]:
                print(js)
                #time.sleep(3)
            #print(js)
            #time.sleep(4)
        except:
            continue
js_object = json.dumps(dictionary, indent=4)
 
# Writing to sample.js
with open("sample.json", "w") as outfile:
    outfile.write(js_object)
