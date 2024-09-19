const questionContainer = document.getElementById('question-container');
const nextButton = document.getElementById('next-button');
const resultContainer = document.getElementById('result-container');
const startButton = document.getElementById('start-button');

const questions = {
    " Aryabhatta invented the number?": ['0', '3', '5', '9'],
    " How many days are there in a week?": ['6', '7', '8', '9'],
    " 3561+9389": ['12960', '12678', '12243', '12950'],
    " How many hours are there in a day?": ['24hr', '23hr', '25hr', '21hr'],
    " Name the national flower of India?": ['Lotus', 'Lily', 'Hibiscus', 'Rose'],
    " Which gas do plants absorb during photosynthesis?": ['Carbon Dioxide', 'Nitrogen', 'Oxygen', 'None'],
    " Who is the Father of our Nation?": ['Mahatma Gandhi', 'Dr. Rajendra Prasad', 'Dr. B. R. Ambedkar', 'Jawaharlal Nehru']
};

const answers = ['0', '7', '12950', '24hr', 'Lotus', 'Carbon Dioxide', 'Mahatma Gandhi'];

let currentQuestion = 0;
let score = 0;

startButton.addEventListener('click', startQuiz);

function startQuiz() {
    startButton.style.display = 'none';
    nextButton.style.display = 'block';
    displayQuestion();
}

function displayQuestion() {
    const question = Object.keys(questions)[currentQuestion];
    const options = questions[question];

    const questionElement = document.createElement('p');
    questionElement.textContent = `Question ${currentQuestion + 1}: ${question}`;

    const optionsContainer = document.createElement('div');

    options.forEach((option, index) => {
        const radioInput = document.createElement('input');
        radioInput.type = 'radio';
        radioInput.name = 'option';
        radioInput.value = option;

        const label = document.createElement('label');
        label.textContent = option;

        const optionElement = document.createElement('div');
        optionElement.appendChild(radioInput);
        optionElement.appendChild(label);

        optionsContainer.appendChild(optionElement);
    });

    questionContainer.innerHTML = '';
    questionContainer.appendChild(questionElement);
    questionContainer.appendChild(optionsContainer);
}

nextButton.addEventListener('click', checkAnswer);

function checkAnswer() {
    const selectedOption = document.querySelector('input[name="option"]:checked');
    if (selectedOption) {
        const selectedAnswer = selectedOption.value;
        if (selectedAnswer === answers[currentQuestion]) {
            score += 2;
        } else {
            score -= 1;
        }
    } else {
        score -= 1;
    }

    currentQuestion++;

    if (currentQuestion < Object.keys(questions).length) {
        displayQuestion();
    } else {
        displayResult();
    }
}

function displayResult() {
    nextButton.style.display = 'none';
    questionContainer.innerHTML = '';

    const resultText = document.createElement('p');
    resultText.textContent = `Your Score is ${score} out of ${Object.keys(questions).length * 2}`;

    if (score >= 11) {
        resultText.textContent += '\nYou win the game!';
    } else {
        resultText.textContent += '\nYou lose the game.';
    }

    resultContainer.innerHTML = '';
    resultContainer.appendChild(resultText);
}