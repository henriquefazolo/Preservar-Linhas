entrada = input('Insira o nome do arquivo a ser tratado ("exemplo.txt"):\n')
caracteres = input('Insira os caracteres, que se encontrados, preservara a linha:\n')

saida = ''

with open(entrada, 'r') as arquivo:


    for linha in arquivo:
      

        if caracteres in linha:
            saida += linha

with open('saida.txt', 'w') as arquivo:
    arquivo.writelines(saida)


print('Concluído.')

input('Pressione qualquer tecla para sair.')

