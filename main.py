from src import Challenge as ch

if __name__ == '__main__':
    # productArray=["chromecast","silla","mesa"]
    flag = True
    while flag:
        prods = str(input("Por favor ingrese al menos 3 productos para listar separados por ',':"))
        array_product = prods.split(",")
        if (len(array_product)>=3):
            challenge = ch.Challenge(array_product)
            challenge.execute()
            flag = False
        else:
            print("Para ejecutar el proceso correctamente debe ingresar al menos 3 productos.")