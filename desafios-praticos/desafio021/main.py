from desafio021 import Caneta


if __name__ == '__main__':

    caneta_azul = Caneta()
    caneta_azul.destampar()

    caneta_azul.escreva("Hello World")
    caneta_azul.quebrar_linha()

    caneta_azul.escreva("--------------------")
    caneta_azul.quebrar_linha()

    caneta_verde = Caneta("Verde")
    caneta_verde.destampar()

    nome = caneta_verde.leia("Digite seu nome: ")

    caneta_verde.escreva(f"Ola {nome}")
    caneta_verde.quebrar_linha()

    idade = caneta_verde.leia("Digite sua idade: ")
    caneta_verde.escreva(idade)
