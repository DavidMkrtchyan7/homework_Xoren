def century(n):
    return (n+99)//100
while True:
    year = int(input("Enter the year  "))
    if not year:
        print("False")
        break
    print("Year: %s  Century: %s" % (year, century(year)))