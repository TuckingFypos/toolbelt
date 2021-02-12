notValid = "Card is not valid"
Valid = "Card is valid"

def checkLength(number:int):
    # does the input have the proper number of characters to be a valid number?
    if len(str(number)) != 16:
        return notValid
    else:
        # map the input to a list of ints
        values = list(map(int, str(number)))
        # remove the check digit
        checkSum = values.pop()
        # iterate over the remaining digits, multiply ever other value by two
        for i in range(0, len(values), 2):
            processing = (values[i])*2
            # if any value is in the double-digits, get the sum of those digits to shrink the value back down
            if processing >= 10:
                toSum = list(map(int, str(processing)))
                processed = toSum[0] + toSum[1]
                values[i] = processed
            else:
                values[i] = processing
        # add each of the worked-on values to the check digit at the end of the list
        check = sum(values, checkSum)
        # if the remaining value is a multiple of 10, the card number is valid
        if (check+checkSum)%10 == 0:
            return Valid
        else:
            return notValid


val = int(input("Enter a CC number for validation: "))

print(checkLength(val))
