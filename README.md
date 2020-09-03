# Busca de coordenadas geográficas - Mapbox API
 
Esse projeto tem o objetivo de oferecer um serviço de busca de coordenadas geográficas a partir a partir de endereço(s) informado(s). A arquitetura da solução:

![Project_img](img/project_diagram.png)

### Tecnologias:

- Flask: Micro-framework escrito em python para desenvolvimento web;
- Mapbox Geocoding API: API do Mapbox(https://www.mapbox.com/place-search/) para coleta das coordenadas;
- Postgresql: Banco de dados para armazenamento das consultas;
- Docker: Container para rodar e isolar a aplicação;

## Como rodar

Iniciar na raiz do diretório do projeto:

```bash
docker-compose up
```
Assim que executar, bastar acessar o "localhost:5000" no seu navegador.

![print_web](img/print_web.png)

⚠️ Utilize o arquivo de excel como layout [aqui](file/)




