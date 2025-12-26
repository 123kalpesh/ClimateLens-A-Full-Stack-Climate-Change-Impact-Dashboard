# ClimatePulse Dashboard

A professional climate change analytics dashboard built with FastAPI backend and React frontend.

## Features

- 📊 Interactive climate data visualization
- 🌍 Country-specific temperature and CO2 trends
- 🔮 Temperature forecasting using machine learning
- 🚨 Climate anomaly alerts
- 🗺️ Interactive maps
- 📱 Responsive design

## Tech Stack

- **Backend**: FastAPI, SQLAlchemy, Pandas, Scikit-learn
- **Frontend**: React, Recharts, React Router, Axios
- **Database**: SQLite (development), configurable for production
- **Styling**: Custom CSS with glassmorphism effects

## Quick Start

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd climate-dashboard
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

3. **Frontend Setup** (in a new terminal)
   ```bash
   cd frontend/my-app
   npm install
   npm start
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Documentation: http://localhost:8000/docs

## API Endpoints

- `GET /api/health` - Health check
- `GET /api/climate/temperature` - Temperature data
- `GET /api/climate/co2` - CO2 emissions data
- `GET /api/climate/alerts` - Climate alerts
- `GET /api/forecast/temperature` - Temperature forecast

## Project Structure

```
climate-dashboard/
├── backend/
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── core/         # Configuration
│   │   ├── db/           # Database models
│   │   ├── models/       # SQLAlchemy models
│   │   ├── schemas/      # Pydantic schemas
│   │   ├── services/     # Business logic
│   │   └── utils/        # Utilities
│   └── data/             # Sample data
├── frontend/
│   └── my-app/
│       ├── public/       # Static assets
│       ├── src/
│       │   ├── components/  # Reusable components
│       │   ├── hooks/       # Custom hooks
│       │   ├── pages/       # Page components
│       │   └── services/    # API services
│       └── package.json
└── README.md
```

## Development

### Running Tests
```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend/my-app
npm test
```

### Building for Production
```bash
# Frontend
cd frontend/my-app
npm run build

# Backend (using Docker)
docker build -t climate-dashboard .
docker run -p 8000:8000 climate-dashboard
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Contact

For questions or support, please open an issue on GitHub.