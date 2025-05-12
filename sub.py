import ipaddress

def find_subnet(ip,prefix):

    network = ipaddress.IPv4Network(f'{ip}/{prefix}', strict= False)
    return network.netmask

ip = input("enter the ip address : ")
prefix = int(input("enter the prefix :"))

subnet = find_subnet(ip,prefix)
print(f"Subnet mask for {ip}/{prefix} is :  {subnet}")