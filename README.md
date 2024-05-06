
# Challenger Dev Python Senior

Se crea un sistema de registro de infracciones de transito, usando Django y Django-Rest Framework para este caso. En los cuales se crea un administraodor de creacion de usuarios, oficiales, vehiculos, y control de infracciones cargados por los oficiales.

Se usa ademas una libreria de JWT (Simple JWT) compatible con Django para el manejo de autenticacion.




## Instalacion

Para instalar localmente sin usar Docker

```bash
git clone git@github.com:jcroot/challenger.git
cd challenger
python3 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cp conf/.env.example conf/.env # edite este archivo y coloque su configuracion
./manage.py migrate
./manages.py createsu # aqui creamos un superusuario
./manage.py runserver
```

en caso que quiera usar docker-compose
```bash
git clone git@github.com:jcroot/challenger.git
cd challenger
cp conf/.env.example conf/.env # edite este archivo y coloque su configuracion
docker-compose up -d --build
docker-compose exec backend ./manage.py createsu # aqui creamos un superusuario
```


## Arquitectura AWS

La arquitectura propuesta es la uitlizacion de:

* Elastic Load Balancer: Para conseguir balancear la carga a las aplicaciones levantadas en la VPC
* Elastic Beanstalk: Levantar n cantidad de instancias en un serverless, para ofrecer un servicio sobre demanda. Es decir, a mas cantidad de acceso, mas escalibilidad
* RDS PostgreSQL: Base de datos relacional para almacenar los datos
* S3: Sirve tanto para almacenar las aplicaciones en EBS, e imagenes que se pudieran registrar de los vehiculos o de los documentos de propietarios.
* VPC: Solo para acceso limitado. 

![AWS Arquitecture](Challenger-AWS.png)

## Supuestos

[Leer supuestos](https://github.com/jcroot/challenger/blob/78b92582b5bf0ced25e699f7311781ca8e586150/supuestos.txt)


## FAQ

#### Como cargar una infraccion?

- Primero crear el usuario en el sistema bajo el rol de oficial. http://localhost:8000/admin
- Al crear el usuario, se actualiza los datos del usuario en el administrador, y se asigna una clave
- luego para obtener un hash de autenticacion, al ejecutar **POST** http://localhost:8000/api/token/
Ejemplo:
request
```
{
    "username": "oficial-usernam",
    "password": "oficial-password"
}
```
response
```
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxNDkyMDY1NywiaWF0IjoxNzE0ODM0MjU3LCJqdGkiOiJlZDNiMTU0N2E4NzE0NGJmYjY1OWJjYmEwZDFhNmMyYSIsInVzZXJfaWQiOjN9.wPbVoTF52swbNuENMgeOFejsomMVqLNZYN_1ZaWy6ZE",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzE0ODM3ODU3LCJpYXQiOjE3MTQ4MzQyNTcsImp0aSI6ImZhOGQxODBkYjg3ZDQxZWVhNjJjZjBhNThhMWJkNDQ4IiwidXNlcl9pZCI6M30.sytVSHnyVypvGSesHjGs1g6F1Zk_vIZ4vnOpxyYDnko"
}
```
- Obtener el "access" del token para crear una infraccion en el siguiente link **POST** http://localhost:8000/api/cargar_infraccion
Ejemplo:
request
```
{
    "plate_number": "NANI745",
    "timestamp": "2024-05-04 17:00:00",
    "comments": "Estacionamiento vencido"
}
```
response: 201 Created (Para registros creados)
```
{
    "plate_number": "NANI745",
    "comments": "Estacionamiento vencido",
    "timestamp": "2024-05-04T17:00:00Z",
    "officer": 2,
    "officer_fullname": "Jeannine Adams"
}
```
response: 400 Bad request (Para registros que patente no coincide)
```
{
    "plate_number": [
        "Vehicle not found"
    ]
}
```
O la fecha no este bien escrita
```
{
    "timestamp": [
        "Datetime has wrong format. Use one of these formats instead: YYYY-MM-DDThh:mm[:ss[.uuuuuu]][+HH:MM|-HH:MM|Z]."
    ]
}
```
O algun campo es requerido
```
{
    "comments": [
        "This field may not be blank."
    ]
}
```
Para los casos de **Error 500**, el error y el status code van a ser visualizados en la respuesta.

#### Como cargar las patentes en el sistema?

Entrar en el admin http://localhost:8000/admin y crear los datos necesarios como Car Brands (Marca de Vehiculos), Persons (Clientes), Vehicles (Vehiculos asociados con las personas)

