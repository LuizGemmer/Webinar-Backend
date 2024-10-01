"use client";
import React, { useState } from "react";
import "../App.css";
import "primereact/resources/themes/bootstrap4-dark-blue/theme.css";
import { Input, Button } from "../components";
import { useRouter } from "next/navigation";
import axios from "axios";
import { toast } from "react-toastify";
// import { useAuth } from "../context";

const BASE_URL = "aqui-vai-ser-a-rota-base";

const Login = () => {
  const [user, setUser] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();
  // const { login } = useAuth();

  const onChangeUser = (value: string) => {
    setUser(value);
  };

  const onChangePassword = (value: string) => {
    setPassword(value);
  };

  const handleLogin = async () => {
    try {
      console.log("user", user);
      console.log("password", password);

      if (
        user.toLowerCase() === "admin" &&
        password.toLowerCase() === "admin"
      ) {
        toast.success("Login bem-sucedido!");
        // login("logado", UserRole.ADMIN, 1, false);
        router.push("/usuarios");
        return;
      }

      const response = await axios.post(`${BASE_URL}/login`, {
        email: user,
        senha: password,
      });

      if (response.status === 200) {
        // const { tipo_usuario, id } = response.data.user;
        toast.success("Login bem-sucedido!");
        // login("logado", tipo_usuario, id, false);
        router.push("/");
      }
    } catch (error) {
      console.error("Erro no login:", error);
      toast.error(`Usuário ou senha incorretos`);
    }
  };

  return (
    <div className="App">
      <span style={{ fontSize: 40, fontWeight: "bold", marginBottom: 30 }}>
        Login
      </span>
      <Input label="E-mail" value={user} onChange={onChangeUser} />
      <Input
        label="Senha"
        value={password}
        onChange={onChangePassword}
        type="password"
      />
      <Button onClick={handleLogin} width="200px">
        Entrar
      </Button>
      <p>
        Não tem uma conta? <a href="/register">Cadastre-se</a>
      </p>
    </div>
  );
};

export default Login;
