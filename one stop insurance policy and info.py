# program created to generate and calculate a new insurance policy and it's information for their customers
# Written on: November 20, 2023
# Author: Alexander Condon-Escott

# Import libraries
import datetime
import calendar

# program constants
TodayDate = datetime.date.today()
FirstDayOfMonth = datetime(10,20,2023).replace(day=1)
FirstPayDate = FirstDayOfMonth.replace(Month = FirstDayOfMonth.Month + 1)

HST_RATE = 0.15
PROCESS_FEE = 39.99
GLASS_COVER = 86.00
LIABITLITY_PER_CAR = 130.00
LOANER_OPT_PER_CAR = 58.00
INSURE_PREM_FOR_FIRST_CAR = 869.00
DISCOUNT_FOR_ADDITIONAL_CAR = 0.25


# gather customer inputs 
CustFirstName = input("Enter the first name of the customer: ").capitalize()
CustLastName = input("Enter the last name of the customer: ").capitalize()
StreetAdd = input("Enter the street address of the customer: ")
City = input ("Enter the city of the customer: ")

while True:

 Province = input ("Enter the province of the customer(XX): ").upper
 if Province !=  "NL" and Province != "NS" and Province !="NB" and Province !="PE" and Province != "QC" and Province != "ON" and Province != "MB" and Province != "SK" and Province != "AB" and Province != "BC" and Province != "YT" and Province != "NT" and Province != "NU":
    print ("Province must be one the 13 listed - please re-enter: ")
 else:
     break
Postalcode = input("Enter the postal code of the customer: ").upper()
CustPhoneNum = input("Enter the phone number of the customer: ")
ClaimNum = input("Enter the insurance claim number (XXXXXX): ")
NumCarInsured = int(input("Enter the number of cars that are insured: "))
ExtraLiability = input("would you like extra liability coverage on your cars (Y/N): ").upper()
GlassCover = input("would you like glass coverage on your vechiles (Y/N): ").upper()
LoanerCar = input("Would you like a loaner car (Y/N): ").upper()
PayType = input("How would you like to pay for your insurance (M/F/D): ").upper()


# gather user if statements 
if NumCarInsured > 1:
    InsurancePrem = ((NumCarInsured - 1) * (INSURE_PREM_FOR_FIRST_CAR * DISCOUNT_FOR_ADDITIONAL_CAR)) + INSURE_PREM_FOR_FIRST_CAR 
else:
    InsurancePrem = INSURE_PREM_FOR_FIRST_CAR

if ExtraLiability == "Y":
   ExtraLiability = LIABITLITY_PER_CAR * NumCarInsured
else:
   ExtraLiability = 0


if ExtraLiability > 1000000:
    print("extra liability cannot cover over 1000000 dollars")



if GlassCover == "Y":
    GlassCover = GLASS_COVER * NumCarInsured
else:
    GlassCover = 0


if LoanerCar == "Y":
    LoanerCar = LOANER_OPT_PER_CAR * NumCarInsured
else:
    LoanerCar = 0






# generate program calculations
TotalExtraCost = LIABITLITY_PER_CAR + GLASS_COVER + LOANER_OPT_PER_CAR
TotalInsurePrem = InsurancePrem + TotalExtraCost
Taxes = TotalInsurePrem * HST_RATE
TotalCost = TotalInsurePrem + Taxes


if  PayType == "D":
    DownPay = float(input("Enter the downpayment amount for the insurance: "))
    MonthlyPay = ((TotalCost - DownPay)+ PROCESS_FEE)/8
elif PayType == "M":
    MonthlyPay = MonthlyPay = PROCESS_FEE + TotalCost/ 8 
elif PayType == "F":
    FullPay = PROCESS_FEE + TotalCost
else:
    PayType = "N/A" 
       


#generate program outputs
TodayDateDsp = TodayDate .strftime("%b %d, %Y")
FirstPayDateDsp = FirstPayDate .strftime("%b %d, %Y")
InsurancePremDsp = "${:.2f}" . format(InsurancePrem)
ExtraLiabilityDsp = "${:.2f}" . format(ExtraLiability)
GlassCoverageDsp = "${:.2f}" . format(GlassCover)
LoanerCarDsp = "${:.2f}" . format(LoanerCar)
TotalExtraCostDsp = "${:.2f}" . format(TotalExtraCost)
TotalInsurePremDsp = "${:.2f}" . format(TotalInsurePrem)
TaxesDsp = "${:.2f}" . format(Taxes)
TotalCostDsp = "${:.2f}" . format(TotalCost)
MonthlyPayDsp = "${:.2f}" . format(MonthlyPay)
print(f"")
print(f" One Stop insurance policy and Recipt                                                      Inovice Date:                {TodayDateDsp:<8s}")
print(f"")
print(f" Inurance customer information:                                                            Claim #:                         {ClaimNum:<6s}")
print(f"                                                                                           -----------------------------------------------")
print(f" {CustFirstName:>12s} {CustLastName:>12s}                                                  # of cars:                  {NumCarInsured:<3s}")
print(f" {StreetAdd:>24s}                                                                          Premium Insurance Cost: ${InsurancePremDsp:<7s}")
print(f" {City:>16s} {Province:>2s} {Postalcode:>6s}                                               Extra Liability Cost:  ${ExtraLiabilityDsp:<7s}")
print(f" {CustPhoneNum:>12s}                                                                       Glass Coverage Cost:    ${GlassCoverageDsp:<7s}")
print(f"                                                                                           Loaner Car Cost:            ${LoanerCarDsp:<7s}")
print(f"------------------------------------------------------------------------------------------------------------------------------------------")
print(f"                                                                                           Total Extra Cost:      ${TotalExtraCostDsp:<7s}")
print(f"                                                                                   Total Premium Insurance Cost: ${TotalInsurePremDsp:<7s}")
print(f"                                                                                           Taxes:                          ${TaxesDsp:<7s}")
print(f"------------------------------------------------------------------------------------------------------------------------------------------")
print(f"                                                                                           Total Cost:                 ${TotalCostDsp:<7s}")
print(f"                                                                                           Payment Type:                     {PayType:>1s}")
print(f"------------------------------------------------------------------------------------------------------------------------------------------")
print(f"")
print(f"      Claim #             Claim Date                  Amount paid")
print(f"      1.                 {FirstPayDateDsp:>8s}                   ")
print(f"      2.                                                         ")
print(f"      3.                                                         ")
print(f"      4.                                                         ")
print(f"      5.                                                         ")
print(f"      6.                                                         ")
print(f"      7.                                                         ")
print(f"      8.                                                         ")