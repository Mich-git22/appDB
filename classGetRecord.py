import requests

class GetRecord:
    def __init__(self):
        self.__url = "https://66db3d98f47a05d55be77b70.mockapi.io/api/v1/estudiante"

    def get_last_record(self):
        response = requests.get(self.__url)
        if response.status_code == 200:
            data = response.json()
            if data:
                return data[-1]  # Obtenemos el último registro
            else:
                return None
        else:
            return None
