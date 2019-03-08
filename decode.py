import sys

sourceFile = sys.argv[1]
destFile = sys.argv[2]

print("decode " + sourceFile + " to " + destFile)

with open(sourceFile, 'r') as readFile:
    # read a list of lines into data
    data = readFile.read()
    readFile.close()

data = data.replace("&#xd;&#xa;", "\r\n")
data = data.replace("&#x27;", '"')
data = data.replace("&#x28;", '(')
data = data.replace("&#x29;", ')')
data = data.replace("&#x3c;", '<')
data = data.replace("&#x3d;", '=')
data = data.replace("&#x3e;", '>')
data = data.replace("&#x2a;", '*')
data = data.replace("&#x2f;", '/')
data = data.replace("&#x3a;", ':')
data = data.replace("&#x2b;", '+')
data = data.replace("&#x24;", '$')
data = data.replace("&#x7b;", '{')
data = data.replace("&#x7d;", '}')
data = data.replace("&#x3b;", ';')
data = data.replace("&#xf6;", 'ö')
data = data.replace("&#xdf;", 'ß')
data = data.replace("&#x22;", '"')
data = data.replace("&#x21;", '!')
data = data.replace("&#xe4;", 'ä')
data = data.replace("&#x7c;", '|')

data = data.replace("&#xa;", "\r\n")


# and write everything back
with open(destFile, 'w') as writeFile:
    writeFile.write(data)

