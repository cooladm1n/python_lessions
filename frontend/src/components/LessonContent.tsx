'use client';

import { LessonDetail } from '@/types';
import ReactMarkdown from 'react-markdown';

interface LessonContentProps {
  lesson: LessonDetail;
}

export default function LessonContent({ lesson }: LessonContentProps) {
  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200">
      <div className="p-6">
        <div className="prose prose-sm max-w-none">
          <ReactMarkdown>{lesson.readme}</ReactMarkdown>
        </div>
        
        {lesson.tasks.length > 0 && (
          <div className="mt-6 pt-6 border-t border-gray-200">
            <h3 className="text-lg font-semibold text-gray-900 mb-3">Tasks</h3>
            <div className="grid gap-2">
              {lesson.tasks.map((task, index) => (
                <div
                  key={task}
                  className="flex items-center px-3 py-2 bg-gray-50 rounded-md text-sm font-mono"
                >
                  <span className="text-gray-500 mr-2">{index + 1}.</span>
                  <span className="text-gray-700">{task}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
