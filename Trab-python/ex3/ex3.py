
def tranformar_pra_mb(bytes):
    mb = round(int(bytes)/ (1024 * 1024), 2)
    return str(mb).replace('.', ',')

def main():
    with open(r'python\ex3\usuarios.txt', 'r') as file: 
        txt = file.readlines()
    
    usuarios = dict(map(str.split, txt))
    total = sum(map(int , usuarios.values()))
    

    with open(r'python\ex3\resultado.txt', 'w', encoding='UTF-8') as file:
        file.write('ACME Inc. Uso do espaço em disco pelos usuários\n')
        file.write('------------------------------------------------------------------------\n')
        file.write('Nr. Usuário Espaço utilizado % do uso\n')
        for count, usuario in enumerate(usuarios.items()):
            nome, espaco = usuario
            file.write(f'{count}   {nome.ljust(15)} {(tranformar_pra_mb(espaco) + "MB").rjust(10)}    {round(int(espaco) * 100/total)} %\n')
    
main()
