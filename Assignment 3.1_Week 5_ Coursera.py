hrs = input("Enter Hours :")
hrs = float(hrs)
rate = input("Enter rate for hours up to 40 hours: ")
rate = float(rate)
if (hrs <= 40):
    Gross_Pay = hrs * rate
    print(Gross_Pay)
if (hrs > 40):
    Gross_Pay = (rate * 40) + (hrs - 40) * (rate * 1.5)
    print(Gross_Pay)

