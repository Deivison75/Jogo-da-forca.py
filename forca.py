from nomes import nome_sorteado
from pygame import init, mixer


# variaveis
palavra = nome_sorteado
vidas = 6
ganhou = False
letras_adivinhadas = []
palavra_oculta = "_" * len(palavra)
resposta = 'a'

# loop que inicia o jogo
while True:
    print(letras_adivinhadas)
    print(vidas)
    print("Palavra oculta:", " ".join(palavra_oculta))

    letra = input('Digite uma letra: ')
    while not letra.isalpha() or len(letra) != 1:
        letra = input('Você precisa digitar apenas uma letra para começar: ')
    # Atualiza a palavra oculta com as letras corretamente adivinhadas
    for i in range(len(palavra)):
        if palavra[i] == letra:
            palavra_oculta = palavra_oculta[:i] + letra + palavra_oculta[i+1:]

    if palavra_oculta == palavra:  # se apalavra oculta for igual a palavra vc ganha
        ganhou = True

    # verifica se o usuario acertou ou nao
    if letra in palavra:
        print('Letra correta!')

    elif letra not in letras_adivinhadas:  # verifica se o usuario ja chutou uma letra ou nao
        letras_adivinhadas.append(letra)
        vidas -= 1
    else:
        print('Essa letra ja foi utilizada')

        # imprime se ganhou ou nao
    if ganhou:
        print(f'Você ganhou a palavra era {palavra}')

        init()
        mixer.music.load('musicas/silvio-santos-certa-resposta.mp3')
        mixer.music.play()

        while mixer.music.get_busy():
            pass
        break
    if vidas <= 0:
        print(f'Eroooou, a palavra era {palavra}')

        init()
        mixer.music.load('musicas/faustao-errou.mp3')
        mixer.music.play()

        while mixer.music.get_busy():
            pass
        break
    #     resposta = input("Deseja continuar (s/n)? ")

    # elif resposta.lower() != "s":
    #     continue
    # else:
    #     break
