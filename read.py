str_line=""
sources_list = []
with open(".\sources.list",'r') as file:
    for line in file:
        var = line.split("\n")
        str_line = "echo " + "\"" + var[0] + "\"" + " >> 1.list"
        sources_list.append(str_line)

with open("echo.txt","w+") as file:
    for i in sources_list:
        file.write(i)
        file.write("\n")
ping("What's up")
