#q1
def overtime_salary(hourly_rate,hours_worked_per_week):
    if(hours_worked_per_week>40):
     return 1.5*hourly_rate*(hours_worked_per_week-40)*4
    return 0

def basic_salary(hourly_rate,hours_worked_per_week):
    if(hours_worked_per_week>40):
     return hourly_rate*40*4
    else:
        return hourly_rate*hours_worked_per_week*4


def total_salary(hourly_rate,hours_worked_per_week):
   #print("Basic Salary:",basic_salary(hourly_rate,hours_worked_per_week))
   #print("Overtime Salary:",overtime_salary(hourly_rate,hours_worked_per_week))   
   return  basic_salary(hourly_rate,hours_worked_per_week)+overtime_salary(hourly_rate,hours_worked_per_week)
#q2
def tax_amount(basic_sal):
    if(basic_sal<=60000):
        tax=.10*basic_sal
    elif(basic_sal<=85000):
        tax=.15*basic_sal
    else:
        tax=.20*basic_sal
    return tax
#q3
def gross_salary(basic_salary):
   allowance=.20*basic_salary
   tax=tax_amount(basic_salary)
   return basic_salary+allowance-tax
#q4
def salary_bracket(gross_sal):
   if(gross_sal<50000):
      print("Salary Bracket:low income")
   elif(gross_sal<80000):
      print("Salary Bracket:middle income")
   else:
      print("Salary Bracket:high income")   
#q5
def employee_report(employee_names,hourlyrates,hrsWorkedPerWeek):
 for i in range(len(employee_names)):
  Total_Salary=total_salary(hourlyrates[i],hrsWorkedPerWeek[i])
  #print("Total_salary:",Total_Salary)
  basic_sal=basic_salary(hourlyrates[i],hrsWorkedPerWeek[i])
  #print("Basic Salary:",basic_salary)
  tax=tax_amount(basic_sal)
  #print("Tax:",tax)
  gross_sal=gross_salary(basic_sal)
  #print(gross_sal)
  print("Employee name:",employee_names[i],"\nTotal Salary:",Total_Salary ,"\n","Basic Salary:",basic_sal,"\n","Tax:",tax,"\n","Salary_Brackey:",salary_bracket(gross_sal),"\n")


emp_names=eval(input("enter list of employee names of length3:"))
h_rate=eval(input("enter list of hourly_rate of length 3:"))
h_worked=eval(input("enter list hours worked of length 3:"))
employee_report(emp_names,h_rate,h_worked)      
    
#i/p:-h_rate=10  ; h_worked=41

