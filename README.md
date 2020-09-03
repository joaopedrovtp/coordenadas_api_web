# Busca de coordenadas geográficas - Mapbox API
 
Esse projeto tem o objetivo de oferecer um serviço de busca de coordenadas geográficas a partir uma lista de endereços. A arquitetura da solução:

![Project_img](img/project_diagram.png)

### Tecnologias:

- Flask: Micro-framework escrito em python para desenvolvimento web;
- Mapbox Geocoding API: Script em python para coleta das coordenadas utilizando a API do Mapbox (https://www.mapbox.com/place-search/);
- Postgresql: Banco de dados para armazenamento das consultas;
- Docker: Container para rodar e isolar a aplicação;

## Como rodar

```bash
docker-compose up
```
Assim que executar, bastar acessar o "localhost:5000" no seu navegador.

<img>




