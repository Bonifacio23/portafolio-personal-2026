-- Mi primer ejercicio SQL

CREATE DATABASE tienda_proyecto;
USE tienda_proyecto;
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    ciudad VARCHAR(50)
);
CREATE TABLE productos (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50),
    precio DECIMAL(10,2)
);
CREATE TABLE ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT,
    id_producto INT,
    cantidad INT,
    FOREIGN KEY (id_cliente)
        REFERENCES clientes(id_cliente),
    FOREIGN KEY (id_producto)
        REFERENCES productos(id_producto)
);
INSERT INTO clientes (nombre, ciudad)
VALUES ('Juan','Lima');

INSERT INTO clientes (nombre, ciudad)
VALUES ('Ana','Arequipa');

INSERT INTO clientes (nombre, ciudad)
VALUES ('Pedro','Cusco');
INSERT INTO clientes (nombre, ciudad)
VALUES ('Luis','Piura');
INSERT INTO productos (nombre, precio)
VALUES ('Laptop',2500);

INSERT INTO productos (nombre, precio)
VALUES ('Mouse',80);

INSERT INTO productos (nombre, precio)
VALUES ('Teclado',150);
INSERT INTO ventas (id_cliente, id_producto, cantidad)
VALUES (1,1,1);

INSERT INTO ventas (id_cliente, id_producto, cantidad)
VALUES (2,2,3);

INSERT INTO ventas (id_cliente, id_producto, cantidad)
VALUES (1,3,2);

INSERT INTO ventas (id_cliente, id_producto, cantidad)
VALUES (3,2,4);

SELECT clientes.nombre,
       productos.nombre,
       ventas.cantidad
FROM ventas
INNER JOIN clientes
ON ventas.id_cliente = clientes.id_cliente
INNER JOIN productos
ON ventas.id_producto = productos.id_producto;

SELECT productos.nombre,
SUM(ventas.cantidad) AS total_vendido
FROM productos 
INNER JOIN ventas
ON productos.id_producto = ventas.id_producto
GROUP BY productos.nombre
HAVING SUM(ventas.cantidad) >=2;

SELECT * FROM productos WHERE precio = ( SELECT MAX(precio) FROM productos);

SELECT clientes.nombre, productos.nombre, ventas.cantidad
FROM clientes
LEFT JOIN ventas
ON clientes.id_cliente = ventas.id_cliente
LEFT JOIN productos
ON ventas.id_producto = productos.id_producto;

DELIMITER // 
CREATE PROCEDURE mostrar_clientes()
BEGIN 
SELECT * FROM clientes;
END //
DELIMITER ;
CALL mostrar_clientes();

DELIMITER //
CREATE PROCEDURE buscar_cliente ( in buscar_nombre VARCHAR(50))
BEGIN 
SELECT * FROM clientes
WHERE nombre = buscar_nombre;
END //
DELIMITER ;

CALL buscar_cliente('juan');

DELIMITER //
CREATE PROCEDURE contar_productos ( OUT  cantidad INT )
BEGIN 
SELECT COUNT(*) INTO cantidad FROM productos;
END //
DELIMITER ;

CALL contar_productos(@cantidad);
SELECT @cantidad;

DELIMITER // 
CREATE PROCEDURE precio_maximo (OUT caro DECIMAL(10.2)
BEGIN 
SELECT MAX(precio) INTO caro FROM productos;
END //
DELIMITER ;
