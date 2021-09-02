initial_amount = float(input("Enter the initial amount: ")) # Do not change this line
interest = float(input("Enter the interest(%): ")) # Do not change this line
years = int(input("Enter for how many years: ")) # Do not change this line
interest_percent = float(interest * 0.01)
current_amount = float(initial_amount)
for i in (0, years,1) : 
    if years != 0 :
        current_amount = current_amount + (current_amount * (interest * 0.01))

print(f"Amount after {years} years: {round(current_amount, 2)}")