#Bryan Apodaca
#1187525
#Homework 5 Problem Set 1
#This program calculates and displays the loan for buying a car

class Loan:
    '''Constructor for Loan Class'''
    def __init__(self, years = 0, loanAmount = 0, borrower = 'Default',rate = 0):
        self.__years = years
        self.__loanAmount = loanAmount
        self.__borrower = borrower
        self.__rate = rate
        
    #These are the getter methods for the Loan Class
    def getYears(self):
        return self.__years
        
    def getLoanAmount(self):
        return self.__loanAmount
        
    def getBorrower(self):
        return self.__borrower
        
    def getRate(self):
        return self.__rate

    #These are the setter methods for the Loan Class
    def setYears(self,years):
        self.__years = years
        
    def setLoanAmount(self,loanAmount):
        self.__loanAmount = loanAmount
        
    def setBorrower(self,borrower):
        self.__borrower = borrower
        
    def setRate(self,rate):
        self.__rate = rate
        
    #Loan Class Methods
    def getMonthlyPayment(self)->float:
        '''Calculates and returns the monthly payment for the loan class'''
        monthlyInterestRate = self.__rate / 1200
        monthlyPayment = self.__loanAmount*monthlyInterestRate/ \
                         (1-(1/(1+monthlyInterestRate)**(self.__years*12)))
        return monthlyPayment

    def getTotalPayment(self)->float:
        '''calculates and returns the total amount of loan for the loan class'''
        totalPayment = self.getMonthlyPayment()*self.__years*12
        return totalPayment

def main():
    annualRate = float(input('Enter yearly interest rate: '))
    years = int(input('Enter number of years as an integer: '))
    loanAmount = float(input('Enter loan amount: '))
    borrowerName = input("Enter a borrower's name: ")
    newLoan = Loan(years,loanAmount,borrowerName,annualRate)
    print("The loan is for",newLoan.getBorrower())
    print("The monthly payment is",format(newLoan.getMonthlyPayment(),',.2f'))
    print("The total payment is",format(newLoan.getTotalPayment(),',.2f'))
    print()
    print('Do you want to change the loan amount? Y for yes or enter to quit')
    answer = input()

    while answer.upper() == 'Y':
        newAmount = float(input('Enter new loan amount: '))
        newLoan.setLoanAmount(newAmount)
        print("The loan is for",newLoan.getBorrower())
        print("The monthly payment is",format(newLoan.getMonthlyPayment(),',.2f'))
        print("The total payment is",format(newLoan.getTotalPayment(),',.2f'))
        print()
        print('Do you want to change the loan amount? Y for yes or enter to quit')
        answer = input()

if __name__ == "__main__":
    main()

#Test Run 1
#Enter yearly interest rate: 2.5
#Enter number of years as an integer: 5
#Enter loan amount: 1000.00
#Enter a borrower's name: John Jones
#The loan is for John Jones
#The monthly payment is 17.75
#The total payment is 1,064.84
#
#Do you want to change the loan amount? Y for yes or enter to quit
#y
#Enter new loan amount: 5000
#The loan is for John Jones
#The monthly payment is 88.74
#The total payment is 5,324.21
#
#Do you want to change the loan amount? Y for yes or enter to quit
#
#>>>

#Test Run 2
#Enter yearly interest rate: 3.2
#Enter number of years as an integer: 10
#Enter loan amount: 21000
#Enter a borrower's name: Bryan
#The loan is for Bryan
#The monthly payment is 204.72
#The total payment is 24,566.65
#
#Do you want to change the loan amount? Y for yes or enter to quit
#y
#Enter new loan amount: 12.23
#The loan is for Bryan
#The monthly payment is 0.12
#The total payment is 14.31
#
#Do you want to change the loan amount? Y for yes or enter to quit
#
#>>> 

#Test Run 3
#Enter yearly interest rate: 5.6
#Enter number of years as an integer: 5
#Enter loan amount: 10000
#Enter a borrower's name: Shanni
#The loan is for Shanni
#The monthly payment is 191.47
#The total payment is 11,488.41
#
#Do you want to change the loan amount? Y for yes or enter to quit
#
#>>>

#Test Run 4
#Enter yearly interest rate: 17.99
#Enter number of years as an integer: 5
#Enter loan amount: 9999
#Enter a borrower's name: Irving
#The loan is for Irving
#The monthly payment is 253.85
#The total payment is 15,231.27
#
#Do you want to change the loan amount? Y for yes or enter to quit
#y
#Enter new loan amount: 12356
#The loan is for Irving
#The monthly payment is 313.69
#The total payment is 18,821.64
#
#Do you want to change the loan amount? Y for yes or enter to quit
#
#>>>

#Test Run 5
#Enter yearly interest rate: 7.2
#Enter number of years as an integer: 35
#Enter loan amount: 450000
#Enter a borrower's name: Lolly
#The loan is for Lolly
#The monthly payment is 2,938.19
#The total payment is 1,234,040.92
#
#Do you want to change the loan amount? Y for yes or enter to quit
#y
#Enter new loan amount: 200000
#The loan is for Lolly
#The monthly payment is 1,305.86
#The total payment is 548,462.63
#
#Do you want to change the loan amount? Y for yes or enter to quit
#
#>>> 
