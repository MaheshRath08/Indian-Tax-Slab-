from asyncio import IncompleteReadError


print("This Tax slab functions according to the new tax rates") #Welcome message

#Define the function 
def taxSlab(income):
    if income <= 250000:
        return "Fully Exempt"
    elif income <= 500000:
        tax = (income - 250000) * 0.05
        return tax
    elif income <= 750000: 
        tax = (income - 500000) * 0.10 + 12500
        return tax
    elif income <= 1000000: 
        tax = (income - 750000) * 0.15 + 37500
        return tax
    elif income <= 1250000: 
        tax = (income - 1000000) * 0.20 + 75000
        return tax
    elif income <= 1500000: 
        tax = (income - 1250000) * 0.25 + 125000
        return tax
    else:
        tax = (income - 1500000) * 0.30 + 187500
        return tax
 
    
try:                
    income = float(input("Your Income:\n"))
    #Call the function here 
    print("Your Income-Tax is", taxSlab(income))
except ValueError:
    print("Make sure type in valid numerical value")      #error hading to intake proper input
    income = float(input("Your Income:\n"))
   

