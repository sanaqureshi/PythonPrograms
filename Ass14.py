# 14. Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

row = [unicode(x.strip()) if x is not None else u'' for x in row]
all_html = row[0] + "<br/>" + row[1]
f = open('out.txt', 'w')
f.write(all_html.encode("utf-8")
