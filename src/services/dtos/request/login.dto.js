import validator from "validator";

export function loginDto({ correo, password }) {
    //isStrongPassword => longitud minima de 8 caracteres, al menos una mayus, al menos una minus,
    //almenos 1 numero, al menos  simbolo


    if (!validator.isEmail(correo)) {
        throw Error('El correo debe ser un correo valido')
    }
    if (!validator.isStrongPassword(password)) {
        throw Error(
            "La contraseña no es la suficiente segura, debe tener al menos una Mayus, una minus,un numero,un simbolo y una longitud minima de 8 caracteres"
        );
    }
    return { correo, password };
}