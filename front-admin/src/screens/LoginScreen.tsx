import ComponenteTesteLink from '@/components/ComponenteTesteLink'

export default function LoginScreen() {
  return (
    <div className="flex flex-col gap-4">
      <span>Pagina de login - admin</span>
      <ComponenteTesteLink href="/" label="Ir para pagina home" />
    </div>
  )
}
