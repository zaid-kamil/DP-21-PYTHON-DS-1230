
def find_occurence_in_file(filepath, word):
    f = open(filepath)
    content = f.read()
    f.close()
    occurence = content.count(word)    
    return occurence


word_count = find_occurence_in_file('D:\DP21PYDS1230\hello.py','hello')
print(f'hello occurs {word_count} times')

word_count = find_occurence_in_file('D:\DP21PYDS1230\hello.py','python')
print(f'python occurs {word_count} times')