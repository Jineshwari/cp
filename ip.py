def type_and_ip(ip):
    octets = ip.split('.')
    octet1= int(octets[0])
    octet2 = int(octets[1])

    if octet1 >= 0 and octet1 <= 127:
        ip_class = "A"
    elif octet1 >= 128 and octet1 <= 191:
        ip_class = "A"
    elif octet1 >= 192 and octet1 <= 223:
        ip_class = "A"
    elif octet1 >= 224 and octet1 <= 239:
        ip_class = "A"
    else:
        ip_class = "E (Expirmental)"

    if (octet1 == 10) or (octet1 == 172 and octet2 >= 16 and octet2 <= 31) or (octet1 == 192 and octet2 == 168):
        ip_type = "Private"
    else:
        ip_type = "Public"
    
    return ip_class,ip_type

ip = input("enter the ip address : ")
ip_class, ip_type = type_and_ip(ip)
print("Ip address is : ", ip)
print("ip class is : ", ip_class)
print("ip type is : ", ip_type)