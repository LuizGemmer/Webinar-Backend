import type { Metadata } from 'next'
import { Kanit } from 'next/font/google'
import './globals.css'

const kanit = Kanit({
  weight: ['100', '200', '300', '400', '500', '600', '700', '800', '900'],
  subsets: ['latin'],
})

export const metadata: Metadata = {
  title: 'Funcionário | Webinar',
  description: '',
  keywords: [],
}

interface Props {
  children: React.ReactNode
}

export default function RootLayout({ children }: Props) {
  return (
    <html lang="pt-BR">
      <body className={`flex flex-col bg-black text-white ${kanit.className}`}>
        {children}
      </body>
    </html>
  )
}
