# Python3 program to print a given number in words.
one = [ "", "one ", "two ", "three ", "four ",
        "five ", "six ", "seven ", "eight ",
        "nine ", "ten ", "eleven ", "twelve ",
        "thirteen ", "fourteen ", "fifteen ",
        "sixteen ", "seventeen ", "eighteen ",
        "nineteen "]
ten = [ "", "", "twenty ", "thirty ", "forty ",
        "fifty ", "sixty ", "seventy ", "eighty ",
        "ninety "]

def numToWords(n, s):
    str = ""
    # if n is more than 19, divide it
    if (n > 19):
        str += ten[n // 10] + one[n % 10]
    else:
        str += one[n]
    # if n is non-zero
    if (n):
        str += s
    return str

# Function to print a given number in words
def convertToWords(n):
    if(n>10000000000000000000):
        return "Aukat me rah kar number daal chote"

    out = ""
    out += numToWords((n // 100000000000000000),"shankh ")
    out += numToWords(((n // 1000000000000000)%100),"padma ")
    out += numToWords(((n // 10000000000000)%100),"nil ")
    out += numToWords(((n // 100000000000)%100),"kharab ")
    out += numToWords(((n // 1000000000)%100),"arab ")
    out += numToWords(((n // 10000000)%100),"crore ")
    out += numToWords(((n // 100000) % 100),"lakh ")
    out += numToWords(((n // 1000) % 100),"thousand ")
    out += numToWords(((n // 100) % 10),"hundred ")
    if (n > 100 and n % 100):
        out += "and "
    out += numToWords((n % 100), "")
    return out


if (__name__=="__main__"):
    while 1:
        n=int(input("Enter Number :"))
        print(convertToWords(n))
        c=input("Want to Exit Press (y/n): ")
        if c=='y':
            break
