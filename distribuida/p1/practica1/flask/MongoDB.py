import pymongo as pym
import datetime
from datetime import timezone
import pytz
import pandas as pd
from bson.objectid import ObjectId

#Class for MongoDB
class MongoDB:
    uri = "mongodb+srv://samurai:UG894zAbRXi9Vr9@clustersamurai0-naqy5.gcp.mongodb.net/Universo?retryWrites=true&w=majority"
    #global client
    client = pym.MongoClient(uri)

    def __init__(self):
        self.cliente_db = self.client.Cliente
        self.universo_db = self.client.Universo


    def find_portafolios_by_email(self, email):
        try:
            portafolios = []
            # find({"email": email}, {"cliente": 1, "fundamentals": 1}
            for portafolio in list(self.cliente_db.Portafolios.find({"email": email})):
                portafolio.pop('_id', None)
                portafolios.append(portafolio)
            return portafolios
        except Exception as e:
            raise

    def insert_portafolio(self, portafolio):
        try:
            self.cliente_db.Portafolios.insert_one(portafolio)
        except Exception as e:
            print("Error: no se pudo guardar el portafolio en Mongo")

    #-----------------------------------------
    def update_portafolio(self, portafolio, email, typePortfolio):
        try:
            #self.cliente_db.Portafolios.insert_one(portafolio)

            portafolio.pop('cliente')
            portafolio.pop('email')
            portafolio.pop('fundamentals')
            portafolio.pop('name')
            #portafolio.pop('notificaciones')
            #portafolio.pop('portafolio_info')
            portafolio.pop('tipo')
            if 'pesos_portafolio' in portafolio:
                portafolio.pop('pesos_portafolio')

            self.cliente_db.Portafolios.update({'email':email,
                                                'cliente.portfolioType':typePortfolio},
                                                {"$set": portafolio })

            #db.Portafolios.update({ 'email':'rodolfo@samurai.science', 'cliente.portfolioType':'casque'}, response_json )

        except Exception as e:
            print("Error: no se pudo actualizar el portafolio en Mongo")
            print(str(e))
    #------------------------------------------
    def update_portafolio_by_id(self, portafolio, portafolio_id):
        try:
            self.cliente_db.Portafolios.update_one({"_id": ObjectId(portafolio_id)}, {"$set": portafolio })
        except Exception as e:
            print("Error: no se pudo actualizar el portafolio en Mongo")
            print(str(e))

    def get_client(self):
        return self.client

    def get_data_db(self, beginDate, endDate, arrayStock):
        dateBegin = datetime.datetime.strptime(beginDate+"T00:00:00.000Z", "%Y-%m-%dT%H:%M:%S.000Z")
        dateEnd = datetime.datetime.strptime(endDate+"T00:00:00.000Z", "%Y-%m-%dT%H:%M:%S.000Z")
        dataList = self.universo_db.YahooFinance.find({'Date': {'$gte': dateBegin, '$lte': dateEnd}, 'Stock': {'$in': arrayStock}})
        data = []
        for ldate in dataList:
            data.append(ldate)
        return data

    def find_all_fundamentals(self):
        dataList = self.universo_db.Fundamentals.find()
        data = []
        for ldate in dataList:
            f_id = ldate.pop('_id', None)
            #data['f_id'] = str(f_id)
            data.append(ldate)
        return data

    def insert_fundamentals(self, fundamentals):
        try:
            self.universo_db.Fundamentals.insert_many(fundamentals, ordered=False)
        except:
            print("Algunos datos en StockError:  ya fueron almacenados")


    def get_data_stocks_df(self, beginDate, endDate, arrayStock):
        l = mongo.get_data_db(beginDate, endDate, arrayStock)

        close_dict = {}
        open_dict = {}
        for e in l:
            key = e['Stock']
            #caso para dataframe close
            if key in close_dict.keys():
                close_dict[key].loc[str(e['Date'])] = [e['ClosePrice']]
            else:
                new_df = pd.DataFrame(columns = [key])
                new_df.loc[str(e['Date'])] = [e['ClosePrice']]
                new_df.index.name = "close"
                close_dict[key] = new_df

                #caso para dataframe open
            if key in open_dict.keys():
                open_dict[key].loc[str(e['Date'])] = [e['OpenPrice']]
            else:
                new_df = pd.DataFrame(columns = [key])
                new_df.loc[str(e['Date'])] = [e['OpenPrice']]
                new_df.index.name = "open"
                open_dict[key] = new_df

        join_df_close = pd.DataFrame()
        join_df_open = pd.DataFrame()

        flag = True
        for key in close_dict.keys():
            if flag:
                join_df_close = close_dict[key]
                join_df_open = open_dict[key]
                flag = False
            else:
                join_df_close = join_df_close.join(close_dict[key])
                join_df_open = join_df_open.join(close_dict[key])

        return join_df_close, join_df_open

    def get_operaciones_portafolio_by_id(self, portafolio_id):
        portafolio = self.cliente_db.Portafolios.find_one({"_id": ObjectId(portafolio_id)}, {"notificaciones": 1})
        if portafolio:
            portafolio['_id'] = str(portafolio['_id'])
            #print(type(portafolio))
            if not 'notificaciones' in portafolio:
                portafolio['notificaciones'] = []
                return portafolio
            operaciones = []
            for notificacion in portafolio['notificaciones']:
                json_not = {
                  "time": notificacion[0],
                  "action": notificacion[1],
                  "ticker": notificacion[2],
                  "share": notificacion[3],
                  "profit": notificacion[4]
                }
                operaciones.append(json_not)
            portafolio['notificaciones'] = operaciones
        return portafolio

    def update_portafolio_operaciones(self, portafolio_id, tuplas):
        try:
            self.cliente_db.Portafolios.update_one({"_id": ObjectId(portafolio_id)}, {"$set": {"notificaciones" : tuplas}})
            return True;
        except Exception as e:
            print("error:", str(e))
            return False

