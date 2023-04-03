# FastDoubleClick

API responsável por receber dois parametros do frontend:

```json
{
	"primeiroclique": "",
	"segundoclique": ""
}
```

Ao precionar o botão no frontend, envia as informações pro backend armazenando em um banco de dados SQLite e calculando a diferença de um click para o outro.

Rotas:

POST - Envia os parâmetros

GET - Consulta todos os cliques / Download em um arquivo do formato JSON

---

Para fazer a instalação das dependencias do projeto, basta executar o comando abaixo em seu terminal. 

```bash
pip install -r requeriments.txt
```