import ComponenteTesteLink from '@/components/ComponenteTesteLink'

export default function HomeScreen() {
  return (
    <div className="flex flex-col gap-4">
      <span>Pagina home - admin</span>
      <ComponenteTesteLink href="/login" label="Ir para pagina login" />
    </div>
  )
}
