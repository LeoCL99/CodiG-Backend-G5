CREATE DATABASE pruebas;

use pruebas;
create table personas(
    -- Ahora definimos las columnas pertenecientes a esta tabla
    id INT primary key unique not null auto_increment, -- solamente se podran almacenar numeros
    nombre VARCHAR(100) not null, -- se podran almacenar caract. HASTA 100 como maximo
    dni CHAR(8)not null, -- siempre se almacenara 8 caracteres
    fecha_nacimiento DATE, -- seran solamente fecha
    createdd_at DATETIME not null, -- sera fecha y hora, minuto , segundo
    sexo ENUM('MASCULINO','FEMENINO','OTRO','HELICOPTERO'), -- solamente podra tener los valores definidos
    estado BOOL -- o sera true o false
);

-- sirve para modificar el nombre de una columna
-- ALTER TABLE personas RENAME COLUMN nombre TO nombrecito;

-- AHORA INGRESAREMOS LOS DATOS
-- DML (Data Manipulation languaje) Lenguaje de Manipulacion de Datos
-- INSERT : ingresar nueva informacion a una tabka en especifico
INSERT INTO personas(id, nombre, dni,fecha_nacimiento,sexo, estado, createdd_at)Values
                     (1,'Leonardo','73625638','1992-08-01','MASCULINO',true,now());
                     
INSERT INTO personas(id, nombre, dni,fecha_nacimiento, sexo, estado, createdd_at)Values
                     (2,'Billy','73625638','1992-08-01','MASCULINO',true,now());
 INSERT INTO personas(nombre, dni,fecha_nacimiento, sexo, estado, createdd_at)Values
                     ('Billy','73625638','1992-08-01','femenino',false,now());                    
select nombre,id FROM personas; 
select * from personas where nombre='Leonardo' and estado=true;
select * from personas where nombre='Leonardo' or estado=false;
select *from personas order by sexo desc;
-- DDL (Data Definition Language) Lenguaje de Definicion de Datos
-- CREATE: Crear tablas, bases de daots y funciones y procedimientos alamcenados entre otros
-- DROP: Eliminar completamente toda una tabla, una base de datos, una estructura
    DROP TABLE personas;  
create table actividaddes(
	   id int primary key not null auto_increment unique,
       nombre varchar(20),
       intensidad enum('baja','media','alta','muy alta'),
       estado bool,
       persona_id int,
       -- para crear las relaciones
       foreign key(persona_id)references personas(id)
       
);
-- sirve para agregar una nueva columna
-- ALTER TABLE actividades ADD personas_id int;
-- Sirve para agregar una nueva relacion ffk en una tabla
-- ALTER TABLE actividades ADD FOREIGN KEY(persona_id) references personas(id);
use pruebas;
select * from actividaddes;
insert into actividaddes(nombre, intensidad, estado,persona_id)values
                       ('PARRILLADAS','ALTA',true,1);
insert into actividaddes(nombre, intensidad, estado,persona_id)values
                       ('MANEJAR','MEDIA',false,2),                   
                       ('COCINAR','ALTA',true,1),                       
                       ('DISEÑAR','BAJA',false,3);
                       
-- sirve para actualizar una columna existente de la tabla
-- ALTER TABLE actividadees MODIFY id INT AUTO_INCREMENT PRIMERY KEY UNIQUE;

insert into personas (nombre, dni, fecha_nacimiento, sexo, estado, createdd_at)VALUES
                     ('Patricio','15964757','1992-08-01','helicoptero',true,now());                         
insert into actividaddes(nombre, intensidad, estado)values
                       ('NADAR','ALTA',false);
select * from personas inner join actividaddes on personas.id=ACTIVIDADDES.persona_id;  

select * from personas left join actividaddes on personas.id=ACTIVIDADDES.persona_id; 
select * from personas right join actividaddes on personas.id=ACTIVIDADDES.persona_id;    

-- Mostrar todas las personas cuya intensidad en la actividad sea alta
-- distinct > sirve oara obviar mismos resultados de la misma columna
-- select nombre from actividaddes inner join personas on actividaddes.persona_id=personas.id where intensidad='ALTA';
select distinct personas.nombre
 from actividaddes inner join personas on actividaddes.persona_id=personas.id 
 where intensidad='ALTA';
-- Mostrar todos los registros cuyo sexo sea masculino o su estado de la actividad sea true
select * from actividaddes inner join personas 
on actividaddes.persona_id=personas.id where personas.sexo='MASCULINO'
or actividaddes.estado=true;
-- Mostrar las personas que no tengan actividades solamnte su nombre y id     
select personas.nombre, personas.id
from personas left join actividaddes on personas.id=actividaddes.persona_id
where actividaddes.persona_id is null;            
                     