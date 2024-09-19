import React from "react";
import Link from "next/link";

interface Props {
  href: string;
  label: string;
}

export default function ComponenteTesteLink({ href, label }: Props) {
  return <Link href={href}>{label}</Link>;
}
