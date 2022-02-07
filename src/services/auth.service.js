import { prisma } from "../prisma.js";
import { compareSync } from "bcrypt";

export class AuthService {
    static async login({ correo, password }) {
        //SELECT password, tipo_usuario FROM USUARIO WHERE correo=""
        //si no lo encuentra lanzara un error de not found
        const usuarioEncontrado = await prisma.usuario.findUnique({
            where: { correo },
            select: { password: true, TipoUsuario: true },
            rejectOnNotFound: true,
        });
        const resultado = compareSync(password, usuarioEncontrado.password)
        if (resultado) {
            return { message: "si es el usuario" };
        } else {
            return { message: "Credenciales incorrrectas" };
        }


    }
}