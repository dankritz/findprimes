def isprime(number):
    for counter in range(1, number+1):
        testresult = number % counter
        if (testresult == 0) and (counter != 1) and (counter != number):
            return False
    else:
        return True


maincounter = 1
while True:
    if (isprime(int(maincounter))):
        print(f'{maincounter}')
    maincounter += 1