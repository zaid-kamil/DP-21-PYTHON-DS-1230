# file handling using function
# 1. read file ☑
# 2. write file
# 3. append file

def read_file(address_of_file):
    file = open(address_of_file)    # load the file
    content= file.read()            # read the file content from string
    file.close()                    # stop using file
    print(content)


read_file("D:\\DP21PYDS1230\\hello.py")

# the joys of online classes