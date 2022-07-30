import math,os
class Frame:
    def __init__(self, signal, channel, flightTime, craftBat, goggleBat, craftCellCount, delay, bitrate, rcsignal, start, end):
        self.signal=signal
        self.frameNumber=0
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
        
        data = contents[2].split(" ")
        time = contents[1].split("-->")
        tDelay = int(data[7].split(":")[1].split("m")[0])
        tBitrage = float(data[8].split(":")[1].split("M")[0])


        return Frame(data[0][7],data[1][3],data[2].split(":")[1],data[3].split(":")[1],data[4].split(":")[1],data[5].split(":")[1],tDelay,tBitrage,data[8].split(":")[1],time[0],time[1])
#Store the frame that the even happened at. Instead of just the humber
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
        print("Lowest Bitrage:", self.lowestBitrage.bitrate)
        print("Highest Delay: ", self.maxDelay.delay)
        print("Averag delay: ", (self.averageDelay))    
        print("Averag Bitrage: ", (self.averageBitrage))    

class Suite:
    print("asdasd")
# target = open("DJIG0000.srt"

target = input("Enter target name(has to be in the same folder): ")
flight = Flight(target)
with open(target) as f:
    stuff = f.readlines() 
    for i in range(0,len(stuff),4):
        tFrame=Frame.make((int(stuff[i].strip()),stuff[i+1].strip(),stuff[i+2].strip()))
        flight.add(tFrame)
        
    flight.math()
flight.out()
# print(len(frames))
# print("Flight Name: ", flight.name)
# print("Frame count: ",flight.frameCount)
# print("Lowest Bitrage:", flight.lowestBitrage.bitrate)
# print("Highest Delay: ", flight.maxDelay.delay)
# print("Averag delay: ", (flight.averageDelay))    
# print("Averag Bitrage: ", (flight.averageBitrage))    
