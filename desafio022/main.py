from desafio022 import ControleRemoto

if __name__ == '__main__':

    crontrole = ControleRemoto()

    crontrole.ligar_desligar()

    crontrole.mudar_canal(6)
    crontrole.mudar_volume(subir=True)
    crontrole.mudar_volume(subir=True)
    crontrole.mudar_volume(subir=True)
    crontrole.mudar_volume(subir=True)
    #cr.mudar_volume(subir=True)
    crontrole.mostrar_tv()