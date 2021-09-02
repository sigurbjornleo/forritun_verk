paper_int = 10
print_int = 150
sales_paper_int = 0
sales_printer_int = 0
sales_confirmed_int = 0
sale_str = " "
print("Welcome to Dunder Mifflin!")
while sale_str != 'n' :
    sale_str = input("Would you like to add a sale (y/n)?: ")
    if sale_str == 'y' :
        type_str = input("paper or printer: ")
        if type_str == 'paper' :
            amount_str = input("# of paper piles: ")
            amount_int = int(amount_str)
            sales_paper_int = sales_paper_int + paper_int * amount_int
            sales_confirmed_int = sales_confirmed_int + 1
            total_int = int(round((sales_paper_int*0.15) + (sales_printer_int * 0.3),0))
        elif type_str == 'printer' :
            amount_str = input("# of printers: ")
            amount_int = int(amount_str)
            sales_printer_int = sales_printer_int + print_int * amount_int
            sales_confirmed_int = sales_confirmed_int + 1
            total_int = int(round((sales_paper_int*0.15) + (sales_printer_int * 0.3),0))
        else :
            print("You did neither type in paper nor printer")

    elif sale_str == 'n' :
        break
    print("You've made",total_int, 'today with',sales_confirmed_int, 'sales')
