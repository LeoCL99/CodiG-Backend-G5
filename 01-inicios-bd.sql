CREATE DATABASE pruebas;

create table personas(
    -- Ahora definimos las columnas pertenecientes a esta tabla
    id INT, -- solamente se podran almacenar numeros
    nombre VARCHAR(100), -- se podran almacenar caract. HASTA 100 como maximo
    dni CHAR(8), -- siempre se almacenara 8 caracteres
    fecha_nacimiento DATE, -- seran solamente fecha
    createdd_at DATETIME, -- sera fecha y hora, minuto , segundo
    sexo ENUM('MASCULINO','FEMENINO','OTRO','HELICOPTERO'), -- solamente podra tener los valores definidos
    estado BOOL -- o sera true o false
);