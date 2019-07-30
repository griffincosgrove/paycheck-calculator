#Client name: Laura Atkins
#Programmer name: Griffin Cosgrove
#PA purpose: Program to determine net pay check of employees and provide new access codes.
#My submission of this program indicates that I have neither received nor given unauthorized assistance in writing this program

#Creating the prompts for the user to input their information
s1=input("Enter employee name (first last):")
no1=eval(input("Enter number of hours worked this last week:"))
no2=eval(input("Enter hourly pay rate:"))
s2=input("Enter Single or married (s or m):")
no3=eval(input("Enter state tax witholding rate (as a decimal):"))

#formula for gross pay
pay=no1*no2
#formula for state witholding deduction.
no4=no3*pay

#conditional for applying the single or married tax rate.
if s2=="s":
    witholding=.15*pay
if s2=="m":
    witholding=.1*pay

#formula for total deductions
no5=witholding+no4

#Creating the access code
y=len(s1)//3

#displaying the information the user entered and calculating and gross pay and deductions.
#displaying the access code
print(("\nEmployee Name:"),s1)
print(("\nHours Worked:"), no1)
print(("Pay Rate"),no2)
print("Gross Pay: ",format(pay,',.2f'),sep='$')
print("Deductions:")
print("\tFederal Witholding: ",format(witholding,',.2f'),sep='$')
print("\tState Witholding: ",format(no4,',.2f'),sep='$')
print("\tTotal Deduction: ",format(no5,',.2f'),sep='$')
print(("\nYour new access code is:"),s1[y:7],s1.upper()[-3:],min(s1),max(s1))
