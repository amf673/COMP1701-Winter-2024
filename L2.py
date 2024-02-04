# 
# L2 CoMP 1701 
# Al Fedeoruk 
#
import math

PAPER_THICKNESS = 0.05 # thickness of a typical sheet of paper in mm

# Question 1 Compound Interest Calculation 

# input
initial_investment = float(input("Enter the initial value of the investment: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the number of years to invest: "))

# processing 
investment_value = initial_investment * (1 + rate)**time

# output note the line continuation \ 
print("An investment of", initial_investment, "at", rate * 100, \
      "% will be worth", round(investment_value,2), "after", time, "years.")


# Question 2 Paper folding

f = int(input("Enter the number of folds (>0): "))

thickness = PAPER_THICKNESS * 2**f

thickness_meters = thickness / 1000 # convent to m, 1m = 1000 mm 

print("A paper", PAPER_THICKNESS, "mm thick if folded ", f, "times, would be ", thickness, "m thick.")

# Question 3 Doubling Times 

r = float(input("Enter the growth rate in percent: "))

doubling_time = 70 / r 
exact_doubling_time = (math.log(2) / math.log(1+(r/100)))

print("At a growth rate of ", r, "doubling occurs in approximately", \
       round(doubling_time,2), "and exactly ", round(exact_doubling_time,2))
print("The difference is ", exact_doubling_time - doubling_time)


