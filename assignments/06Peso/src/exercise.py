def main():
    #escribe tu código abajo de esta línea
    pesoinicial=float(input("Dame el peso inicial: "))
    pesofinal=float(input("Dame el peso final: "))
    meses=int(input("Dame la cantidad de meses: "))
    peso=float((pesoinicial-pesofinal)/meses)
    print("Lo que debes bajar por mes es:", peso)

    pass



if __name__ == '__main__':
    main()
