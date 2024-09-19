import React from "react";
import { InputText } from "primereact/inputtext";
import "primereact/resources/themes/bootstrap4-light-blue/theme.css";

import {
  Card,
  CardContent,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Button } from "@/components/ui/button";

import styles from "../styles/styles.module.scss";

export default function LoginScreen() {
  const handleLogin = () => {};

  return (
    <div
      style={{
        display: "flex",
        height: "100vh",
        alignItems: "center",
        justifyContent: "center",
        backgroundColor: "#c8c8c8",
      }}
    >
      <Card
        style={{
          width: "100%",
          maxWidth: "28rem",
          padding: "1.5rem",
          boxShadow:
            "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 10px 15px -3px rgba(0, 0, 0, 0.1)",
        }}
      >
        <CardHeader>
          <CardTitle
            style={{
              color: "#000",
              fontWeight: "bold",
              marginBottom: 10,
              textAlign: "center",
            }}
          >
            Login
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div
            style={{
              display: "flex",
              flexDirection: "column",
              gap: "1rem",
            }}
          >
            <div style={{ flexDirection: "column", display: "flex" }}>
              <span style={{ color: "#000" }}>Email</span>
              <InputText
                className={styles.input}
                type="email"
                id="Email"
                placeholder="Email"
              />
            </div>
            <div style={{ flexDirection: "column", display: "flex" }}>
              <span style={{ color: "#000" }}>Senha</span>
              <InputText
                className={styles.input}
                type="password"
                id="Senha"
                placeholder="Senha"
              />
            </div>
          </div>
        </CardContent>
        <CardFooter
          style={{
            display: "flex",
            flexDirection: "column",
            gap: "1rem",
            marginTop: "2rem",
          }}
        >
          <Button className={styles.primaryButton} onClick={handleLogin}>
            Entrar
          </Button>
          <Button className={styles.secondaryButton}>Cadastrar</Button>
        </CardFooter>
      </Card>
    </div>
  );
}
