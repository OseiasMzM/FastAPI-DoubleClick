import json
import sqlite3
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import time
from fastapi.responses import FileResponse

# ==== Import Module ====
from src.Model.clickmodel import Cliques
# =======================

app = FastAPI()

conn = sqlite3.connect('database.db')


@app.get("/")
async def home():
    return {"message": "Backend is running..."}


@app.post("/click/", status_code=status.HTTP_201_CREATED)
def create_clique(clique: Cliques):
    try:
        conn = sqlite3.connect('database.db', check_same_thread=False)

        # Verificando quantos items possui no DB
        cursor = conn.execute('''SELECT id, primeiroclique, segundoclique, diferenca FROM cliques''')
        cliques = [{"id": row[0], "primeiroclique": row[1], "segundoclique": row[2], "diferenca": row[3]} for row in cursor.fetchall()]    
        next_id: int = len(cliques) + 1
        # ===========================
        
        
        difere = lambda x,y: (-1)*(x - y).total_seconds()

        diferenca_seg = difere(clique.primeiro_clique, clique.segundo_clique)
        

        conn.execute('''INSERT INTO cliques (id,primeiroclique, segundoclique, diferenca)
                        VALUES (?, ?, ?, ?)''', (next_id, clique.primeiro_clique, clique.segundo_clique,diferenca_seg))
        conn.commit()
        
        return {"message":"item was create"}  
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


@app.get("/cliques", status_code=status.HTTP_200_OK)
async def get_cliques():
    cursor = conn.execute('''SELECT id, primeiroclique, segundoclique, diferenca FROM cliques''')
    cliques = [{"id": row[0], "primeiroclique": row[1], "segundoclique": row[2], "diferenca": row[3]} for row in cursor.fetchall()]

    print(cliques)
    return cliques



@app.delete('/clique/{clique_id}', status_code=status.HTTP_200_OK)
async def delete_clique(clique_id: int):
    
    cursor = conn.cursor()
    cursor.execute("DELETE FROM cliques WHERE id = ?", (clique_id,))
    conn.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted"}



@app.get("/download")
async def download_file():
    cursor = conn.execute('''SELECT id, primeiroclique, segundoclique, diferenca FROM cliques''')
    cliques = [{"id": row[0], "primeiroclique": row[1], "segundoclique": row[2], "diferenca": row[3]} for row in cursor.fetchall()]
    
    
    with open('result.json', 'w') as f:
        json.dump(cliques, f, indent=4)
    
    path = './result.json'
    return FileResponse(path, media_type="application/octet-stream", filename="result.json")

if __name__ == '__main__':
    
    """
    Verifica se o arquivo Python está sendo executado como um 
    programa principal (ou seja, diretamente do terminal ou da
    linha de comando) ou se está sendo importado como um módulo 
    em outro arquivo Python.
    """
    
    import uvicorn
    
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=8000,
                reload=True)