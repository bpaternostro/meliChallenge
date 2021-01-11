from src.apiManager import Meli as meli
from src.apiManager import Tableau as tableau

class Challenge:

    def __init__(self,products):
        self.productArray =products

    def execute(self):
        #obtener data del servicio publico de MELI. Al menos 150
        results=[]
        for prod in self.productArray:
            api=meli.Meli()
            response=api.get_results(prod)
            if(response!=None):
                results_array=response['results']
                for item in results_array:
                    results.append(item)
            else:
                print("Existieron inconvenientes para procesar el producto: " + prod)

        if(len(results)!=0):
            #generar archivo de tipo hyper y dejar en el localhost para abrir con Tableau
            ta = tableau.Tableau()
            status_process = ta.extract_search_results(results)
            print("El proceso se ejecutó correctamente: " + str(status_process) + ", y se generaron : " + str(len(results)) + " registros")
        else:
            print("Existieron en el procesamiento del archivo .hyper. No fue posible obtener resultados validos.")

