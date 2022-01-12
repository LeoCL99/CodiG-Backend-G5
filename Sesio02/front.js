console.log("Hola desde el navegador");
fetch("http://127.0.0.1:5000/producto",{method:'GET'}).then((response)=>{
    return response.json();
})
.then((data)=>{
    console.log(data);
}).catch((error)=>{
    console.error(error)
});
fetch("http://127.0.0.1:5000/producto",{method:'POST',body:JSON.stringify({
    nombre:"Paneton con arto bromato",
    precio:17.5,
    disponible:true,
    fecha_vencimiento:"2022-01-14"
}),
//Los headers sirven para indicar al backend varias opciones para la transferencia de informacion como el conetent
//-type que servira para indicar que tipo de contenido estamos enviando mediante el body
headers:{
    "Content-Type":"application/json"
},
})
.then((response)=>{
    return response.json();
})
.then((data)=>{
    console.log(data);
}).catch((error)=>{
    console.error(error)
});

// const URL ="http://12.0.0.1:5000/productos";
// const getData=async()=>{
//     try {
//         const response = await fetch(URL,{method:"GET"});
//         const data=await response.json();
//         console.log(data);
//     } catch (error) {
//         throw error;
//     }
// } 
