import re

ip = "129.34.13.4kdsfskdj"
hostname = "urkjdfk3434ff"

#pattern = re.compile("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}")

#test = pattern.match(ip)

test = re.search("(\d{1,3}\.\d{1,3})(\.\d{1,3}\.\d{1,3})", ip)


print(test.group(1))
print(test.group(2))
print(test.group(0))