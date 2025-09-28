'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import { Topic } from '@/types';
import { apiClient } from '@/lib/api';
import TopicList from '@/components/TopicList';

export default function HomePage() {
  const [topics, setTopics] = useState<Topic[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const router = useRouter();

  useEffect(() => {
    const fetchTopics = async () => {
      try {
        const data = await apiClient.getTopics();
        setTopics(data);
        // NOTE: previously we automatically redirected to the first topic here
        // (router.push(`/topics/${data[0].id}`)). That caused an immediate
        // navigation from `/` to `/topics/...`. We removed the automatic
        // redirect so users stay on the landing page and choose a topic.
      } catch (err) {
        setError('Failed to load topics');
        console.error('Error fetching topics:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchTopics();
  }, [router]);

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
          <p className="text-gray-600">Loading...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <div className="text-red-600 text-xl mb-4">⚠️</div>
          <p className="text-gray-600">{error}</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900">Python Lessons</h1>
          <p className="mt-2 text-gray-600">
            Learn Python programming with interactive lessons and hands-on coding exercises.
          </p>
        </div>
        
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <div className="lg:col-span-1">
            <TopicList topics={topics} />
          </div>
          
          <div className="lg:col-span-2">
            <div className="bg-white rounded-lg shadow-sm border border-gray-200 p-8 text-center">
              <div className="text-6xl mb-4">🐍</div>
              <h2 className="text-2xl font-semibold text-gray-900 mb-4">
                Welcome to Python Lessons
              </h2>
              <p className="text-gray-600 mb-6">
                Select a topic from the sidebar to start learning Python programming.
                Each topic contains multiple lessons with hands-on coding exercises.
              </p>
              <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
                <div className="p-4 bg-blue-50 rounded-lg">
                  <div className="font-semibold text-blue-900">Interactive</div>
                  <div className="text-blue-700">Code and test your solutions</div>
                </div>
                <div className="p-4 bg-green-50 rounded-lg">
                  <div className="font-semibold text-green-900">Progressive</div>
                  <div className="text-green-700">From basics to advanced topics</div>
                </div>
                <div className="p-4 bg-purple-50 rounded-lg">
                  <div className="font-semibold text-purple-900">Comprehensive</div>
                  <div className="text-purple-700">70+ lessons across 7 topics</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}