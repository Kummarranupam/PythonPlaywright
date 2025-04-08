with open("Sample_text", 'r') as reader:
    file1 = reader.readlines()
    print(file1)
    reversed(file1)
    with open("Sample_text", 'w') as writer:
        for line in reversed(file1):
            writer.write(line)
        #print(line)


