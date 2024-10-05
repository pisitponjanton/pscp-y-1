"""ProgressiveTax"""
def main():
    """ProgressiveTax"""
    tax = int(input())
    if tax <= 150000:
        tax = 0
    elif 150000<tax<=300000:
        tax = (tax - 150000)*(5/100)
    elif 300000<tax<=500000:
        tax = (tax - 300000)*(10/100) + 7500
    elif 500000<tax<=750000:
        tax = (tax - 500000)*(15/100) + 7500 + 20000
    elif 750000<tax<=1000000:
        tax = (tax - 750000)*(20/100) + 7500 + 20000 + 37500
    elif 1000000<tax<=2000000:
        tax = (tax - 1000000)*(25/100) + 7500 + 20000 + 37500 + 50000
    elif 2000000<tax<=4000000:
        tax = (tax - 2000000)*(30/100) + 7500 + 20000 + 37500 + 50000 + 250000
    elif tax>4000000:
        tax = (tax - 4000000)*(35/100) + 7500 + 20000 + 37500 + 50000 + 250000 + 600000
    print(int(tax))
main()
