
def main():

    for num in range(1,101): # 1-100 
        fizzBuzz(num)

def fizzBuzz(num):

    line=""   
    if num % 3 ==0: #Catches multiples of 3
        line ="Fizz"
        if num % 5 ==0: #Catches multiples of 3 & 5
            line += "Buzz!"          
    elif num % 5 ==0: #Catches multiples of 5
        line ="Buzz"
    else:
        line = str(num)

    print(line)

main()
