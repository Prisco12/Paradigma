import ipaddress  

with open("lista_ips.txt", 'r') as ips:
    x = ips.readlines()
    
y = list(map(lambda x: x.replace('\n',''), x ))
print(y)


def validate_ip(ip_str):  
    try: 
        ipaddress.ip_address(ip_str)     
        return True
    except ValueError: 
        return False
    
ipsv = list()
ipsiv = list()
with open("resultado_lista_ips.txt", 'w') as result:
    for ip in y:
        valido = ['[Endereços válidos:] ']
        invalido = ['[Endereços inválidos:] ']
        if ipaddress.ip_address(ip):
            valido.append(ip)
        else:
            invalido.append(ip)

    for j in valido:
        result.write(j)
    for i in invalido:
        result.write(i)
   


# def main():
#     x = map(validate_ip, lista_ip)

#     print(list(x))

# main()
       
   

