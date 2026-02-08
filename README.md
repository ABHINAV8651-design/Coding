# Scientific Calculator

A modern Python calculator application with both basic and advanced scientific functions. Features a beautiful web interface with real-time calculations and calculation history.

## Features

### Basic Operations
- **Addition** (+): Add two numbers
- **Subtraction** (-): Subtract two numbers  
- **Multiplication** (×): Multiply two numbers
- **Division** (÷): Divide two numbers
- **Power** (^): Raise a number to a power
- **Modulo** (%): Get the remainder of division

### Scientific Functions

#### Trigonometric Functions
- **sin, cos, tan**: Basic trigonometric functions
- **asin, acos, atan**: Inverse trigonometric functions
- **Mode Toggle**: Switch between Degrees and Radians

#### Hyperbolic Functions
- **sinh, cosh, tanh**: Hyperbolic trigonometric functions

#### Logarithmic Functions
- **ln**: Natural logarithm (base e)
- **log₁₀**: Base-10 logarithm

#### Power & Root Functions
- **x²**: Square a number
- **x³**: Cube a number
- **√x**: Square root
- **∛x**: Cube root
- **1/x**: Reciprocal function

#### Other Functions
- **|x|**: Absolute value
- **±**: Negation (toggle sign)
- **x!**: Factorial

#### Constants
- **π (Pi)**: 3.14159...
- **e (Euler's number)**: 2.71828...

## Requirements

- Python 3.6 or higher
- Flask 2.3.3+

## Installation

1. Clone or download the project
   ```bash
   git clone <repository-url>
   cd calculator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Web Interface (Recommended)

Run the Flask web server:

```bash
python app.py
```

Then open your browser and navigate to: **http://localhost:5000**

#### Web Interface Features

**Two Modes:**
1. **Basic Mode** - Standard arithmetic operations
   - Input two numbers and select an operator
   - Click "Calculate" or press Enter
   
2. **Scientific Mode** - Advanced mathematical functions
   - Input a single number (or none for constants)
   - Click any function button to execute
   - Toggle between Degrees and Radians for trigonometric functions

**Calculation History:**
- Automatically stores your last 20 calculations
- Click any history item to reload it into the calculator
- Clear history anytime with the "Clear History" button
- History persists between browser sessions

### Command-Line Interface

Run the calculator in the terminal:

```bash
python calculator.py
```

Example usage:
```
Enter expression (e.g., 10 + 5): 10 + 5
Result: 15

Enter expression (e.g., 10 + 5): 20 - 8
Result: 12
```

## API Endpoint

The web server provides a REST API for calculations:

### Binary Operations
**POST** `/calculate`

Request body:
```json
{
  "num1": 10,
  "operator": "+",
  "num2": 5
}
```

Response:
```json
{
  "result": 15,
  "error": null
}
```

### Scientific Functions
**POST** `/calculate`

Request body (example with sine in degrees):
```json
{
  "function": "sin",
  "num": 30,
  "angleMode": "deg"
}
```

Response:
```json
{
  "result": 0.5,
  "error": null
}
```

## Error Handling

The calculator handles various errors gracefully:

- **Division by zero**: Prevents mathematical errors
- **Modulo by zero**: Prevents invalid operations
- **Invalid domains**: For functions like log, sqrt, asin/acos
- **Input validation**: Ensures numbers are properly formatted
- **User feedback**: Clear error messages displayed in the interface

## Project Structure

```
calculator/
├── app.py                    # Flask web server & API
├── calculator.py             # Core calculator logic
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── templates/
│   └── index.html            # Web interface (HTML)
├── static/
│   ├── style.css             # Styling & layout
│   └── script.js             # Frontend logic
└── .github/
    └── copilot-instructions.md
```

## Examples

### Basic Calculations (Web Interface)
- `5 + 3` = `8`
- `10 - 7` = `3`
- `4 × 5` = `20`
- `20 ÷ 4` = `5`
- `2 ^ 3` = `8`
- `17 % 5` = `2`

### Scientific Calculations (Web Interface)
- `sin(30°)` = `0.5`
- `cos(0°)` = `1`
- `tan(45°)` = `1`
- `√16` = `4`
- `ln(e)` = `1`
- `log₁₀(100)` = `2`
- `2³` = `8`
- `5!` = `120`

## Browser Compatibility

- Chrome 60+
- Firefox 55+
- Safari 12+
- Edge 79+

Works on desktop, tablet, and mobile devices (via responsive design)

## License

MIT
