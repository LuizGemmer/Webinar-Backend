"use client";
import React from "react";
import { useState } from "react";
import "../App.css";
import "primereact/resources/themes/bootstrap4-dark-blue/theme.css";
import { Button } from "../components";
import { DataTable } from "primereact/datatable";
import { Button as PrimeButton } from "primereact/button";
import { Column } from "primereact/column";
import { format } from "date-fns";
import { UserRole, Usuario } from "../types";
import { toast } from "react-toastify";
import UsuariosDialog from "./UsuariosDialog";
import { Badge } from "primereact/badge";
import Link from "next/link";
import pencilIcon from "../assets/pencil.png";
import deleteIcon from "../assets/delete.png";

const usuariosData: Usuario[] = [
  {
    id: 1,
    nome: "João Silva",
    senha: "senha123",
    email: "joao.silva@example.com",
    tipo_usuario: UserRole.NORMAL,
    genero: 1,
    data_criacao: new Date(2023, 0, 15),
    data_exclusao: new Date(2024, 0, 15),
  },
  {
    id: 2,
    nome: "Maria Oliveira",
    senha: "senha456",
    email: "maria.oliveira@example.com",
    tipo_usuario: UserRole.ADMIN,
    genero: 2,
    data_criacao: new Date(2023, 1, 10),
    data_exclusao: new Date(2024, 1, 10),
  },
  {
    id: 3,
    nome: "Carlos Sousa",
    senha: "senha789",
    email: "carlos.sousa@example.com",
    tipo_usuario: UserRole.ADMIN,
    genero: 1,
    data_criacao: new Date(2023, 2, 20),
    data_exclusao: new Date(2024, 2, 20),
  },
  {
    id: 4,
    nome: "Ana Costa",
    senha: "senha987",
    email: "ana.costa@example.com",
    tipo_usuario: UserRole.NORMAL,
    genero: 2,
    data_criacao: new Date(2023, 3, 5),
    data_exclusao: new Date(2024, 3, 5),
  },
  {
    id: 5,
    nome: "Pedro Lima",
    senha: "senha654",
    email: "pedro.lima@example.com",
    tipo_usuario: UserRole.NORMAL,
    genero: 1,
    data_criacao: new Date(2023, 4, 18),
    data_exclusao: new Date(2024, 4, 18),
  },
  {
    id: 6,
    nome: "Lucas Martins",
    senha: "senha321",
    email: "lucas.martins@example.com",
    tipo_usuario: UserRole.ADMIN,
    genero: 1,
    data_criacao: new Date(2023, 5, 30),
    data_exclusao: new Date(2024, 5, 30),
  },
  {
    id: 7,
    nome: "Juliana Nunes",
    senha: "senha159",
    email: "juliana.nunes@example.com",
    tipo_usuario: UserRole.NORMAL,
    genero: 2,
    data_criacao: new Date(2023, 6, 12),
    data_exclusao: new Date(2024, 6, 12),
  },
  {
    id: 8,
    nome: "Ricardo Alves",
    senha: "senha753",
    email: "ricardo.alves@example.com",
    tipo_usuario: UserRole.ADMIN,
    genero: 1,
    data_criacao: new Date(2023, 7, 24),
    data_exclusao: new Date(2024, 7, 24),
  },
  {
    id: 9,
    nome: "Fernanda Souza",
    senha: "senha852",
    email: "fernanda.souza@example.com",
    tipo_usuario: UserRole.NORMAL,
    genero: 2,
    data_criacao: new Date(2023, 8, 15),
    data_exclusao: new Date(2024, 8, 15),
  },
  {
    id: 10,
    nome: "Roberto Gomes",
    senha: "senha963",
    email: "roberto.gomes@example.com",
    tipo_usuario: UserRole.ADMIN,
    genero: 1,
    data_criacao: new Date(2023, 9, 8),
    data_exclusao: new Date(2024, 9, 8),
  },
];

const Usuarios = () => {
  const [visible, setVisible] = useState(false);
  const [usuarios, setUsuarios] = useState<Usuario[]>(usuariosData);
  const [editingItem, setEditingItem] = useState<Usuario>();

  //   const fetchUsuarios = async () => {
  //     try {
  //       const response = await fetch(`${BASE_URL}/usuarios`);
  //       const data = await response.json();
  //       setUsuarios(data);
  //     } catch (error) {
  //       console.error("Erro ao buscar usuarios:", error);
  //     }
  //   };

  //   useEffect(() => {
  //     fetchUsuarios();
  //   }, []);

  const handleCloseDialog = () => {
    setVisible(false);
    setEditingItem(undefined);
  };

  const dateTemplate = (rowData: Usuario) => {
    const formattedDate = format(
      new Date(rowData.data_criacao),
      "dd/MM/yyyy HH:mm:ss"
    );
    return formattedDate;
  };

  const handleEdit = (value: Usuario) => {
    setEditingItem(value);
    setVisible(true);
  };

  const handleDelete = async (id: number) => {
    try {
      const updatedUsuarios = usuarios.filter((tipo) => tipo.id !== id);
      setUsuarios(updatedUsuarios);
      toast.success("Usuário deletado com sucesso!");
    } catch (error) {
      console.error("Erro ao excluir Usuário:", error);
      toast.error("Erro ao excluir Usuário");
    }
  };

  const editBody = (rowData: Usuario) => {
    return (
      <PrimeButton
        icon="pi pi-pencil"
        style={{ backgroundColor: "#FFFFFF", borderColor: "#FFFFFF" }}
        onClick={() => handleEdit(rowData)}
        iconPos="bottom"
      >
        <img src={pencilIcon.src} width={16} height={16} />
      </PrimeButton>
    );
  };

  const deleteBody = (rowData: Usuario) => {
    return (
      <PrimeButton
        icon="pi pi-check"
        iconPos="right"
        style={{ backgroundColor: "#FF0000", borderColor: "#FF0000" }}
        onClick={() => handleDelete(rowData.id)}
      >
        <img src={deleteIcon.src} width={16} height={16} />
      </PrimeButton>
    );
  };

  const statusBody = (rowData: Usuario) => {
    let statusText = "";
    let severity: "info" | "warning" | "danger" | "success" = "info";
    switch (rowData.tipo_usuario) {
      case UserRole.NORMAL:
        statusText = "Normal";
        severity = "info";
        break;
      case UserRole.ADMIN:
        statusText = "Administrador";
        severity = "danger";
        break;
      default:
        throw Error("Tipo de usuário não identificado");
    }
    return <Badge value={statusText} severity={severity} />;
  };

  return (
    <Link href="/usuarios">
      <div className="App">
        <DataTable
          value={usuarios}
          tableStyle={{ width: "100vw", padding: "1rem" }}
          dataKey="id"
          header={
            <Button
              label="Cadastrar"
              type="secondary"
              onClick={() => setVisible(true)}
            />
          }
        >
          <Column body={editBody} align="left" bodyStyle={{ width: 0 }} />
          <Column body={deleteBody} align="left" />
          <Column field="nome" header="Nome" />
          <Column field="email" header="Email" />
          <Column
            field="tipo_usuario"
            header="Tipo de Usuário"
            body={statusBody}
          />
          <Column
            field="dataCriacao"
            header="Data de Criação"
            body={dateTemplate}
          />
        </DataTable>
        {visible && (
          <UsuariosDialog
            visible={visible}
            closeDialog={handleCloseDialog}
            itemToEdit={editingItem}
            // update={fetchUsuarios}
          />
        )}
      </div>
    </Link>
  );
};

export default Usuarios;
