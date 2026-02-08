# Scientific Calculator - Project Instructions

## Project Overview
A comprehensive scientific calculator application with both basic arithmetic and advanced scientific functions. Features include:
- Web interface with two modes (Basic and Scientific)
- Real-time calculations with error handling
- Calculation history with browser storage
- Support for 30+ mathematical functions
- Degree/Radian toggle for trigonometric functions
- RESTful API for calculations

## Features by Category

### Basic Operations
- Addition, Subtraction, Multiplication, Division
- Power (exponentiation) and Modulo operations

### Trigonometric Functions
- sin, cos, tan (with degree/radian toggle)
- asin, acos, atan (inverse functions)
- Hyperbolic: sinh, cosh, tanh

### Logarithmic & Exponential
- ln (natural logarithm)
- log₁₀ (base-10 logarithm)
- Constants: π and e

### Power & Root Functions
- Square (x²) and Cube (x³)
- Square root (√x) and Cube root (∛x)
- Reciprocal (1/x)

### Other Functions
- Factorial (x!)
- Absolute value (|x|)
- Negation (±)

## Technology Stack
- **Backend**: Python 3.12+, Flask 2.3.3+
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Storage**: Browser localStorage for calculation history
- **Architecture**: REST API + Single Page Application

## Project Structure
```
calculator/
├── app.py                    # Flask server & API endpoints
├── calculator.py             # Core calculation logic
├── requirements.txt          # Python dependencies
├── README.md                 # User documentation
├── templates/
│   └── index.html            # Web UI with tabs (Basic/Scientific)
├── static/
│   ├── style.css             # Responsive styling, gradients, animations
│   └── script.js             # Tab switching, API calls, history management
└── .github/
    └── copilot-instructions.md  # This file
```

## Key Implementation Details

### Calculator Class (calculator.py)
- **Static methods** for all operations (no state needed)
- **Error handling** for domain errors (log, sqrt, trig inverse)
- **Degree/Radian support** duplicated methods (sin_deg, sin_rad)
- **Math library integration** for precise calculations

### Flask API (app.py)
- **POST /calculate** endpoint handles both types:
  - Binary operations (num1, operator, num2)
  - Unary functions (function, num, angleMode)
- **JSON request/response** format
- **Comprehensive error handling** with descriptive messages

### Frontend Architecture (script.js)
- **Tab-based UI** switching between Basic and Scientific modes
- **Real-time display** showing current expression
- **Event delegation** for function buttons
- **localStorage** for persistent history across sessions
- **Responsive design** working on desktop and mobile

## API Endpoints

### Calculate Endpoint
```
POST /calculate
Content-Type: application/json

# Binary Operation Request
{
  "num1": number,
  "operator": "+|-|*|/|**|%",
  "num2": number
}

# Scientific Function Request
{
  "function": "sin|cos|tan|asin|acos|atan|sinh|cosh|tanh|ln|log10|sqrt|cbrt|square|cube|reciprocal|factorial|abs|negate|pi|e",
  "num": number,  // optional for pi and e
  "angleMode": "deg|rad"  // for trigonometric functions
}
```

## Development Guidelines

### Code Style
- Follow PEP 8 for Python
- Use descriptive function names
- Include docstrings for all functions
- Add comments for complex logic

### Adding New Functions
1. Add static method to Calculator class
2. Add endpoint handler in app.py
3. Add button to HTML UI
4. Add JavaScript function call handler

### Testing
Run scientific function tests:
```bash
python -c "
from calculator import Calculator
import math
calc = Calculator()
print('sin(30°):', calc.sin_deg(30))
print('√16:', calc.sqrt(16))
print('5!:', calc.factorial(5))
"
```

## Browser Compatibility
- Chrome 60+, Firefox 55+, Safari 12+, Edge 79+
- Mobile-responsive design
- Cross-browser CSS3 support
- ES6 JavaScript (transpile if needed for older browsers)

## Performance Considerations
- Lightweight codebase (~400 lines total)
- No external JavaScript libraries
- CSS animations use GPU acceleration
- Single-page application (no page reloads)
- Efficient localStorage management (max 20 items)

## Security Notes
- Input validation on both frontend and backend
- No eval() or dynamic code execution
- Safe JSON serialization/deserialization
- CORS headers if API used externally

## Future Enhancement Ideas
- Complex number support
- Matrix operations
- Calculus operations (derivatives, integrals)
- Graph plotting for functions
- Unit conversion
- More logarithm bases
- Programming functions (AND, OR, XOR, etc.)
- Export calculation history as CSV/PDF
