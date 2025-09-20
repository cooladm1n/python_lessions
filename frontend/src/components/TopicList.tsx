'use client';

import { Topic } from '@/types';
import Link from 'next/link';

interface TopicListProps {
  topics: Topic[];
  currentTopicId?: string;
}

export default function TopicList({ topics, currentTopicId }: TopicListProps) {
  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200">
      <div className="p-4 border-b border-gray-200">
        <h2 className="text-lg font-semibold text-gray-900">Topics</h2>
      </div>
      <div className="p-2">
        {topics.map((topic) => (
          <Link
            key={topic.id}
            href={`/topics/${topic.id}`}
            className={`block px-3 py-2 rounded-md text-sm font-medium transition-colors ${
              currentTopicId === topic.id
                ? 'bg-blue-100 text-blue-700'
                : 'text-gray-700 hover:bg-gray-100'
            }`}
          >
            <div className="flex justify-between items-center">
              <span>{topic.title}</span>
              <span className="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded-full">
                {topic.lessons_count}
              </span>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
