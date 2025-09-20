export interface Topic {
  id: string;
  title: string;
  lessons_count: number;
}

export interface Lesson {
  displayId: string;
  lessonId: string;
  title: string;
}

export interface TopicDetail {
  id: string;
  title: string;
  readme: string;
  lessons: Lesson[];
}

export interface LessonDetail {
  id: string;
  readme: string;
  tasks: string[];
  tasks_source: string;
  has_tests: boolean;
}

export interface SubmitRequest {
  lesson_id: string;
  code: string;
}

export interface SubmitResponse {
  success: boolean;
  returncode: number;
  stdout: string;
  stderr: string;
}

export type ViewMode = 'topics' | 'overview' | 'solve';
