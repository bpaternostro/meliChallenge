from src.util import Global as glo
from string import ascii_letters, digits

class Meli:

    #endpoint = "https://api.mercadolibre.com/sites/MLA/search?q=chromecast&limit=50#json"

    def __init__(self):
        self.env = "https://api.mercadolibre.com/"
        self.searchPath = "sites/MLA/search"

    def get_results(self, product):
        #valido que no existan caracteres especiales
        if (product == None):
            print("El producto no puede ser Null. No es posible realizar una solicitud.")
            return None
        elif (set(product).difference(ascii_letters + digits)):
            print("El producto " + product + " tiene caracteres especiales y no es posible realizar una solicitud.")
            return None

        data = {'q': product, 'limit': 50}
        g = glo.Global()
        response = g.send_request(self.env + self.searchPath, data)

        return response