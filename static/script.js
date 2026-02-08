/**
 * Scientific Calculator Frontend Script
 * Handles both basic and scientific calculations
 */

// DOM Elements - Basic Mode
const num1Input = document.getElementById('num1');
const operatorSelect = document.getElementById('operator');
const num2Input = document.getElementById('num2');
const calculateBtn = document.getElementById('calculateBtn');
const clearBtn = document.getElementById('clearBtn');

// DOM Elements - Scientific Mode
const sciNumInput = document.getElementById('sci-num');
const sciClearBtn = document.getElementById('sciClearBtn');
const angleBtns = document.querySelectorAll('.angle-btn');
const functionBtns = document.querySelectorAll('.btn-function');

// DOM Elements - Common
const displayInput = document.getElementById('display');
const resultSection = document.getElementById('result-section');
const resultDisplay = document.getElementById('resultDisplay');
const errorSection = document.getElementById('error-section');
const errorMessage = document.getElementById('errorMessage');
const historyList = document.getElementById('history');
const clearHistoryBtn = document.getElementById('clearHistoryBtn');
const tabBtns = document.querySelectorAll('.tab-btn');
const tabContents = document.querySelectorAll('.tab-content');

// State
let calculationHistory = JSON.parse(localStorage.getItem('calcHistory')) || [];
let currentAngleMode = 'deg';
let currentTab = 'basic';

// Initialize
document.addEventListener('DOMContentLoaded', () => {
    loadHistory();
    setupEventListeners();
});

/**
 * Setup all event listeners
 */
function setupEventListeners() {
    // Basic mode
    calculateBtn.addEventListener('click', performBasicCalculation);
    clearBtn.addEventListener('click', clearBasicInputs);
    num2Input.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') performBasicCalculation();
    });
    num1Input.addEventListener('change', updateBasicDisplay);
    operatorSelect.addEventListener('change', updateBasicDisplay);
    num2Input.addEventListener('change', updateBasicDisplay);
    
    // Scientific mode
    sciClearBtn.addEventListener('click', clearScientificInputs);
    sciNumInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter' && sciNumInput.value) {
            const firstBtn = document.querySelector('.btn-function[data-func="sin"]');
            if (firstBtn) firstBtn.click();
        }
    });
    sciNumInput.addEventListener('change', updateScientificDisplay);
    
    // Angle mode toggle
    angleBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            angleBtns.forEach(b => b.classList.remove('active'));
            e.target.classList.add('active');
            currentAngleMode = e.target.getAttribute('data-mode');
            updateScientificDisplay();
        });
    });
    
    // Scientific function buttons
    functionBtns.forEach(btn => {
        btn.addEventListener('click', performScientificCalculation);
    });
    
    // Tab switching
    tabBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const tab = e.target.getAttribute('data-tab');
            switchTab(tab);
        });
    });
    
    // Common
    clearHistoryBtn.addEventListener('click', clearHistory);
}

/**
 * Switch between tabs
 */
function switchTab(tab) {
    currentTab = tab;
    
    // Update tab buttons
    tabBtns.forEach(btn => {
        if (btn.getAttribute('data-tab') === tab) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });
    
    // Update tab contents
    tabContents.forEach(content => {
        if (content.id === `${tab}-tab`) {
            content.classList.add('active');
        } else {
            content.classList.remove('active');
        }
    });
}

/**
 * Update basic mode display
 */
function updateBasicDisplay() {
    const num1 = num1Input.value || '0';
    const operator = operatorSelect.value;
    const num2 = num2Input.value || '0';
    
    const operatorSymbols = {
        '+': '+',
        '-': '-',
        '*': '×',
        '/': '÷',
        '**': '^',
        '%': '%'
    };
    
    displayInput.value = `${num1} ${operatorSymbols[operator]} ${num2}`;
}

/**
 * Update scientific mode display
 */
function updateScientificDisplay() {
    const num = sciNumInput.value || '0';
    const modeLabel = currentAngleMode === 'deg' ? '°' : 'rad';
    displayInput.value = `${num} ${modeLabel}`;
}

/**
 * Perform basic calculation
 */
async function performBasicCalculation() {
    hideError();
    resultSection.style.display = 'none';
    
    if (!num1Input.value || !num2Input.value) {
        showError('Please enter both numbers');
        return;
    }
    
    try {
        const num1 = parseFloat(num1Input.value);
        const num2 = parseFloat(num2Input.value);
        const operator = operatorSelect.value;
        
        if (isNaN(num1) || isNaN(num2)) {
            showError('Please enter valid numbers');
            return;
        }
        
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ num1, operator, num2 })
        });
        
        const data = await response.json();
        
        if (data.error) {
            showError(data.error);
        } else {
            const operatorSymbols = {
                '+': '+', '-': '-', '*': '×', '/': '÷', '**': '^', '%': '%'
            };
            displayBasicResult(data.result, num1, operator, num2);
            addToHistory(`${num1} ${operatorSymbols[operator]} ${num2}`, data.result);
        }
    } catch (error) {
        showError('An error occurred. Please try again.');
        console.error('Error:', error);
    }
}

/**
 * Perform scientific calculation
 */
async function performScientificCalculation(e) {
    hideError();
    resultSection.style.display = 'none';
    
    const functionName = e.target.getAttribute('data-func');
    
    if (!sciNumInput.value && functionName !== 'pi' && functionName !== 'e') {
        showError('Please enter a number');
        return;
    }
    
    try {
        const num = functionName === 'pi' || functionName === 'e' 
            ? null 
            : parseFloat(sciNumInput.value);
        
        if ((functionName !== 'pi' && functionName !== 'e') && isNaN(num)) {
            showError('Please enter a valid number');
            return;
        }
        
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                function: functionName,
                num: num,
                angleMode: currentAngleMode
            })
        });
        
        const data = await response.json();
        
        if (data.error) {
            showError(data.error);
        } else {
            displayScientificResult(data.result, functionName, num);
            addToHistory(`${functionName}(${num})`, data.result);
        }
    } catch (error) {
        showError('An error occurred. Please try again.');
        console.error('Error:', error);
    }
}

/**
 * Display basic calculation result
 */
function displayBasicResult(result, num1, operator, num2) {
    let formattedResult = result;
    if (typeof result === 'number') {
        formattedResult = Math.round(result * 10000000000) / 10000000000;
    }
    
    displayInput.value = formattedResult;
    resultDisplay.textContent = formattedResult;
    resultSection.style.display = 'block';
    resultSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/**
 * Display scientific calculation result
 */
function displayScientificResult(result, functionName, num) {
    let formattedResult = result;
    if (typeof result === 'number') {
        formattedResult = Math.round(result * 10000000000) / 10000000000;
    }
    
    displayInput.value = formattedResult;
    resultDisplay.textContent = formattedResult;
    resultSection.style.display = 'block';
    resultSection.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

/**
 * Show error message
 */
function showError(message) {
    errorMessage.textContent = message;
    errorSection.style.display = 'block';
}

/**
 * Hide error message
 */
function hideError() {
    errorSection.style.display = 'none';
    errorMessage.textContent = '';
}

/**
 * Clear basic mode inputs
 */
function clearBasicInputs() {
    num1Input.value = '';
    num2Input.value = '';
    displayInput.value = '0';
    operatorSelect.value = '+';
    resultSection.style.display = 'none';
    hideError();
    num1Input.focus();
}

/**
 * Clear scientific mode inputs
 */
function clearScientificInputs() {
    sciNumInput.value = '';
    displayInput.value = '0';
    resultSection.style.display = 'none';
    hideError();
    sciNumInput.focus();
}

/**
 * Add calculation to history
 */
function addToHistory(expression, result) {
    const calculation = {
        expression: expression,
        result: result,
        timestamp: new Date().toLocaleTimeString()
    };
    
    calculationHistory.unshift(calculation);
    
    if (calculationHistory.length > 20) {
        calculationHistory.pop();
    }
    
    localStorage.setItem('calcHistory', JSON.stringify(calculationHistory));
    loadHistory();
}

/**
 * Load and display history
 */
function loadHistory() {
    historyList.innerHTML = '';
    
    if (calculationHistory.length === 0) {
        historyList.innerHTML = '<li style="color: #999;">No calculations yet</li>';
        return;
    }
    
    calculationHistory.forEach((calc) => {
        const li = document.createElement('li');
        li.innerHTML = `
            <span style="font-weight: 600;">${calc.expression}</span> = 
            <span style="color: #667eea; font-weight: 700;">${calc.result}</span>
            <span style="float: right; font-size: 12px; color: #999;">${calc.timestamp}</span>
        `;
        li.style.cursor = 'pointer';
        li.addEventListener('click', () => {
            // Load into scientific or basic mode
            if (calc.expression.includes('(')) {
                // Scientific function format
                switchTab('scientific');
                const match = calc.expression.match(/(\w+)\((.*?)\)/);
                if (match) {
                    sciNumInput.value = parseFloat(match[2]) || 0;
                    updateScientificDisplay();
                }
            } else {
                // Basic operation format
                switchTab('basic');
                const parts = calc.expression.split(' ');
                if (parts.length >= 3) {
                    num1Input.value = parseFloat(parts[0]);
                    operatorSelect.value = getOperatorValue(parts[1]);
                    num2Input.value = parseFloat(parts.slice(2).join(''));
                    updateBasicDisplay();
                }
            }
        });
        historyList.appendChild(li);
    });
}

/**
 * Map operator symbol to value
 */
function getOperatorValue(symbol) {
    const map = {
        '+': '+',
        '-': '-',
        '×': '*',
        '÷': '/',
        '^': '**',
        '%': '%'
    };
    return map[symbol] || '+';
}

/**
 * Clear calculation history
 */
function clearHistory() {
    if (confirm('Are you sure you want to clear the calculation history?')) {
        calculationHistory = [];
        localStorage.removeItem('calcHistory');
        loadHistory();
    }
}
