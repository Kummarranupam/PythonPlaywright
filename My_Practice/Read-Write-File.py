with open("D:\\Sample_Edit_File.txt",'r') as readfile:

    read_data = readfile.read()
    print(read_data)

with open("D:\\Sample_Edit_File.txt",'w') as writefile:
    writr_data= writefile.write("I love India")
    print(writr_data)
    