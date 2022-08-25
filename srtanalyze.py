import math,os

# Features:
# Add gps data so you can tell at what point in the flight you had the bad link quality

# Total statiscs across all flights in a group.


class Frame:
    def __init__(self, signal, channel, flightTime, craftBat, goggleBat, craftCellCount, delay, bitrate, rcsignal, start, end,numba):
        self.signal=signal
        self.frameNumber=numba
        self.frameStart=start
        self.frameEnd=end
        self.channel=channel
        self.flightTime= flightTime
        self.craftBat=craftBat
        self.goggleBat=goggleBat
        self.craftCellCount=craftCellCount
        self.delay=delay
        self.bitrate=bitrate
        self.rcsignal=rcsignal

    def make(contents):
        #contents frameNumber|time|data
        #print(contents)
        data = contents[2].split(" ")
        time = contents[1].split("-->")
        tDelay = int(data[7].split(":")[1].split("m")[0])
        tBitrage = float(data[8].split(":")[1].split("M")[0])
        return Frame(data[0][7],data[1][3],data[2].split(":")[1],data[3].split(":")[1],data[4].split(":")[1],data[5].split(":")[1],tDelay,tBitrage,data[8].split(":")[1],time[0],time[1],contents[0])

class Flight:
    def __init__(self, name):
        self.frames=[]
        self.frameCount=0
        self.name=name
        self.maxDelay=None
        self.lowestBitrage=None
        self.averageDelay=0
        self.averageBitrage=0

    def add(self,flightFrame: Frame):
        if self.maxDelay!=None and self.lowestBitrage!=None:

            if flightFrame.delay > self.maxDelay.delay:
                self.maxDelay=flightFrame
            if flightFrame.bitrate < self.lowestBitrage.bitrate:
                self.lowestBitrage=flightFrame
        else:
            self.maxDelay=flightFrame
            self.lowestBitrage=flightFrame
        self.averageBitrage+=flightFrame.bitrate
        self.averageDelay+=flightFrame.delay
        self.frames.append(flightFrame)
        self.frameCount+=1
    def getMaxDelay(self):
        return self.maxDelay.delay
    def getLowestBitrate(self):
        return  self.lowestBitrage.bitrate


    def math(self):
        self.averageDelay=self.averageDelay//self.frameCount
        self.averageBitrage=self.averageBitrage//self.frameCount

    def out(self):
        print("Flight Name: ", self.name)
        print("Frame count: ",self.frameCount)
        print("Lowest Bitrage:", self.lowestBitrage.bitrate, "mbps ",self.lowestBitrage.delay,"ms"," Frame number: ",self.lowestBitrage.frameNumber)
        print("Highest Delay: ", self.maxDelay.delay,"ms ",self.maxDelay.bitrate,"mbps"," Frame number: ",self.maxDelay.frameNumber)
        print("Averag delay: ", self.averageDelay,"ms")    
        print("Averag Bitrage: ", self.averageBitrage,"mbps")    

class Suite:
    def __init__(self, flights: list[Flight]):
        self.flights=[]
    def __init__(self):
        self.flights=[]

    def add(self, flight: Flight):
        self.flights.append(flight)
    
    def out(self):
        for i in self.flights:
            print("---------------------------------")
            i.out()
    print("asdasd")

def menu():

    print("""
                Menu
    ---------------------------------
    1. |   Add Flight
    2. |   List Flights
    3. |   Output Flights
    4. |   Folder target
    """)

s = Suite()
while True:
    menu()
    case = int(input(":"))
    match case:
        case 1:
            target = input("Enter target name(has to be in the same folder): ")
            flight = Flight(target)
            with open(target) as f:
                stuff = f.readlines() 
                for i in range(0,len(stuff),4):
                    tFrame=Frame.make((int(stuff[i].strip()),stuff[i+1].strip(),stuff[i+2].strip()))
                    flight.add(tFrame)
                    
                flight.math()
            s.add(flight)
        case 2:
            for i in s.flights:
                print(i.out())
        case 3:
            s.out()
        case 4:
            print("add logic for whole folder.")

