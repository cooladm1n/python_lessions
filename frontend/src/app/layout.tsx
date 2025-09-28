import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import Header from '@/components/Header';
import Breadcrumbs from '@/components/Breadcrumbs';

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Python Lessons',
  description: 'Learn Python programming with interactive lessons and hands-on coding exercises.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="min-h-screen bg-gray-50">
          <Header />
          <Breadcrumbs />
          <main>{children}</main>
        </div>
      </body>
    </html>
  );
}