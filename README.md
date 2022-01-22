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
1. ```/api/room/``` GET Lista las habitacion disponibles, una habitacion puede tener los siguientes estados:available, booked, maintenance.
2. ```/api/booking/``` POST  Crea una reservacion, recibe identificadores de la habitacion, cliente, usuario, entre los mas importantes. Esta ruta creara una reservacion y una venta preliminar, y a su vez la habitacion pasara a booked. Tambien la venta pasara al estado pendiente hasta que se complete el pago.
3. ```/api/booking/{booking_id}/```   PUT  Modifica algunas datos de la reservacion.
4. ```/api/payment/{booking_id}/```   POST Realiza un pago a una reservacion, una venta puede tener muchos pagos, entonces esta se ira acumlando hasta completar con el total. Una vez completado el total se actualizara el estado de la reservacion.
5. ```/api/booking/finished/{sale_id}/``` POST Finaliza la venta y se guardan los datos para la factura. Esta puede ser factura o recibo de acuerdo al parametro enviado en crear la reservacion. 

Existen otros endpoints pero son CRUD pequeños que sirven para crear cliente, tipo de habitacion, modo de pago entro otros.