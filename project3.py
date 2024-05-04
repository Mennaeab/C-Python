n = int(input())

for i in range(n):
    first_name = input("enter first name of the employee: ")
    no_of_work_hour = int(input("enter no of woking hour should be in between 30 to 40: "))
    pay_rate = float(input("enter pay rate of the employee per hour should be in between 10.25 to 30.50: "))
    fedral_tax = .15 #float(input())
    social_security = .17 #float(input())
    gross_pay = pay_rate*no_of_work_hour
    fedral_deduction = gross_pay*fedral_tax
    social_security_deduction = gross_pay*social_security
    net_pay = gross_pay - fedral_deduction-social_security_deduction

print(f"{first_name} is work for {no_of_work_hour} of a pay rate {pay_rate} and his gross income is {gross_pay} and fedral taxes is {fedral_deduction} and social security is {social_security_deduction} and his net income is {net_pay}")
