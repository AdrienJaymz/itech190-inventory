'''
We have an issue at our company. 
We have a massive amount of inventory and like always, management never took records.
Luckily for us, they do have a spreadsheet with everything.  They just don't know how to use it.

We have been tasked with generating some reports for them
1) total number of items they have
2) how many of each type of item we have (Laptops, Tablets, Phones)
3) How many laptops we have that are over 7 years old (they need to be replaced)
'''

import csv

def get_data(file_path:str)->list:
    data=[]
    with open(file_path, mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)
    return data

def get_num_items(data:list)->int:
    return len(data)

def get_categories(data:list)->dict:
    categories ={}
     
    for item in data:
        category =item.get('category')
        if categories.get(category) is None:
            categories[category] = 0

        categories[category] +=1

    return categories

def main():
    file_path:str = "inventory.csv"
    data:list = get_data(file_path)

    # num_items = get_num_items(data)
    # print(f"total number of items: {num_items}")

    categories = get_categories(data)
    print(f"Laptops: {categories.get('Laptop')}")
    print(f"Tablet: {categories.get('Tablet')}")
    print(f"Phones: {categories.get('Phone')}")

    

if __name__ == "__main__":
    main()