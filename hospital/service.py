import random

from fastapi_sqlalchemy import db
from base.base_service import BaseService
from hospital.model import Hospital


class HospitalService(BaseService):
    name = 'hospital_service'
    __model__ = Hospital
    
    def generate_random_phone(self):
        return f"+34 {random.randint(600000000, 699999999)}"

    def create_all(self):
        data = [
                {
                    "nom": "Hospital Clínic de Barcelona",
                    "adreça": "Carrer de Villarroel, 170, Barcelona",
                    "lat": 41.3855,
                    "long": 2.157
                },
                {
                    "nom": "Hospital Universitari Vall d'Hebron",
                    "adreça": "Passeig de la Vall d'Hebron, 119-129, Barcelona",
                    "lat": 41.4281,
                    "long": 2.1423
                },
                {
                    "nom": "Hospital de Sant Pau",
                    "adreça": "Carrer de Sant Quintí, 89, Barcelona",
                    "lat": 41.4122,
                    "long": 2.174
                },
                {
                    "nom": "Hospital del Mar",
                    "adreça": "Passeig Marítim, 25-29, Barcelona",
                    "lat": 41.3853,
                    "long": 2.195
                },
                {
                    "nom": "Hospital Universitari de Bellvitge",
                    "adreça": "Carrer de la Feixa Llarga, s/n, L'Hospitalet de Llobregat",
                    "lat": 41.3449,
                    "long": 2.1042
                },
                {
                    "nom": "Hospital Universitari Germans Trias i Pujol",
                    "adreça": "Carretera de Canyet, s/n, Badalona",
                    "lat": 41.4825,
                    "long": 2.2382
                },
                {
                    "nom": "Hospital de Mataró",
                    "adreça": "Carrer de la Cirera, s/n, Mataró",
                    "lat": 41.5381,
                    "long": 2.432
                },
                {
                    "nom": "Hospital de Sabadell (Parc Taulí)",
                    "adreça": "Parc Taulí, 1, Sabadell",
                    "lat": 41.5484,
                    "long": 2.107
                },
                {
                    "nom": "Hospital Universitari Joan XXIII",
                    "adreça": "Carrer del Dr. Mallafrè Guasch, 4, Tarragona",
                    "lat": 41.1239,
                    "long": 1.2416
                },
                {
                    "nom": "Hospital Universitari Arnau de Vilanova",
                    "adreça": "Avinguda de l'Alcalde Rovira Roure, 80, Lleida",
                    "lat": 41.6231,
                    "long": 0.6067
                },
                {
                    "nom": "Hospital Universitari de Girona Doctor Josep Trueta",
                    "adreça": "Avinguda de França, s/n, Girona",
                    "lat": 41.9902,
                    "long": 2.8208
                },
                {
                    "nom": "Hospital de Sant Joan de Déu",
                    "adreça": "Passeig de Sant Joan de Déu, 2, Esplugues de Llobregat",
                    "lat": 41.3814,
                    "long": 2.1035
                },
                {
                    "nom": "Hospital de Terrassa",
                    "adreça": "Carrer de la Cerdanya, s/n, Terrassa",
                    "lat": 41.5603,
                    "long": 2.0245
                },
                {
                    "nom": "Hospital Comarcal del Pallars",
                    "adreça": "Carrer Pau Casals, 5, Tremp",
                    "lat": 42.1672,
                    "long": 0.8945
                },
                {
                    "nom": "Hospital de Cerdanya",
                    "adreça": "Avinguda de l'Exèrcit, 32, Puigcerdà",
                    "lat": 42.4347,
                    "long": 1.9295
                },
                {
                    "nom": "Hospital Comarcal de Mora d'Ebre",
                    "adreça": "Carrer del Castell, s/n, Mora d'Ebre",
                    "lat": 41.0965,
                    "long": 0.6398
                },
                {
                    "nom": "Hospital Comarcal de Vendrell",
                    "adreça": "Carrer de la Pèrgola, s/n, El Vendrell",
                    "lat": 41.2178,
                    "long": 1.5309
                },
                {
                    "nom": "Hospital Universitari Sant Joan de Reus",
                    "adreça": "Avinguda del Doctor Josep Laporte, 2, Reus",
                    "lat": 41.1458,
                    "long": 1.1067
                },
                {
                    "nom": "Hospital Verge de la Cinta",
                    "adreça": "Carrer Esplanetes, 44, Tortosa",
                    "lat": 40.8121,
                    "long": 0.5218
                },
                {
                    "nom": "Hospital Comarcal d'Amposta",
                    "adreça": "Avinguda de la Ràpita, s/n, Amposta",
                    "lat": 40.7176,
                    "long": 0.5763
                },
                {
                    "nom": "Hospital de Santa Maria de Lleida",
                    "adreça": "Carrer de Sant Antoni Maria Claret, 2, Lleida",
                    "lat": 41.6196,
                    "long": 0.6211
                }
        ]
        o_data=[]
        for _ in data:
            hospital = Hospital(
                name = _['nom'],
                address = _['adreça'],
                lat = _['lat'],
                lng = _['long'],
                phone= self.generate_random_phone()
            )
            o_data.append(hospital)
        db.session.add_all(o_data)
        db.session.commit()
        return o_data
    
    def delete_all(self):
        db.session.query(Hospital).delete()
        db.session.commit()