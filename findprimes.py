import threading


class primeFinder(threading.Thread):
    def __init__(self, startnum, stopnum):
        threading.Thread.__init__(self)
        self.startnum = startnum
        self.stopnum = stopnum

    def isprime(self, number):
        for counter in range(1, number+1):
            testresult = number % counter
            if (testresult == 0) and (counter != 1) and (counter != number):
                return False
        else:
            return True

    def run(self):
        for maincounter in range(self.startnum, self.stopnum):
            if (self.isprime(int(maincounter))):
                print(f'{maincounter}')


thread1 = primeFinder(500000, 700000)
thread2 = primeFinder(800000, 900000)
thread1.start()
thread2.start()
