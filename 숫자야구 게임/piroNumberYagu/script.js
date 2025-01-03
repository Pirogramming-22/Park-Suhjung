let attempts = 9;
let randomNumbers = [];
let strikes = 0;
let balls = 0;

function getRandomNumbers() {
    const num = new Set();
    while (num.size < 3) {
        const randomNum = Math.floor(Math.random() * 10);
        num.add(randomNum);
    }
    return Array.from(num);
}

function init() {
    attempts = 9;
    randomNumbers = getRandomNumbers();

    document.getElementById('results').innerHTML = '';
    document.querySelector('.submit-button').disabled = false;
    document.getElementById('game-result-img').src = '';
    ['number1', 'number2', 'number3'].forEach(id => {
        document.getElementById(id).value = '';
    });

    document.getElementById('attempts').innerText = attempts;
}

function calculateResult(inputs) {
    let strikes = 0;
    let balls = 0;

    for (let i = 0; i < 3; i++) {
        if (inputs[i] === randomNumbers[i]) {
            strikes++;
        } else if (randomNumbers.includes(inputs[i])) {
            balls++;
        }
    }

    return { strikes, balls }; 
    
}

function updateHTML(inputNumbers, result) {
    const resultString = (result.strikes === 0 && result.balls === 0)
        ? '<span class="num-result out">O</span>'
        : `${result.strikes} <span class="num-result strike">S</span> ${result.balls} <span class="num-result ball">B</span>`;

    const numResult = document.createElement('span');
    numResult.className = 'num-result';
    numResult.innerText = inputNumbers.join(' ');

    const resultDivider = document.createElement('span');
    resultDivider.innerText = ':';

    const checkResult = document.createElement('span');
    checkResult.className = 'num-result';
    checkResult.innerHTML = resultString;

    const resultContainer = document.createElement('div');
    resultContainer.className = 'check-result';
    resultContainer.appendChild(numResult);
    resultContainer.appendChild(resultDivider);
    resultContainer.appendChild(checkResult);

    document.getElementById('results').appendChild(resultContainer);
}

function checkNumbers() {
    const input1 = parseInt(document.getElementById('number1').value);
    const input2 = parseInt(document.getElementById('number2').value);
    const input3 = parseInt(document.getElementById('number3').value);

    if (isNaN(input1) || isNaN(input2) || isNaN(input3)) {
        alert('모든 숫자를 입력하세요!');
        return;
    }

    const inputs = [input1, input2, input3];
    const result = calculateResult(inputs);

    updateHTML(inputs, result);

    if (result.strikes === 3) {
        document.getElementById('game-result-img').src = './success.png';
        document.querySelector('.submit-button').disabled = true;
        return;
    }

    attempts--;
    document.getElementById('attempts').innerText = attempts;

    if (attempts === 0) {
        document.getElementById('game-result-img').src = './fail.png';
        document.querySelector('.submit-button').disabled = true;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    init();
    document.querySelector('.submit-button').addEventListener('click', checkNumbers);
});
