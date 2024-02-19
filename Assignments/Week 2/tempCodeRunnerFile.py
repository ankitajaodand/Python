salary=float(input("Enter Salary "))
def salaryIncrement(salary:float): 
    if salary <= 10000: 
        incr=5
    elif salary > 10000 and salary >= 20000: 
        incr=10
    elif salary > 20000 and salary >= 50000: 
        incr=15
    else: 
        incr=20    
    updated_salary=salary+salary*(incr/100)  
    print(f"updated_salary: {updated_salary}")

salaryIncrement(salary)      
    