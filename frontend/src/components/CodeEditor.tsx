'use client';

import { useState, useEffect } from 'react';
import { Editor } from '@monaco-editor/react';
import { LessonDetail, SubmitResponse } from '@/types';
import { apiClient } from '@/lib/api';

interface CodeEditorProps {
  lesson: LessonDetail;
  onResult?: (result: SubmitResponse) => void;
}

export default function CodeEditor({ lesson, onResult }: CodeEditorProps) {
  const [code, setCode] = useState(lesson.tasks_source);
  const [isRunning, setIsRunning] = useState(false);
  const [result, setResult] = useState<SubmitResponse | null>(null);

  useEffect(() => {
    setCode(lesson.tasks_source);
    setResult(null);
  }, [lesson.tasks_source]);

  const handleRun = async () => {
    if (!code.trim()) return;

    setIsRunning(true);
    try {
      const response = await apiClient.submitCode({
        lesson_id: lesson.id,
        code: code,
      });
      setResult(response);
      onResult?.(response);
    } catch (error) {
      console.error('Error submitting code:', error);
      setResult({
        success: false,
        returncode: 1,
        stdout: '',
        stderr: 'Error submitting code: ' + (error as Error).message,
      });
    } finally {
      setIsRunning(false);
    }
  };

  return (
    <div className="bg-white rounded-lg shadow-sm border border-gray-200">
      <div className="p-4 border-b border-gray-200">
        <div className="flex justify-between items-center">
          <h3 className="text-lg font-semibold text-gray-900">Code Editor</h3>
          <button
            onClick={handleRun}
            disabled={isRunning || !code.trim()}
            className="px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
          >
            {isRunning ? 'Running...' : 'Run Tests'}
          </button>
        </div>
      </div>
      
      <div className="h-96">
        <Editor
          height="100%"
          defaultLanguage="python"
          value={code}
          onChange={(value) => setCode(value || '')}
          theme="vs-dark"
          options={{
            minimap: { enabled: false },
            fontSize: 14,
            lineNumbers: 'on',
            roundedSelection: false,
            scrollBeyondLastLine: false,
            automaticLayout: true,
          }}
        />
      </div>

      {result && (
        <div className="p-4 border-t border-gray-200">
          <div className="flex items-center mb-2">
            <div
              className={`w-3 h-3 rounded-full mr-2 ${
                result.success ? 'bg-green-500' : 'bg-red-500'
              }`}
            />
            <span className="font-medium">
              {result.success ? 'Tests Passed' : 'Tests Failed'}
            </span>
            <span className="ml-2 text-sm text-gray-500">
              (Exit code: {result.returncode})
            </span>
          </div>
          
          {result.stdout && (
            <div className="mb-2">
              <div className="text-sm font-medium text-gray-700 mb-1">Output:</div>
              <pre className="bg-gray-100 p-3 rounded text-sm font-mono text-gray-800 whitespace-pre-wrap">
                {result.stdout}
              </pre>
            </div>
          )}
          
          {result.stderr && (
            <div>
              <div className="text-sm font-medium text-gray-700 mb-1">Errors:</div>
              <pre className="bg-red-50 p-3 rounded text-sm font-mono text-red-800 whitespace-pre-wrap">
                {result.stderr}
              </pre>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
