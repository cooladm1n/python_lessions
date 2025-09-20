# Python Lessons Frontend

Modern Next.js frontend for the Python learning platform with interactive coding exercises.

## Features

- **Modern UI**: Built with Next.js 15, TypeScript, and Tailwind CSS
- **Interactive Code Editor**: Monaco Editor with Python syntax highlighting
- **Responsive Design**: Mobile-first design that works on all devices
- **Real-time Testing**: Submit code and get instant feedback
- **Progressive Learning**: Organized topics and lessons with clear navigation

## Tech Stack

- **Framework**: Next.js 15 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Code Editor**: Monaco Editor (VS Code editor)
- **HTTP Client**: Axios
- **Markdown**: React Markdown

## Getting Started

### Prerequisites

- Node.js 18+ 
- npm or yarn
- Backend API running on http://localhost:8000

### Installation

```bash
# Install dependencies
npm install

# Start development server
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.

### Build for Production

```bash
# Build the application
npm run build

# Start production server
npm start
```

## Project Structure

```
src/
├── app/                    # Next.js App Router pages
│   ├── page.tsx           # Home page
│   ├── layout.tsx         # Root layout
│   └── topics/            # Topic and lesson pages
├── components/            # React components
│   ├── TopicList.tsx      # Topics sidebar
│   ├── LessonList.tsx     # Lessons sidebar
│   ├── LessonContent.tsx  # Lesson content display
│   └── CodeEditor.tsx     # Code editor with testing
├── lib/                   # Utilities and API client
│   └── api.ts            # API client for backend
└── types/                # TypeScript type definitions
    └── index.ts          # Shared types
```

## API Integration

The frontend communicates with the Python backend API:

- `GET /api/topics` - List all topics
- `GET /api/topics/{id}` - Get topic details
- `GET /api/lessons/{id}` - Get lesson details
- `POST /api/submit` - Submit code for testing

## Development

### Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run start` - Start production server
- `npm run lint` - Run ESLint

### Environment Variables

Create `.env.local` file:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Features Overview

### 1. Topic Navigation
- Browse all available topics
- See lesson count for each topic
- Clean, organized sidebar

### 2. Lesson Management
- View lesson content with markdown rendering
- Switch between Overview and Solve modes
- Breadcrumb navigation

### 3. Code Editor
- Monaco Editor with Python syntax highlighting
- Auto-completion and error detection
- Run tests button with real-time feedback
- Pre-filled with task templates

### 4. Testing Integration
- Submit code to backend for testing
- View test results (pass/fail)
- Display output and error messages
- Real-time feedback

## Deployment

The frontend can be deployed to any platform that supports Next.js:

- **Vercel** (recommended)
- **Netlify**
- **AWS Amplify**
- **Docker**

Make sure to set the `NEXT_PUBLIC_API_URL` environment variable to point to your backend API.