import { hashSync } from "bcrypt";


export default async (prisma) => {
    const password = hashSync('Welcome123!', 10)

    await prisma.usuario.upsert({
        create: {
            nombre: "Leonardo",
            correo: "leo987444@hotmail.com",
            password,
            TipoUsuario: "ADMIN",
        },
        update: {
            password,
        },
        where: {
            //solamente se pueden declarar las columnas qeu sean unicas
            //
            correo: "leo987444@hotmail.com",
        },
    });
};