from pathlib import Path
import json

from tableauhyperapi import Connection, HyperProcess, SqlType, TableDefinition, \
    escape_string_literal, escape_name, NOT_NULLABLE, Telemetry, Inserter, CreateMode, TableName, Nullability

class Tableau:

    def __init__(self):
        self.location = "./output/meli_challenge_result.hyper"
        self.test_location = "../output/meli_challenge_result.hyper"
        self.searchResult_table = TableDefinition('results', [
            TableDefinition.Column('id', SqlType.text(), Nullability.NOT_NULLABLE),
            TableDefinition.Column('site_id', SqlType.text(), Nullability.NOT_NULLABLE),
            TableDefinition.Column('title', SqlType.text(), Nullability.NOT_NULLABLE),
            TableDefinition.Column('seller', SqlType.text(), Nullability.NOT_NULLABLE),
            TableDefinition.Column('price', SqlType.text(), Nullability.NOT_NULLABLE),
            TableDefinition.Column('prices', SqlType.json(), Nullability.NOT_NULLABLE),
            TableDefinition.Column('sale_price', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('currency_id', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('available_quantity', SqlType.int(), Nullability.NULLABLE),
            TableDefinition.Column('sold_quantity', SqlType.int(), Nullability.NULLABLE),
            TableDefinition.Column('buying_mode', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('listing_type_id', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('stop_time', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('condition', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('permalink', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('thumbnail', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('accepts_mercadopago', SqlType.bool(), Nullability.NULLABLE),
            TableDefinition.Column('installments', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('address', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('shipping', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('seller_address', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('attributes', SqlType.text(), Nullability.NOT_NULLABLE),
            TableDefinition.Column('original_price', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('category_id', SqlType.text(), Nullability.NOT_NULLABLE),
            TableDefinition.Column('official_store_id', SqlType.int(), Nullability.NULLABLE),
            TableDefinition.Column('domain_id', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('catalog_product_id', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('tags', SqlType.text(), Nullability.NULLABLE),
            TableDefinition.Column('catalog_listing', SqlType.bool(), Nullability.NULLABLE),
            TableDefinition.Column('order_backend', SqlType.int(), Nullability.NULLABLE),
        ])

    def extract_search_results(self, json_array):
        if(json_array != None):
            resp = self.__create_hyper(json_array, self.searchResult_table)
        else:
            print("No es posible realizar el procesamiento con un array=None.")
            resp = None
        return resp

    def __create_hyper(self, json_array, table):
        result = True
        try:
            with HyperProcess(Telemetry.SEND_USAGE_DATA_TO_TABLEAU, 'challenge') as hyper:
                print("Inicia el proceso de extracción.")
                path_to_database = Path(self.location)
                with Connection(endpoint=hyper.endpoint,
                                database=path_to_database,
                                create_mode=CreateMode.CREATE_AND_REPLACE) as connection:

                    print("Se abre la conexión.")
                    #connection.catalog.create_schema('Extract')

                    print("La tabla queda definida")
                    connection.catalog.create_table(table)
                    with Inserter(connection, table) as inserter:
                        for prod in json_array:
                            #le doy un tratamiento especial al campo "catalog_listing"
                            catalog = False
                            try:
                                catalog = prod["catalog_listing"]
                            except:
                                pass

                            aux=[prod["id"],prod["site_id"],prod["title"],json.dumps(prod["seller"]),str(prod["price"]),json.dumps(prod["prices"]),prod["sale_price"],prod["currency_id"],prod["available_quantity"],
                                    prod["sold_quantity"],prod["buying_mode"],prod["listing_type_id"],prod["stop_time"],prod["condition"],prod["permalink"],
                                    prod["thumbnail"],prod["accepts_mercadopago"],json.dumps(prod["installments"]),json.dumps(prod["address"]),json.dumps(prod["shipping"]),json.dumps(prod["seller_address"]),
                                    json.dumps(prod["attributes"]),str(prod["original_price"]),prod["category_id"],prod["official_store_id"],prod["domain_id"],prod["catalog_product_id"],
                                    json.dumps(prod["tags"]),catalog,prod["order_backend"]]
                            inserter.add_row(
                                aux
                            )
                        inserter.execute()
                    print("La data fue ingresada a la tabla")
                print("La conexión con el archivo hyper fue cerrada.")
            print("Cerramos el HyperProcess.")
        except Exception as e:
            print("Error: ejecutando el proceso createHyper con status code: "+ str(e))
            result=False

        return result


    def read_data_from_hyper(self, tableName):
        count=0
        if(tableName != None):
            with HyperProcess(Telemetry.SEND_USAGE_DATA_TO_TABLEAU, 'challenge') as hyper:
                path_to_database = Path(self.test_location)
                with Connection(endpoint=hyper.endpoint,
                                database=path_to_database) as connection:
                    #with connection.execute_query(query=f"SELECT * FROM {TableName('results')} ") as searchResults:
                    with connection.execute_query(query=f"SELECT * FROM {TableName(tableName)} ") as searchResults:
                        for row in searchResults:
                            count += 1
                            print(row)
            print("La cantidad de resultados obtenidos es: " + str(count))
            result=True
        else:
            result=False
        return result