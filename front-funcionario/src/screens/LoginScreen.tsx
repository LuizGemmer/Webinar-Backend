import ComponenteTesteLink from '@/components/ComponenteTesteLink'

export default function LoginScreen() {
  return (
    <div className="flex flex-col gap-4">
      <span>Pagina de login - funcionario</span>
      <ComponenteTesteLink href="/" label="Ir para pagina home" />
    </div>
  )
}
