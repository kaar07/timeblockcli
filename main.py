import os
import math
import datetime


def formatTime(inp):
    if(inp.find(":") >= 0):
        hours, mins = inp.strip().split(":")
        return float(hours)+(float(mins)/60)
    return float(inp)


def showBlockedTime():
    with open("~/.timeblock/immutable.txt") as data:
        for line in data:
            print(line, end="")


def archiveSchedule():
    todate = datetime.date.today()
    arcfile = "~/.timeblock/Archives/"+todate.strftime("%b-%d-%Y")+".txt"
    os.system("touch "+arcfile)
    os.system("cp ~/.timeblock/Archives/immutable.txt "+arcfile)


def printHelp():
    help = """
    IMMUTABLE TIME BLOCK
    --------------------
    command format: # [__command__]

    Options                         |   Commands
    --------------------------------|----------------
                                    |
    show blocked schedule           |   s/show/Show
    add a block in the schedule     |   a/add/(PRESS ENTER)
    archive today's schedule        |   archive/arc/Archive
    erase schedule and start new    |   erase/Erase
    exit from time block program    |   exit/q/:q

    Press <C>-c anytime to exit abrutly.
    """
    print(help)


def addTask(n, m, task):
    content = ""
    i = 0
    with open("~/.timeblock/immutable.txt", "r") as data:
        for line in data:
            if(i >= n and i <= m):
                content += line.strip()+task+"\n"
            else:
                content += line.strip()+"\n"
            i += 1

    with open("~/.timeblock/immutable.txt", 'w') as d:
        d.write(content)


def refreshSchedule():
    with open("~/.timeblock/immutable.txt", "w") as data:
        for i in range(0, 9):
            data.write("0"+str(i)+":00 - 0"+str(i+1)+":00:-\n")
        data.write("09:00 - 10:00:-\n")
        for j in range(10, 23):
            data.write(str(j)+":00 - "+str(j+1)+":00:-\n")
        data.write("23:00 - 00:00:-\n")


if __name__ == "__main__":
    try:
        while(True):
            print("#", end=" ")
            command = input()
            if(command == "exit" or command == "q" or command == ":q"):
                exit()
            elif(command == "help"):
                printHelp()
            elif(command == "show" or command == "s" or command == "Show"):
                showBlockedTime()
            elif(command == "" or command == "add" or command == "a" or command == "add"):
                startTime = (input("  Start time:\t"))
                endTime = (input("  End time:\t"))
                task = str(input("  Task:\t"))
                task += "("+str(startTime)+","+str(endTime)+")"
                task = " |"+task+"| "
                start = formatTime(startTime)
                end = formatTime(endTime)
                start = int(start)
                end = math.ceil(end-1)
                addTask(start, end, task)
                print("  Task added successfully! ")
            elif(command == "erase" or command == "Erase"):
                refreshSchedule()
            elif(command == "archive" or command == "arc" or command == "Archive"):
                archiveSchedule()
            else:
                print("You have entered invalid command. Try typing in \"help\".")
    except KeyboardInterrupt:
        print("")
        exit()
