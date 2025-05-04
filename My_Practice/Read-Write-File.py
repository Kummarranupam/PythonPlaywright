with open("D:\\Sample_Edit_File.txt",'r') as readfile:

    read_data = readfile.read()
    print(read_data)

# to handle exception
try:
    with open("D:\\Sample_Edit_File.txt",'w') as writefile:
        writr_data= writefile.write("I love India")
        print(writr_data)
#even we can you - except Exception as e    for all kinds of exception
except FileNotFoundError as e:
    print(e)

