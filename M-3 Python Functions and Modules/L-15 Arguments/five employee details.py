n = int(input("Enter the number of employee's whose details who wish to register : "))
name = ['--']
age = ['--']
exp = ['--']
job = ['--']
for i in range(1,n+1,1) :
    nam = input("Enter the name of the employee : ")
    name.append(nam)
    ag = int(input(f"Enter the age of {nam} : "))
    age.append(ag)
    ex = int(input(f"Enter the number of years of exprience {nam} has : "))
    exp.append(ex)
    jo = input(f"Enter the job title of {nam} : ")
    job.append(jo)
    print("The employee's number is ",i)
empnum = int(input("Enter a employee's number to access their details : "))
print(name[empnum])
print(age[empnum])
print(exp[empnum])
print(job[empnum])
