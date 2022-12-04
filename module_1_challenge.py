# Part 1.2 Automate the Calculations

# list of costs associated to loans
loan_costs = [500, 600, 200, 1000, 450]
# count the number of loans in list
number_of_loans = len(loan_costs)
# add all loans together to come up with total sum of loans
sum_of_loans = sum(loan_costs)
# Average loan price = Sum of Loans / Number of Loans
average_loan_price = sum_of_loans * number_of_loans

# Shows the value of all loans combined
print("The sum of all loans is:$",sum_of_loans)
# Shows the total number of loans in the portfolio
print("The total number of loans is:",number_of_loans)
# Shows the price of the average loan
print("The average loan price is:$",average_loan_price)



