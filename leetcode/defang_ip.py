"""Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

 

Example 1:

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
Example 2:

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"""

def defang_ip(ip_address):

	ip_list = ip_address.split(".")

	return [ [ip] + ["[.]"] for ip in ip_list]

def defang_ip(ip_address):
	return ip_address.replace(".", "[.]")

def defang_ip(ip_address):
	return "".join(('[.]' if i == "." else i for i in ip_address))

print(defang_ip("192.168.0.1"))
print(defang_ip("192.168.1.1"))
print(defang_ip("10.218.0.123"))
