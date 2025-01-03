let timerInterval;
let timeInSeconds = 0;
let timeInHundredths = 0;
let isRunning = false;
let records = [];

const timeDisplay = document.querySelector('.time');
const recordList = document.querySelector('.record-list');
const btnStart = document.querySelector('.btn_start');
const btnStop = document.querySelector('.btn_stop');
const btnReset = document.querySelector('.btn_reset');

function Start() {
    if (!isRunning) {
        isRunning = true;
        timerInterval = setInterval(updateTime, 10);
    }
}

function Stop() {
    if (isRunning) {
        clearInterval(timerInterval);
        isRunning = false;
        records.push({ seconds: timeInSeconds, hundredths: timeInHundredths });
        updateRecordList();
    }
}

function Clear() {
    clearInterval(timerInterval);
    isRunning = false;
    timeInSeconds = 0;
    timeInHundredths = 0;
    timeDisplay.textContent = formatTime(timeInSeconds, timeInHundredths);
}

function updateTime() {
    timeInHundredths++;
    if (timeInHundredths >= 100) {
        timeInHundredths = 0;
        timeInSeconds++;
    }
    timeDisplay.textContent = formatTime(timeInSeconds, timeInHundredths);
}

function formatTime(seconds, hundredths) {
    return `${padZero(seconds)}:${padZero(hundredths)}`;
}

function padZero(num) {
    return num < 10 ? `0${num}` : num;
}

function updateRecordList() {
    recordList.innerHTML = '';
    records.forEach((record, index) => {
        const recordItem = document.createElement('div');
        recordItem.classList.add('record-item');
        
        const checkbox = document.createElement('input');
        checkbox.type = 'checkbox';
        checkbox.id = `record-${index}`;
        checkbox.classList.add('record-checkbox');
        
        checkbox.addEventListener('change', (e) => {
            if (e.target.checked) {
                console.log(`Selected Record: ${formatTime(record.seconds, record.hundredths)}`);
            } else {
                console.log(`Deselected Record: ${formatTime(record.seconds, record.hundredths)}`);
            }
        });

        const label = document.createElement('label');
        label.setAttribute('for', `record-${index}`);
        label.textContent = formatTime(record.seconds, record.hundredths);
        
        recordItem.appendChild(checkbox);
        recordItem.appendChild(label);
        
        recordList.appendChild(recordItem);
    });

    updateSelectAllCheckbox();
}

const selectAllCheckbox = document.querySelector('.select-all-checkbox');

function updateSelectAllCheckbox() {
    const recordCheckboxes = document.querySelectorAll('.record-checkbox');
    
    selectAllCheckbox.addEventListener('change', function() {
        recordCheckboxes.forEach(checkbox => {
            checkbox.checked = selectAllCheckbox.checked;
        });
    });

    recordCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const allChecked = Array.from(recordCheckboxes).every(checkbox => checkbox.checked);
            selectAllCheckbox.checked = allChecked;
        });
    });
}

const deleteIcon = document.querySelector('.delete-icon');
deleteIcon.addEventListener('click', function() {
    const checkboxes = document.querySelectorAll('.record-checkbox');
    
    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            checkbox.parentElement.remove();
        }
    });

    selectAllCheckbox.checked = false;
});
