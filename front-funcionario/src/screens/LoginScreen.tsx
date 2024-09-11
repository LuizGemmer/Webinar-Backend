import { Input } from "@/components/ui/input";

import {
  Card,
  CardContent,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";

export default function LoginScreen() {
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
            "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
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
              <Label style={{ color: "#000" }}>Email</Label>
              <Input
                style={{ padding: 5, borderRadius: 5, color: "#000" }}
                type="email"
                id="Email"
                placeholder="Email"
              />
            </div>
            <div style={{ flexDirection: "column", display: "flex" }}>
              <Label style={{ color: "#000" }}>Senha</Label>
              <Input
                style={{ padding: 5, borderRadius: 5, color: "#000" }}
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
          <Button
            style={{
              width: "100%",
              backgroundColor: "#ffffff",
              color: "#000",
              border: "1px solid #d1d5db",
              padding: "0.5rem",
              borderRadius: "0.375rem",
              cursor: "pointer",
              fontWeight: "bold",
            }}
          >
            Entrar
          </Button>
          <Button
            style={{
              width: "100%",
              backgroundColor: "#6b7280",
              color: "#fff",
              padding: "0.5rem",
              borderRadius: "0.375rem",
              cursor: "pointer",
              fontWeight: "bold",
            }}
          >
            Cadastrar
          </Button>
        </CardFooter>
      </Card>
    </div>
  );
}
