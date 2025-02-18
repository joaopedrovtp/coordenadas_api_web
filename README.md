# Geographic Coordinates Search
 
This project aims to provide a service for searching geographic coordinates from address(es) provided in a spreadsheet. The solution architecture:


![Project_img](img/project_diagram.png)

### Technologies:

- Flask: Micro-framework written in Python for web development;
- Mapbox Geocoding API: Mapbox API (https://www.mapbox.com/place-search/) to collect the coordinates;
- Postgresql: Database for storing queries;
- Docker: Container to run and isolate the application;

## How to run it

Start at the root of the project directory:

```bash
docker-compose up
```
Once executed, simply access "localhost:5000" in your browser.


![print_web](img/print_web.png)

⚠️ Use the Excel file as a layout [here](file/)

Following the Excel model (same name/number of columns), the API is configured to return up to 3 locations closest to the search and is only valid for addresses in Brazil. The next result would be like this:

**Search:** 

![busca_end](img/busca_end.png)

**Results:**

![consulta_end](img/consulta_end.png)

Ps.:
- The Mapbox Geocoding API accepts up to 100,000 free requests, after that it is paid.
- You can query addresses from any country, but I limited the search to Brazil only;
- API documentation: https://docs.mapbox.com/api/search/#geocoding




