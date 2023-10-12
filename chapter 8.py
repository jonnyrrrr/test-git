brands = ['Nike', 'Addidas','Puma', 'Vans' ]
grocceries = ['bread', 'toothpaste', 'apples']

def brand_adder(thing_to_add, target_list):
    if target_list[0].lower() in 'abcdefg':
        print('this brand stars with A-G')
        target_list.append(thing_to_add)

    else:
        print('this brand starts with H-Z')

    for item in target_list:
        if len(item) <= 5:
            brands.remove(item)
            print(f'{item} was not added because it has too few characters')

brand_adder('Nike', brands)
brand_adder('Puma', brands)
brand_adder('coffee', grocceries)
brand_adder('milk', grocceries)

print(brands)
print(grocceries)