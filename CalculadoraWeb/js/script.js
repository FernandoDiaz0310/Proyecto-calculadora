const valorA = document.getElementById('valorA');
const valorB = document.getElementById('valorB');
const resultado = document.getElementById('resultado');
const errorMessage = document.getElementById('errorMessage');
const buttons = document.querySelectorAll('[data-op]');

const showError = message => {
    errorMessage.textContent = message;
    resultado.textContent = '--';
};

const clearError = () => {
    errorMessage.textContent = '';
};

const parseNumber = value => {
    const number = Number(value);
    return Number.isFinite(number) ? number : null;
};

const calculate = operation => {
    clearError();
    const a = parseNumber(valorA.value);
    const b = parseNumber(valorB.value);

    if (a === null) {
        showError('Ingresa un primer número válido.');
        return;
    }

    if (operation !== 'raiz' && b === null) {
        showError('Ingresa un segundo número válido.');
        return;
    }

    let value;

    switch (operation) {
        case 'sumar':
            value = a + b;
            break;
        case 'restar':
            value = a - b;
            break;
        case 'multiplicar':
            value = a * b;
            break;
        case 'dividir':
            if (b === 0) {
                showError('Error: No se puede dividir entre cero.');
                return;
            }
            value = a / b;
            break;
        case 'potencia':
            value = Math.pow(a, b);
            break;
        case 'raiz':
            if (a < 0) {
                showError('Error: La raíz cuadrada de un número negativo no es válida.');
                return;
            }
            value = Math.sqrt(a);
            break;
        default:
            showError('Operación no reconocida.');
            return;
    }

    resultado.textContent = Number.isFinite(value) ? value : 'NaN';
};

buttons.forEach(button => {
    button.addEventListener('click', () => calculate(button.dataset.op));
});
