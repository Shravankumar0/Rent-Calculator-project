Rent = int(input("Enter the Total rent :"))
Food = int(input("Enter the Amount of food ordered :"))
Electricity_bill =int(input("Enter the total of electricity spend :"))
Charge_per_units = int(input("Enter tye charge per unit :"))
persons = int(input("Enter the number of person living in room :"))

total_bill = Electricity_bill * Charge_per_units

output = (Rent + Food + total_bill) // 4

print(output)