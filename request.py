from datetime import datetime
import json
import time
import requests

url = 'http://127.0.0.1:8000/click'


def clicou():

    hora_clique = datetime.now()
    new_hora_clique = hora_clique.strftime("%Y-%m-%d %H:%M:%S")
    #time.sleep(20)
    segundo_clique = datetime.now()
    new_segundo_clique = segundo_clique.strftime("%Y-%m-%d %H:%M:%S")
    
    print("\nPrimeiro click:", new_hora_clique, "\nSegundo click", new_segundo_clique)

    data = {
        "primeiro_clique": new_hora_clique,
        "segundo_clique": new_segundo_clique
    }
    print(data)
    
    response = requests.post(url, json=data)
    print(response)

clicou()

