from enum import Enum

class Holidays(Enum):
    New_Year_Day = 1
    MLK_Day = 2
    President_Day = 3
    Memorial_Day = 4
    Independence_Day = 5
    Labor_Day = 6
    Columbus_Day = 7
    Veterans_Day = 8
    Thanksgiving = 9
    Christmas_Day = 10

class BookingApp:
    def __init__(self):
        self.__waitingList = []
        self.__customer = None
        self.__magicianNames = self.readFiles('Magician.dat.txt')
        self.__holidayNames = self.readFiles('Holidays.dat.txt')
        self.__holidaydic = {}
        for holiday in self.__holidayNames:
            self.__holidaydic[holiday] = {}
        self.__scheduledic = {}
        self.fetchdata()

    def showTitle(self):
        print("The Magician scheduling program\n")

    def showMenu(self):
        print("COMMAND MENU")
        print("SC - Schedule an appointment with magician")
        print("C - Cancel an appointment with magician")
        print("S - Status of Magician or Holiday")
        print("Q - Quit")
        print()

    def readFiles(self, filename):
        names = []
        with open(filename, 'r') as file:
            line = file.readline()
            while line:
                if line.strip():
                    names.append(line.strip())
                line = file.readline()
        return names

    def addCustomer(self, customerName):
        if self.__customer is None:
            self.__customer = customerName
        else:
            self.__waitingList.append(customerName)

    def deleteCustomer(self, customerName):
        if self.__customer == customerName:
            if not self.__waitingList:
                self.__customer = None
            else:
                self.__customer = self.__waitingList.pop(0)
        else:
            self.__waitingList.remove(customerName)

    def getCustomer(self):
        return self.__customer

    def getWaitingList(self):
        return self.__waitingList

    def Booking(self):
        customer_name = input("Please enter customer name who wants to schedule a holiday")
        print("List of Holidays to schedule appointment with a magician")
        print("1 - New Year's Day")
        print("2 - Martin Luther King Day")
        print("3 - President's Day")
        print("4 - Memorial Day")
        print("5 - Independence Day")
        print("6 - Labor Day")
        print("7 - Columbus Day")
        print("8 - Veterans Day")
        print("9 - Thanksgiving")
        print("10 - Christmas Day")

        holiday_num = int(input("Please enter the holiday number"))
        holiday_name = Holidays(holiday_num).name
        if (customer_name, holiday_name) in self.__scheduledic:
            print("Already scheduled")
            return
        if holiday_name not in self.__holidaydic:
            print("Holiday name doesn't exist")
            return

        event_holiday = self.__holidaydic[holiday_name]
        count = -1
        free_magician = None
        for magician in self.__magicianNames:
            if magician not in event_holiday or event_holiday[magician].getCustomer() is None:
                event = BookingApp()
                event.addCustomer(customer_name)
                event_holiday[magician] = event
                self.__scheduledic[(customer_name, holiday_name)] = event
                print('Magician {} is scheduled for customer {} on {}'.format(magician, customer_name, holiday_name))
                return
            else:
                event = event_holiday[magician]
                if count == -1 or count > len(event.getWaitingList()):
                    free_magician = magician
                    count = len(event.getWaitingList())
        event = event_holiday[free_magician]
        event.addCustomer(customer_name)
        self.__scheduledic[(customer_name, holiday_name)] = event
        print('Customer {} is put on waiting list for {}'.format(customer_name, holiday_name))

    def Cancel(self):
        customer_name = input("Please enter customer name who wants to schedule a holiday")
        print("List of Holidays to schedule appointment with a magician")
        print("1 - New Year's Day")
        print("2 - Martin Luther King Day")
        print("3 - President's Day")
        print("4 - Memorial Day")
        print("5 - Independence Day")
        print("6 - Labor Day")
        print("7 - Columbus Day")
        print("8 - Veterans Day")
        print("9 - Thanksgiving")
        print("10 - Christmas Day")

        holiday_num = int(input("Please enter the holiday number"))
        holiday_name = Holidays(holiday_num).name

        if (customer_name, holiday_name) not in self.__scheduledic:
            print("Can't find your booking.")
            return
        self.__scheduledic[(customer_name, holiday_name)].deleteCustomer(customer_name)
        print("Booking is cancelled")

    def showStatus(self):
        name = input("Enter name of magician or holiday whose status you want to see")
        if name in self.__magicianNames:
            print("Magician's {} schedule is as follows: ".format(name))
            self.getMagicianSchedulelist(name)
        elif name in self.__holidayNames:
            print("Schedule on {} is as follows: ".format(name))
            self.getHolidaySchedulelist(name)
        else:
            print("Please enter correct name of Magician/Holiday")

    def getMagicianSchedulelist(self, magician):
        for holiday_name, event_holiday in self.__holidaydic.items():
            if magician not in event_holiday:
                continue
            customer = event_holiday[magician].getCustomer()
            waitingList = event_holiday[magician].getWaitingList()
            if customer is not None:
                print("A Magician {} is scheduled for Customer {} ".format(magician, customer, ))
                if waitingList:
                    print("Waiting list members are:")
                    print(waitingList)

    def getHolidaySchedulelist(self, holiday):
        event_holiday = self.__holidaydic[holiday]
        for name, event in event_holiday.items():
            if event.getCustomer():
                print("An event is scheduled by Magician {} for Customer {} on {} ".format(name, event.getCustomer(),
                                                                                           holiday))
                if event.getWaitingList():
                    print("Waiting list holidays are:")
                    print(event.getWaitingList())

    def fetchdata(self):
        try:
            with open('Schedule', 'r') as f:
                holiday_count = int(f.readline().strip())
                for i in range(holiday_count):
                    holiday = f.readline().strip()
                    self.__holidaydic[holiday] = {}
                    event_count = int(f.readline().strip())
                    for j in range(event_count):
                        m = f.readline().strip()
                        c = f.readline().strip()
                        wait_list = []
                        wait_count = int(f.readline().strip())
                        for k in range(wait_count):
                            wait_list.append(f.readline().strip())
                        event = BookingApp()
                        event.addCustomer(c)
                        self.__scheduledic[(c, holiday)] = event
                        for w in wait_list:
                            event.addCustomer(w)
                            self.__scheduledic[(w, holiday)] = event
                        self.__holidaydic[holiday][m] = event
        except Exception as e:
            return

    def quit(self):
        with open('Schedule', 'w') as f:
            for holiday, events in self.__holidaydic.items():
                f.write(holiday)
                f.write(",")
                count = 0
                for m, event in events.items():
                    if event.getCustomer() is not None:
                        count += 1
                f.write(str(count))
                f.write("\n")
                for m, event in events.items():
                    if event.getCustomer() is not None:
                        f.write(m)
                        f.write(",")
                        f.write(event.getCustomer())
                        f.write("\n")



def main():
    app = BookingApp()
    app.showTitle()
    while True:
        app.showMenu()
        print()
        command = input("Command: ")
        command = command.lower()
        if command == "sc":
            app.Booking()
        elif command == "c":
            app.Cancel()
        elif command == "s":
            app.showStatus()
            print()
        elif command == "q":
            app.quit()
            print('Bye!')
            return
        else:
            print("Not a valid command. Please try again.\n")


if __name__ == "__main__":
    main()
