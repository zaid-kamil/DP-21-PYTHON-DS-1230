# 

def file_char_counter(filepath):
    f =  open(filepath)
    content = f.read()
    chars = len(content)
    print(f"file  has {chars} characters in it")
    f.close()


file_char_counter('D:\\DP21PYDS1230\\hello.py')
file_char_counter('C:\\Users\\HP 346 G3\\Downloads\\paper_paper_2.html')
# file_char_counter() # error