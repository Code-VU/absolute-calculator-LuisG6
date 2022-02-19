def calculateAbsolute():
    
    # This first line is provided for you
    try: 
        in_num  = int(input("Enter a number: "))

        if in_num < 21:
            absoluteDifference = 21 - in_num
    
        else:
            absoluteDifference = (in_num - 21) * 2

        print(f"Result: {absoluteDifference}")

    except:
        print("Please enter a number ")

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateAbsolute() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
# calculateAbsolute()