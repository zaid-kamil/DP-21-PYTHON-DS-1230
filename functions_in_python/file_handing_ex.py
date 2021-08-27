# open(filepath) -> open file

def read_file(addr):
    f = open(addr)
    content = f.read()
    f.close()
    return content

out = read_file('D:/DP21PYDS1230/functions_in_python/default_param_ex1.py')
out2 = read_file('D:/DP21PYDS1230/hello.py')
print(out)
print(out2)