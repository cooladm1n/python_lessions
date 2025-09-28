'use client';

import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';
import { LessonDetail, TopicDetail } from '@/types';
import { apiClient } from '@/lib/api';
import LessonContent from '@/components/LessonContent';
import CodeEditor from '@/components/CodeEditor';

export default function LessonPage() {
  const params = useParams();
  const router = useRouter();
  const topicId = params.topicId as string;
  const lessonId = params.lessonId as string;
  const mode = params.mode as string;
  
  const [lesson, setLesson] = useState<LessonDetail | null>(null);
  const [topic, setTopic] = useState<TopicDetail | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [lessonData, topicData] = await Promise.all([
          apiClient.getLessonDetail(`${topicId}/${lessonId}`),
          apiClient.getTopicDetail(topicId)
        ]);
        setLesson(lessonData);
        setTopic(topicData);
      } catch (err) {
        setError('Failed to load lesson');
        console.error('Error fetching lesson:', err);
      } finally {
        setLoading(false);
      }
    };

    if (topicId && lessonId) {
      fetchData();
    }
  }, [topicId, lessonId]);

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading lesson...</p>
        </div>
      </div>
    );
  }

  if (error || !lesson || !topic) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="text-red-600 text-xl mb-4">⚠️</div>
          <p className="text-gray-600">{error || 'Lesson not found'}</p>
        </div>
      </div>
    );
  }

  // Find the metadata for the current lesson (title, displayId) inside topic.lessons
  const currentLessonMeta = topic.lessons.find((l) => {
    const s = l.lessonId.includes('/') ? l.lessonId.split('/').pop()! : l.lessonId;
    return s === lessonId || l.lessonId === lessonId;
  });

  const currentLessonTitle = currentLessonMeta?.title ?? lessonId;

  const tabs = [
    // Use short lesson id (basename) for routing — lessonId param is expected to be the short id
    { id: 'overview', label: 'Overview', href: `/topics/${topicId}/${lessonId}/overview` },
    { id: 'solve', label: 'Solve', href: `/topics/${topicId}/${lessonId}/solve` },
  ];

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Breadcrumb removed: using global Breadcrumbs component in layout */}

        <div className="mb-6">
          <h1 className="text-3xl font-bold text-gray-900">{currentLessonTitle}</h1>
        </div>

        {/* Tabs */}
        <div className="mb-6">
          <div className="border-b border-gray-200">
            <nav className="-mb-px flex space-x-8">
              {tabs.map((tab) => (
                <Link
                  key={tab.id}
                  href={tab.href}
                  className={`py-2 px-1 border-b-2 font-medium text-sm ${
                    mode === tab.id
                      ? 'border-blue-500 text-blue-600'
                      : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                  }`}
                >
                  {tab.label}
                </Link>
              ))}
            </nav>
          </div>
        </div>

        {/* Content */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-1">
            <div className="bg-white rounded-lg shadow-sm border border-gray-200">
              <div className="p-4 border-b border-gray-200">
                <h3 className="text-lg font-semibold text-gray-900">Lessons</h3>
              </div>
              <div className="p-2">
                {topic.lessons.map((l) => {
                  const shortId = l.lessonId.includes('/') ? l.lessonId.split('/').pop()! : l.lessonId;
                  const isCurrent = shortId === lessonId || l.lessonId === lessonId;

                  return (
                    <Link
                      key={l.lessonId}
                      href={`/topics/${topicId}/${shortId}/overview`}
                      className={`block px-3 py-2 rounded-md text-sm transition-colors ${
                        isCurrent
                          ? 'bg-blue-100 text-blue-700'
                          : 'text-gray-700 hover:bg-gray-100'
                      }`}
                    >
                      <div className="font-medium">{l.title}</div>
                    </Link>
                  );
                })}
              </div>
            </div>
          </div>

          <div className="lg:col-span-2">
            {mode === 'overview' && <LessonContent lesson={lesson} />}
            {mode === 'solve' && <CodeEditor lesson={lesson} />}
          </div>
        </div>
      </div>
    </div>
  );
}
