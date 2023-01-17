from persistence import *

import sys


def insert_supply_arrival(splittedline : list[str]):
    product_id = int(splittedline[0])
    quantity = int(splittedline[1])
    supplier_id = int(splittedline[2])
    date = splittedline[3]
    # Update product quantity
    product = repo.products.find(id=product_id)[0]
    product.quantity += quantity
    repo.products.insert(product)
    # Save activity to db
    repo.activities.insert(Activitie(product_id, quantity, supplier_id, date))


def insert_sale_activity(splittedline : list[str]):
    product_id = int(splittedline[0])
    quantity = int(splittedline[1])
    employee_id = int(splittedline[2])
    date = splittedline[3]
    # Update product quantity
    product = repo.products.find(id=product_id)[0]
    if product.quantity < quantity:
        # Not enough quantity
        return
    product.quantity += quantity
    repo.products.insert(product)
    # Save activity to db
    repo.activities.insert(Activitie(product_id, quantity, employee_id, date))


def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            quantity = int(splittedline[1])
            if quantity > 0:
                insert_supply_arrival(splittedline)
            else:
                insert_sale_activity(splittedline)


if __name__ == '__main__':
    main(sys.argv)