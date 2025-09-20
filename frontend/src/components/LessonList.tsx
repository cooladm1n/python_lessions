'use client';

import { Lesson } from '@/types';
import Link from 'next/link';

interface LessonListProps {
  lessons: Lesson[];
  topicId: string;
  currentLessonId?: string;
}

export default function LessonList({ lessons, topicId, currentLessonId }: LessonListProps) {
  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200">
      <div className="p-4 border-b border-gray-200">
        <h2 className="text-lg font-semibold text-gray-900">Lessons</h2>
      </div>
      <div className="p-2">
        {lessons.map((lesson) => (
          <Link
            key={lesson.lessonId}
            href={`/topics/${topicId}/${lesson.lessonId}/overview`}
            className={`block px-3 py-2 rounded-md text-sm transition-colors ${
              currentLessonId === lesson.lessonId
                ? 'bg-blue-100 text-blue-700'
                : 'text-gray-700 hover:bg-gray-100'
            }`}
          >
            <div className="font-medium">{lesson.displayId}</div>
            <div className="text-xs text-gray-500 mt-1">{lesson.title}</div>
          </Link>
        ))}
      </div>
    </div>
  );
}
