# Python Lessons Platform

Complete Python learning platform with interactive coding exercises, built with FastAPI backend and Next.js frontend.

## 🚀 Features

- **70+ Interactive Lessons**: From Python basics to advanced topics
- **Real-time Code Testing**: Submit solutions and get instant feedback
- **Modern UI**: Beautiful, responsive interface built with Next.js and Tailwind CSS
- **Progressive Learning**: Organized topics with clear learning paths
- **Code Editor**: Monaco Editor with Python syntax highlighting
- **Automated Testing**: pytest-based validation of student solutions

## 📚 Learning Topics

- **Python Basics**: Variables, functions, loops, data structures
- **Modules & Error Handling**: Imports, exceptions, debugging
- **OOP & Iterators**: Classes, inheritance, generators
- **Asyncio & Concurrency**: Async programming, coroutines
- **Testing & Best Practices**: Unit testing, code quality
- **SQLAlchemy ORM**: Database operations and relationships
- **FastAPI**: Modern web API development

## 🏗️ Architecture

### Backend (FastAPI)
- RESTful API with automatic documentation
- CORS support for frontend integration
- pytest-based code testing
- Support for both old and new lesson formats

### Frontend (Next.js)
- Modern React with TypeScript
- Tailwind CSS for styling
- Monaco Editor for code editing
- Responsive design for all devices

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- npm or yarn

### Backend Setup

```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows PowerShell

# Install dependencies
pip install -r requirements.txt

# Start API server
uvicorn server.main:app --reload --port 8000
```

### Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### Access the Platform
- **Frontend**: http://localhost:3000
- **API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 📁 Project Structure

```
python_lessions/
├── server/                 # FastAPI backend
│   └── main.py            # API server
├── frontend/              # Next.js frontend
│   ├── src/
│   │   ├── app/          # Pages and routing
│   │   ├── components/   # React components
│   │   ├── lib/          # API client
│   │   └── types/        # TypeScript types
│   └── README.md         # Frontend documentation
├── python_lessions/       # Learning content
│   ├── topics/           # Topic definitions
│   ├── basics/           # Basic Python lessons
│   ├── asyncio/          # Async programming
│   ├── fastapi/          # FastAPI lessons
│   └── ...               # Other topics
└── requirements.txt       # Python dependencies
```

## 🔧 API Endpoints

- `GET /` - API information
- `GET /api/topics` - List all topics
- `GET /api/topics/{topic_id}` - Get topic details
- `GET /api/lessons/{lesson_id}` - Get lesson details
- `POST /api/submit` - Submit code for testing

## 🛡️ Security

- Code execution in isolated temporary directories
- Input validation and sanitization
- CORS configuration for frontend integration
- **Note**: Do not expose publicly without proper sandboxing

## 🚀 Deployment

### Backend
- Deploy to any Python hosting (Heroku, Railway, AWS)
- Set environment variables for production
- Consider adding authentication and rate limiting

### Frontend
- Deploy to Vercel, Netlify, or similar
- Set `NEXT_PUBLIC_API_URL` environment variable
- Build optimized production bundle

## 📖 Documentation

- [Frontend Documentation](frontend/README.md)
- [API Documentation](http://localhost:8000/docs) (when running)
- [Lesson Content](python_lessions/) - Browse learning materials

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add new lessons or improve existing content
4. Test your changes
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

