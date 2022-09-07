dollars_input_str = input("# of dollars: ")
cents_input_str = input("# of cents: ")

dollars_input_int = int(dollars_input_str)
cents_input_int= int(cents_input_str)

quarters_num = dollars_input_int * 4
dimes_num = 0
nickels_num = 0
pennies_num = 0

while(cents_input_int >= 25):
    quarters_num = quarters_num + 1
    cents_input_int = cents_input_int - 25


while(cents_input_int >= 10):
    dimes_num = dimes_num + 1
    cents_input_int = cents_input_int - 10

while(cents_input_int >= 5):
    nickels_num = nickels_num + 1
    cents_input_int = cents_input_int - 5


while(cents_input_int >= 1):
    pennies_num = pennies_num + 1
    cents_input_int = cents_input_int - 1


print(f" The coins are  {quarters_num} quarters ,  {dimes_num} dimes ,  {nickels_num} nickels and {pennies_num} pennies")
