from io import StringIO
sIO = StringIO('Hello\nWorld\nMartian')
print(sIO.getvalue())
while True:
    s = sIO.readline()
    if s == '':
        break
    print(s.strip())