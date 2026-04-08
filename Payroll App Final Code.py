import time

def slowPrint(text, speed=0.1):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)
    print("")

def n_input(prompt, is_float=False, is_int=False):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("This field cannot be blank. Please try again.")
            continue
        
        if is_float:
            try:
                return float(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif is_int:
            try:
                return int(user_input)
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        else:
            return user_input

def main():
    while True:
        slowPrint("Welcome to the system!")

        employeeName = n_input("Enter Your Fullname (Lastname, Firstname Initial): ")
        baseSalary = n_input("Enter your Base Salary: ", is_float=True)
        hours_Late = n_input("Enter how many hours late: ", is_float=True)
        over_Time = n_input("Enter how many hours overtime: ", is_int=True)
        startDate = n_input("Enter Starting Date (MM-DD-YYYY): ")
        endDate = n_input("Enter End Date (MM-DD-YYYY): ")

        taxDeduction = 0.08
        sss = 0.11
        philHealth = 0.04
        pag_Ibig = 0.01

        deduction_sss = baseSalary * sss
        deduction_philhealth = baseSalary * philHealth
        deduction_pag_ibig = baseSalary * pag_Ibig
        tax_deduction = baseSalary * taxDeduction
        hourly = baseSalary / 28
        hourlyrate = hourly / 12
        overtime = hourlyrate * 0.1
        overtime1 = overtime + hourlyrate
        overtime2 = overtime * over_Time
        hours_late = hourlyrate * hours_Late
        deductions = deduction_sss + deduction_philhealth + deduction_pag_ibig + hours_late + tax_deduction
        netpay1 = baseSalary - deductions
        netpay2 = netpay1 + overtime2

        formated_hourlyrate = f"{hourlyrate:.2f}"
        formated_overtime1 = f"{overtime1:.2f}"
        formated_tax_deduction = f"{tax_deduction:.2f}"
        formated_sss = f"{deduction_sss:.2f}"
        formated_philhealth = f"{deduction_philhealth:.2f}"
        formated_pag_ibig = f"{deduction_pag_ibig:.2f}"
        formated_hourslate = f"{hours_late:.2f}"
        formated_deductions = f"{deductions:.2f}"
        formated_overtime2 = f"{overtime2:.2f}"
        formated_netpay = f"{netpay2:.2f}"

        print("\n" * 3)
        print("Name: ", employeeName)
        print("----------------------------------------------------------------------------------------------------------------------------")
        print("Hourly rate                                                                                                       ", formated_hourlyrate, "PHP")
        print("Overtime rate                                                                                                     ", formated_overtime1, "PHP")
        print("Start Date                                                                                                        ", startDate)
        print("End Date                                                                                                          ", endDate)
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("Deductions")
        print("Tax                                                                                                              ", formated_tax_deduction, "PHP")
        print("SSS                                                                                                              ", formated_sss, "PHP")
        print("PhilHealth                                                                                                       ", formated_philhealth, "PHP")
        print("Pag-ibig                                                                                                         ", formated_pag_ibig, "PHP")
        print("Hours late                                                                                                       ", formated_hourslate, "PHP")
        print("-----------------------------------------------------------------------------------------------------------------------------")
        print("Total Deduction                                                                                                  ", formated_deductions, "PHP")
        print("Overtime                                                                                                         ", formated_overtime2, "PHP")
        print("Netpay                                                                                                           ", formated_netpay, "PHP")
        print("\n" * 2)

        choice = input("Do you want to try again? (yes/no): ").strip().lower()

        if choice != 'yes':
            slowPrint("Exiting the system.")
            break  

main()