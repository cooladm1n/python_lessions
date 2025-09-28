 'use client';

import Link from 'next/link';
import { usePathname, useParams } from 'next/navigation';
import { useEffect, useState } from 'react';
import { apiClient } from '@/lib/api';

export default function Breadcrumbs() {
  const pathname = usePathname();
  const params = useParams();
  const topicId = (params && (params as any).topicId) as string | undefined;
  const lessonId = (params && (params as any).lessonId) as string | undefined;

  const [topicTitle, setTopicTitle] = useState<string | null>(null);

  useEffect(() => {
    let mounted = true;
    if (topicId) {
      apiClient.getTopicDetail(topicId).then((t) => {
        if (mounted) setTopicTitle(t.title || topicId);
      }).catch(() => {
        if (mounted) setTopicTitle(topicId);
      });
    } else {
      setTopicTitle(null);
    }
    return () => { mounted = false; };
  }, [topicId]);

  // Build crumbs from params if present
  const crumbs = [
    { href: '/', label: 'Home' },
  ];

  if (topicId) {
    crumbs.push({ href: `/topics/${topicId}`, label: topicTitle || topicId });
  }

  if (lessonId) {
    crumbs.push({ href: pathname || '#', label: lessonId });
  }

  return (
    <div className="bg-gray-50 border-b border-gray-200">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2">
        <nav className="text-sm text-gray-600" aria-label="Breadcrumb">
          <ol className="flex items-center space-x-2">
            {crumbs.map((c, i) => (
              <li key={c.href} className="flex items-center">
                <Link href={c.href} className={`hover:text-gray-800 ${i === crumbs.length - 1 ? 'text-gray-900 font-medium' : ''}`}>
                  {c.label}
                </Link>
                {i < crumbs.length - 1 && <span className="mx-2">/</span>}
              </li>
            ))}
          </ol>
        </nav>
      </div>
    </div>
  );
}
