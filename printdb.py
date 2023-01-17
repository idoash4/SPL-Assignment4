from persistence import *

EMPLOYEES_REPORT_QUERY = """
SELECT employees.name, employees.salary, branches.location, 
COALESCE(SUM(-activities.quantity * products.price), 0) as sales_income
FROM employees
LEFT JOIN branches ON branches.id = employees.branche
LEFT JOIN (activities LEFT JOIN products ON products.id = activities.product_id)
ON employees.id = activities.activator_id
GROUP by employees.id
ORDER BY employees.name
"""

ACTIVITIES_REPORT_QUERY = """
SELECT activities.date, products.description, activities.quantity, employees.name, suppliers.name
FROM activities
LEFT JOIN products ON products.id = activities.product_id
LEFT JOIN employees ON employees.id = activities.activator_id
LEFT JOIN suppliers ON suppliers.id = activities.activator_id
ORDER BY activities.date
"""


def main():
    print("Activities")
    print(*repo.activities.find_all(), sep='\n')
    print("Branches")
    print(*repo.branches.find_all(), sep='\n')
    print("Employees")
    print(*repo.employees.find_all(), sep='\n')
    print("Products")
    print(*repo.products.find_all(), sep='\n')
    print("Suppliers")
    print(*repo.suppliers.find_all(), sep='\n')

    print("\nEmployees report")
    for line in repo.execute_command(EMPLOYEES_REPORT_QUERY):
        print(' '.join(map(lambda item: str(item) if not isinstance(item, bytes) else item.decode('utf-8'), line)))

    print("\nActivities report")
    for line in repo.execute_command(ACTIVITIES_REPORT_QUERY):
        print(tuple([str(item) if not isinstance(item, bytes) else item.decode('utf-8') for item in line]))


if __name__ == '__main__':
    main()
