class SalaryEngine:
    def __init__(self, salary, tax, deduction, bonus):
        self.salary = salary
        self.tax = tax
        self.deduction = deduction
        self.bonus = bonus

    def calculate(self):
        if self.salary < 0:
            return "Invalid: Salary cannot be negative"

        if self.tax < 0:
            return "Invalid: Tax cannot be negative"

        if self.deduction < 0:
            return "Invalid: Deduction cannot be negative"

        if self.bonus < 0:
            return "Invalid: Bonus cannot be negative"

        if self.salary == 0:
            return "Salary is zero"

        tax_amount = self.salary * self.tax / 100
        final_salary = self.salary - tax_amount - self.deduction + self.bonus

        return final_salary


salary = float(input("Enter salary: "))
tax = float(input("Enter tax percentage: "))
deduction = float(input("Enter deduction: "))
bonus = float(input("Enter bonus: "))

obj = SalaryEngine(salary, tax, deduction, bonus)

print("Final Salary:", obj.calculate())