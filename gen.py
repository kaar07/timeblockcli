with open("immutable.txt","w") as data:
    for i in range(0,9):
        data.write("0"+str(i)+":00 - 0"+str(i+1)+":00:-\n")
    data.write("09:00 - 10:00:-\n")
    for j in range(10,23):
        data.write(str(j)+":00 - "+str(j+1)+":00:-\n")
    data.write("23:00 - 00:00:-\n")
