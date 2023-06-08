## SUPERUSUARIO PARA EL ADMIN para la BD respaldada
user: superduper@admin.com
pwd: acme12345

## Introducción
Prueba técnica de Store Acme.
EON IGNITING

## Instalación
Pasos para instalar lo necesario para el proyecto:
    - instalar python y virtualenv
    - crear un entorno virtual desde la terminal:
        python3 -m venv <nombre_del_ambiente>
    - activar el entorno virtual.
        source <nombre_del_ambiente>/bin/activate
    - instalar requirements.txt:
        pip install -r requirements.txt

    

## Configuración
- crear una base de datos, de preferencia en PostgreSQL y configurarla en el settings.py del proyecto:
- restaurar la base adjunta en la base creada en el paso anterior, de lo contrario generar una nueva.

    * Si se genera una nueva base de datos, hay dos opciones para prellenar la base:
        OPCION A:
            se tienen que correr estos scripts en el siguiente orden (teniendo el entorno virtual activado y estando en la ruta en donde esta 'manage.py'):
                ./manage.py script_categories ó python manage.py script_categories
                ./manage.py script_products ó python manage.py script_products
                ./manage.py script_customers ó python manage.py script_customers

            * en el script 'script_customers' que se encuentra en customers > management > commands, se puede cambiar algunos datos para crear superusuarios
            * opcional crear superadmin de la forma tradicional: ./manage.py createsuperuser
        OPCION B:
            - INGRESAR DESDE EL ADMIN            
                - crear superadmin con: ./manage.py createsuperuser
                - ingresar a localhost:8000/admin
                - firmarse como superadmin
                - llenar los modelos desde el admin: Category, Types of transactions, Products
                *** NOTA: Para el modelo ***Types of transactions*** respetar los siguients nombres ***
                *** - "Purchase" Tiene que crearse con el ID 1.*** 
                *** - "Sale". Tiene que crearse con el ID 2. ***                

## Modelos
### Modelo de Usuario
Existen 5 modelos principales
    - auth_user
    - customers_customer. Este modelo extiende el modelo User y se agrega el campo 'balance' el cual tiene un valor por default de 1000
    - catalogs_category. En este modelo se agregan las categorias de los productos
    - catalogs_operationtype. En este modelo se agregan las opciones de:
        - "Purchase"(Compra).  ***RESPETAR EL NOMBRE***. Tiene que crearse con el ID 1.
        - "Sale"(Venta). ***RESPETAR EL NOMBRE***. Tiene que crearse con el ID 2.
    - balances_operation. En este modelo se guardan las transacciones de los customers (Compra y venta).


## Vistas
### Vista de Inicio
- URL: `/`
    - Cuando se inicia el servidor y se ingresa a: 'localhost:8000', se redireccionara directamente a un login.


### Vista de Registro
- Descripción: Página de registro de productos y compra/venta de productos
- URL : `webmin/productos`
    * Si el usuario es superusuario, se redirige a 'webmin/products' para crear, actualizar, ver detalle o eliminar un producto
- URL : `webstore`
    * Si el usuario no es superusuario, se redirige a 'webstore'.
- URL :  `webstore/shoppingcart/<product_id>/user/<user_id>/`
    * Url del shoppingcart. Permite comprar/vender articulos
    
- URL: `/registro`
- Parámetros:
  - Nombre de usuario: Nombre de usuario del nuevo usuario.
  - Correo electrónico: Correo electrónico del nuevo usuario.
  - Contraseña: Contraseña del nuevo usuario.
- Valor de retorno: Si la información es válida, crea un nuevo usuario y redirige a la página de inicio. En caso contrario, muestra un mensaje de error.

