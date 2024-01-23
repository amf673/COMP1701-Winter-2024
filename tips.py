# 
# Tip Calculator 
#
# A. Fedoruk
# 

TIP_RATE = 0.02 

total_sales = float(input("Enter the total sales: "))
employees = int(input("Enter the number of employees: "))

total_tips = total_sales * TIP_RATE
employee_tips = total_tips / employees

print("Total Sales: $", round(total_sales,2), " Each employee recieves: $", round(employee_tips,2), sep="")