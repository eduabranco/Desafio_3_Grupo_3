while True:
    informacoes_do_usuario = str(input('Indique, respectivamente. indicando respectivamente número de figurinhas (e espaços) do álbum, o número de figurinhas carimbadas do álbum e o número de figurinhas já compradas: ')).split()
    print()
    dados_usuario = []
    for c in informacoes_do_usuario:
        c = int(c)
        dados_usuario.append(c)
    if len(dados_usuario) != 3:
        print('Os dados forma digitados incorretamente. \nDigite novamente. \n')
    elif not(1 <= dados_usuario[0] <= 100) or not(1 <= dados_usuario[1] <= dados_usuario[0]/2) or not(1<= dados_usuario[2] <= 300):
        print('Os dados forma digitados incorretamente. \nDigite novamente. \n')
    else:
        break
while True:    
    figurinhas_carimbadas = str(input('Indique as figurinhas carimbadas do álbum: ')).split()
    figurinhas_carimbadas = list(dict.fromkeys(figurinhas_carimbadas))
    cont_carimbadas = 0
    for c in figurinhas_carimbadas:
        c = int(c)
        figurinhas_carimbadas[cont_carimbadas] = c
        cont_carimbadas += 1
    if max(figurinhas_carimbadas) > dados_usuario[0] or min(figurinhas_carimbadas)<1:
        print('Os dados foram inseridos de forma incorreta. \nTente novamente. \n')
    elif not(cont_carimbadas == dados_usuario[1]):
        print('Os dados foram inseridos de forma incorreta. \nTente novamente. \n')
    else:
        break 
while True:    
    figurinhas_compradas = str(input('Indique as figuinhas já comprada: ')).split()
    if len(figurinhas_compradas)==dados_usuario[2]:
        figurinhas_compradas = list(dict.fromkeys(figurinhas_compradas))
        cont = 0
        for c in figurinhas_compradas:
            c = int(c)
            figurinhas_compradas[cont] = c
            cont += 1
        if max(figurinhas_compradas) > dados_usuario[0]:
            print('Os dados foram inseridos de forma incorreta. \nTente novamente. \n')
        elif not(1 <= cont <= dados_usuario[0]):
            print('Os dados foram inseridos de forma incorreta. \nTente novamente. \n')
        else:
            break 
    else:print('Os dados foram inseridos de forma incorreta. \nTente novamente. \n')
for i in figurinhas_carimbadas:
    for j in figurinhas_compradas:
        if j == i:
            cont_carimbadas-=1
            break
        
print(f"Faltam {cont_carimbadas} figurinhas carimbadas.")