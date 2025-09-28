 'use client';

import { useEffect, useState, Fragment } from 'react';
import Link from 'next/link';
import { apiClient } from '@/lib/api';
import { Topic } from '@/types';

export default function Header() {
  const [topics, setTopics] = useState<Topic[]>([]);
  const [openTopics, setOpenTopics] = useState(false);
  const [openResources, setOpenResources] = useState(false);

  useEffect(() => {
    let mounted = true;
    apiClient.getTopics().then((data) => {
      if (mounted) setTopics(data);
    }).catch(() => {});
    return () => { mounted = false; };
  }, []);

  return (
    <header className="bg-white border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center space-x-6">
            <Link href="/" className="text-xl font-bold text-gray-900">Python Lessons</Link>

            {/* Topics dropdown */}
            <div className="relative">
              <button
                onClick={() => setOpenTopics((v) => !v)}
                className="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-100"
                aria-expanded={openTopics}
              >
                Topics
              </button>

              {openTopics && (
                <div className="absolute mt-2 w-56 bg-white border border-gray-200 rounded-md shadow-lg z-20">
                  <div className="py-1">
                    {topics.length === 0 && (
                      <div className="px-4 py-2 text-sm text-gray-500">No topics</div>
                    )}
                    {topics.map((t) => (
                      <Link
                        key={t.id}
                        href={`/topics/${t.id}`}
                        className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50"
                        onClick={() => setOpenTopics(false)}
                      >
                        {t.title}
                      </Link>
                    ))}
                  </div>
                </div>
              )}
            </div>

            {/* Resources two-level dropdown */}
            <div className="relative">
              <button
                onClick={() => setOpenResources((v) => !v)}
                className="px-3 py-2 rounded-md text-sm font-medium text-gray-700 hover:bg-gray-100"
                aria-expanded={openResources}
              >
                Resources
              </button>

              {openResources && (
                <div className="absolute mt-2 w-64 bg-white border border-gray-200 rounded-md shadow-lg z-20">
                  <div className="py-1">
                    <div className="px-4 py-2 text-sm text-gray-700 font-medium">Docs</div>
                    <Link href="/docs/getting-started" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50">Getting Started</Link>
                    <Link href="/docs/api" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50">API</Link>

                    <div className="border-t border-gray-100 mt-2" />

                    <div className="px-4 py-2 text-sm text-gray-700 font-medium">Community</div>
                    <div className="pl-4">
                      <Link href="/community/forum" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50">Forum</Link>
                      <Link href="/community/chat" className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-50">Chat</Link>
                    </div>
                  </div>
                </div>
              )}
            </div>
          </div>

          <div>
            <nav className="flex items-center space-x-4">
              <Link href="/about" className="text-sm text-gray-600 hover:text-gray-800">About</Link>
              <Link href="/contact" className="text-sm text-gray-600 hover:text-gray-800">Contact</Link>
            </nav>
          </div>
        </div>
      </div>
    </header>
  );
}
