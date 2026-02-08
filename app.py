"""
Flask web application for the calculator.
Serves the frontend and provides API endpoints for calculations.
"""

from flask import Flask, render_template, request, jsonify
from calculator import Calculator

app = Flask(__name__)
calc = Calculator()


@app.route('/')
def index():
    """Serve the calculator homepage."""
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    """Handle calculation requests from the frontend."""
    try:
        data = request.get_json()
        
        # Check if it's a unary operation (single number, like sin, cos, sqrt, etc.)
        if 'function' in data and data['function']:
            function_name = data['function']
            num = float(data.get('num'))
            
            # Handle single-operand functions
            if function_name == 'sin':
                angle_mode = data.get('angleMode', 'deg')
                result = calc.sin_deg(num) if angle_mode == 'deg' else calc.sin_rad(num)
            elif function_name == 'cos':
                angle_mode = data.get('angleMode', 'deg')
                result = calc.cos_deg(num) if angle_mode == 'deg' else calc.cos_rad(num)
            elif function_name == 'tan':
                angle_mode = data.get('angleMode', 'deg')
                result = calc.tan_deg(num) if angle_mode == 'deg' else calc.tan_rad(num)
            elif function_name == 'asin':
                angle_mode = data.get('angleMode', 'deg')
                result = calc.asin_deg(num) if angle_mode == 'deg' else calc.asin_rad(num)
            elif function_name == 'acos':
                angle_mode = data.get('angleMode', 'deg')
                result = calc.acos_deg(num) if angle_mode == 'deg' else calc.acos_rad(num)
            elif function_name == 'atan':
                angle_mode = data.get('angleMode', 'deg')
                result = calc.atan_deg(num) if angle_mode == 'deg' else calc.atan_rad(num)
            elif function_name == 'sinh':
                result = calc.sinh(num)
            elif function_name == 'cosh':
                result = calc.cosh(num)
            elif function_name == 'tanh':
                result = calc.tanh(num)
            elif function_name == 'log10':
                result = calc.log10(num)
            elif function_name == 'ln':
                result = calc.ln(num)
            elif function_name == 'sqrt':
                result = calc.sqrt(num)
            elif function_name == 'cbrt':
                result = calc.cbrt(num)
            elif function_name == 'square':
                result = calc.square(num)
            elif function_name == 'cube':
                result = calc.cube(num)
            elif function_name == 'reciprocal':
                result = calc.reciprocal(num)
            elif function_name == 'factorial':
                result = calc.factorial(int(num))
            elif function_name == 'abs':
                result = calc.absolute(num)
            elif function_name == 'negate':
                result = calc.negate(num)
            elif function_name == 'pi':
                result = calc.get_pi()
            elif function_name == 'e':
                result = calc.get_e()
            else:
                return jsonify({'error': f'Unknown function: {function_name}', 'result': None}), 400
            
            return jsonify({'result': result, 'error': None})
        
        # Binary operations
        num1 = float(data.get('num1'))
        operator = data.get('operator')
        num2 = float(data.get('num2'))
        
        # Perform the calculation
        if operator == '+':
            result = calc.add(num1, num2)
        elif operator == '-':
            result = calc.subtract(num1, num2)
        elif operator == '*':
            result = calc.multiply(num1, num2)
        elif operator == '/':
            result = calc.divide(num1, num2)
        elif operator == '**':
            result = calc.power(num1, num2)
        elif operator == '%':
            result = calc.modulo(num1, num2)
        else:
            return jsonify({'error': f'Unknown operator: {operator}'}), 400
        
        return jsonify({'result': result, 'error': None})
    
    except ValueError as e:
        return jsonify({'error': str(e), 'result': None}), 400
    except Exception as e:
        return jsonify({'error': f'Invalid input: {str(e)}', 'result': None}), 400


if __name__ == '__main__':
    print("Starting Calculator Web App...")
    print("Open your browser and go to: http://localhost:5000")
    app.run(debug=True, port=5000)
