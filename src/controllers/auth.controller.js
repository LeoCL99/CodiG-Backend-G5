//export const login =async()=>{...}
import { AuthService } from "../services/auth.service.js"
export async function login(req, res) {
    const { correo, password } = req.body;
    const result = await AuthService.login({ correo, password });

    res.status(200).json(result);

}