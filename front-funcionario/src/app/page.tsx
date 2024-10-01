"use client";
import React from "react";

import "primereact/resources/themes/bootstrap4-dark-blue/theme.css";
import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import HomeScreen from "@/screens/HomeScreen";
import Login from "@/screens/Login";
import { ToastContainer } from "react-toastify";

export default function LoginPage() {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean | null>(null);
  const router = useRouter();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      setIsAuthenticated(true);
      router.push("/");
    } else {
      setIsAuthenticated(false);
    }
  }, [router]);

  if (isAuthenticated === null) {
    return <div>Carregando...</div>;
  }

  return (
    <>
      {isAuthenticated ? <HomeScreen /> : <Login />}
      <ToastContainer />
    </>
  );
}
