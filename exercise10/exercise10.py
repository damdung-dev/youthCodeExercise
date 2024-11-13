"""The Canadian Social Insurance Number (SIN) is a 9-digit number, which is checked for validity as follows:
- The rightmost digit (position 1, counting from right to left) is the check digit.
- The weight is calculated from right to left (excluding the check digit), equal to s1 + s2:
+ s1 is the sum of the odd-positioned digits.
+ The even-positioned digits are doubled. If the result of the doubling has two digits, the result is
the sum of these two digits. s2 is the sum of the results.

A valid SIN has a weighted sum with the check digit that is divisible by 10."""

sin=int(input("Enter a number has 9 digits: "))
if sin//1000000000==0:
    print("You have entered enough sin")
    check_digit=sin%10
    s11=sin%100//10
    s12=sin%1000//100
    s13=sin%10000//1000
    s14=sin%100000//10000
    s15=sin%1000000//100000
    s16=sin%10000000//1000000
    s17=sin%100000000//10000000
    s18=sin%1000000000//100000000
    s1=s18+s16+s14+s12
    s171=(s17*2)//10
    s172=(s17*2)%10
    s151=(s15*2)//10
    s152=(s15*2)%10
    s131=(s13*2)//10
    s132=(s13*2)%10
    s111=(s11*2)//10
    s112=(s11*2)%10
    s2=s171+s172+s151+s152+s131+s132+s111+s112
    if(s1+s2+check_digit)%10==0:
        print("Valid SIN number")
    else:
        print("Invalid SIN number")
elif sin==0:
    exit
else:
    print("Missing number, please check again")


