import express, { json } from "express";
import cors from "cors";
//const express = require("express");

const productos = [];

const app = express();
//middleware> es un intermediario entre todas las peticiones que se realicen a determinado
//endpoint o si no se indica a todas las peticiones de mi API
//que mi aplicacion de expres s podra entender toda la infromacion enviadda por el cliente siempre y cuando sea un json

app.use(json());
//para toda la aplicacion voy a utilizar la configuracion de los CORS
// app.use(cors({
//     methods: ["GET", "POST"],
//     origin: 'https://wwww.mipagina.com'
// }))
const port = 3000;

app.get('/', (req, res) => {
    res.status(200).json({
        //req> es la informacion que me viene del cliente
        //req> es la respuesta que le dare al cliente
        message: 'peticion realizada exitosamente',
    });
});

app.post("/producto", (req, res) => {
    console.log(req.body);
    if (req.body) {
        productos.push(req.body);
        res.status(201).json({
            message: "Producto agregado exitosamente",
            producto: req.body,
        });
    } else {
        res.status(400).json({
            message: "informacion incorrecta",
            producto: req.body,
        });
    }
    res.json({
        message: "Producto agregado exitosamente",
    });
});
//mediante el endpoint /productos devolver todos los productos en el siguiente formato:
//{
// message:'los productos son:',
// content:  [...]
//}
app.get("/productos", (req, res) => {
    res.status(200).json({
        message: "los prodcutos son",
        content: productos,
    });
});
app.route('/producto', (req, res) => {
    res.status(200).json({
        message: "los productos son:",
        content: productos,
    });
});
app
    .route("/producto/:id")
    .get((req, res) => {
        //destructuracion
        const { id } = req.params;
        //cosnt nuevoID = req.params.id
        //buscar ese prodcutos por ese id(posicion del array)y si existe, retornar el producto 200
        //si no existe retornar un estado 200 e indicar en el message que el  producto no existe
        //ayudita: que pasa si en js queremos ingresar a una posicion que o existe??
        if (productos[id]) {
            return res.status(200).json({
                content: productos[id]
            });
        } else {
            return res.status(200).json({
                message: 'productos no existe',
                content: null,
            });
        }

    })

    .put((req, res) => {
        const { id } = req.params;
        if (productos[id - 1]) {
            productos[id - 1] = req.body;
            return res.status(200).json({
                message: "Producto actualizado correctamente",
                content: productos[id],
            });
        } else {
            return res.status(400).json({
                message: "producto o existe",
                cotent: null,
            });
        }
    })
    .delete((req, res) => {
        const { id } = req.params;
        if (productos[id - 1]) {
            productos.splice(id - 1, 1);

            return res.status(200).json({
                message: "productos eliminado exitosamente",
                content: producto,
            });
        } else {
            return res.status(400), json({
                message: "Producto no existe",
                content: null,
            });
        }
    });
//
//estado>200
//se mantendra escuchqando las consultas realizadas a este servidormediante el puerto definido

app.listen(port, () => {
    //Esto sucedera cuando se levante el servidor de express
    console.log(`Servidor levantando exitosamente! ${port}`);

});