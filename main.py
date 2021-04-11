import os
import math
import datetime

home = os.getenv("HOME")


def formatTime(inp):
    if(inp.find(":") >= 0):
        hours, mins = inp.strip().split(":")
        return float(hours)+(float(mins)/60)
    return float(inp)


def showBlockedTime():
    immutabletxt_path = home+"/.timeblock/immutable.txt"
    with open(immutabletxt_path, "r") as data:
        for line in data:
            print(line, end="")


def archiveSchedule():
    immutabletxt_path = home+"/.timeblock/immutable.txt"
    archivePath = home+"/.timeblock/Archives/"
    todate = datetime.date.today()
    arcfile = archivePath+todate.strftime("%b-%d-%Y")+".txt"
    os.system("touch "+arcfile)
    os.system("cp "+immutabletxt_path+" "+arcfile)


def printHelp():
    help = """
    IMMUTABLE TIME BLOCK
    --------------------
    command format: # [__command__]

    Options                         |   Commands
    --------------------------------|----------------
                                    |
    show blocked schedule           |   s/show/Show/ls
    add a block in the schedule     |   a/add/(PRESS ENTER)
    archive today's schedule        |   archive/arc/Archive
    show yesterday's schedule       |   prev/yest/yesterday
    erase schedule and start new    |   erase/Erase
    exit from time block program    |   exit/q/:q

    Press <C>-c anytime to exit abrutly.
    """
    print(help)


def printYesterday():
    try:
        archivePath = home+"/.timeblock/Archives/"
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        fileName = archivePath+yesterday.strftime("%b-%d-%Y")+".txt"
        with open(fileName, "r") as yest:
            for line in yest:
                print(line.strip())
    except FileNotFoundError:
        print(" Yesterday's schedule was not archived. Oops!")


def addTask(n, m, task):
    content = ""
    i = 0
    immutabletxt_path = home+"/.timeblock/immutable.txt"
    with open(immutabletxt_path, "r") as data:
        for line in data:
            if(i >= n and i <= m):
                content += line.strip()+task+"\n"
            else:
                content += line.strip()+"\n"
            i += 1

    with open(immutabletxt_path, 'w') as d:
        d.write(content)


def refreshSchedule():
    immutabletxt_path = home+"/.timeblock/immutable.txt"
    with open(immutabletxt_path, "w") as data:
        for i in range(0, 9):
            data.write("0"+str(i)+":00 - 0"+str(i+1)+":00:-\n")
        data.write("09:00 - 10:00:-\n")
        for j in range(10, 23):
            data.write(str(j)+":00 - "+str(j+1)+":00:-\n")
        data.write("23:00 - 00:00:-\n")


if __name__ == "__main__":
    while(True):
        try:
            print("#", end=" ")
            command = input()
            if(command == "exit" or command == "q" or command == ":q"):
                exit()
            elif(command == "help"):
                printHelp()
            elif(command == "ls" or command == "show" or command == "s" or command == "Show"):
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
            elif(command == "yest" or command == "prev" or command == "yesterday"):
                printYesterday()
            else:
                print("You have entered invalid command. Try typing in \"help\".")
        except KeyboardInterrupt:
            print("")
            exit()
        except ValueError:
            print("  Please enter a valid time.\n  Format allowed -- HH:MM or HH.x (where x=MM/60)")
            pass
