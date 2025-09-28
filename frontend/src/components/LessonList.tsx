'use client';

import { Lesson } from '@/types';
import Link from 'next/link';
import { basename } from 'path';

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
        {lessons.map((lesson) => {
          // lesson.lessonId may be in the form "topic/lesson_01". Use the basename (after last slash)
          const shortId = lesson.lessonId.includes('/') ? lesson.lessonId.split('/').pop()! : lesson.lessonId;
          const isCurrent = currentLessonId === shortId || currentLessonId === lesson.lessonId;

          return (
            <Link
              key={lesson.lessonId}
              href={`/topics/${topicId}/${shortId}/overview`}
              className={`block px-3 py-2 rounded-md text-sm transition-colors ${
                isCurrent
                  ? 'bg-blue-100 text-blue-700'
                  : 'text-gray-700 hover:bg-gray-100'
              }`}
            >
              <div className="font-medium">{lesson.title}</div>
            </Link>
          );
        })}
      </div>
    </div>
  );
}
