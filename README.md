# booking Api

### Instalacion
1. Clonar repositorio
2. Copiar archivo env
```
cp .env.example .env
```
### Correr la aplicacion
1. levantar contenedores
```
docker-compose up -d --build
```
2. sitio administrativo
```
localhost:8000/admin
```
```
user:admin
pass:admin
email:admin@admin.com
```
3. Endpoint Base
```
localhost:8000/api
```

## Descripcion
He seguido el siguiente enfoque para cumplir este flujo:
he creado varios modelos, como: habitacion, tipo de habitacion, reserva, venta, pago, modo de pago y factura.

Donde reserva y venta son las mas importantes ya que estas manejaran la logica principal del negocio,
Reserva guardara datos relacionados a la reserva de una habitacion y venta guardara datos relacionados a lo economico.

Por lo cual a continuacion describire alunas de las rutas mas importantes:
1. ```/api/room/``` GET Lista las habitacion disponibles 

2. ```/api/booking/``` POST  Crea una reservacion, recibe identificadores de la habitacion, cliente, user entre los mas importantes.
3. ```/api/booking/{booking_id}/```   PUT  Modifica una reservacion
4. ```/api/payment/{booking_id}/```   POST Realiza un pago a una reservacion, una venta puede tener muchos pagos, entonces esta se ira acumlando hasta completar con el total.
5. ```/api/booking/finished/{sale_id}/``` POST Finaliza la venta y se guardan los datos para la factura.
