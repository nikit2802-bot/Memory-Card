from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, 
    QHBoxLayout, QVBoxLayout, 
    QGroupBox, QRadioButton,  
    QPushButton, QLabel, QButtonGroup
)
from random import shuffle, randint

class Question():
    def __init__(self, question_text, right_answer_text, wrong1_text, wrong2_text, wrong3_text):
        self.question = question_text
        self.right_answer = right_answer_text
        self.wrong1 = wrong1_text
        self.wrong2 = wrong2_text
        self.wrong3 = wrong3_text

app = QApplication([])


btn_OK = QPushButton('Ответить')
btn_Skip = QPushButton('Пропустить')  
lb_Question = QLabel('Самый сложный вопрос в мире!')


lb_QuestionNumber = QLabel()
lb_QuestionNumber.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
lb_QuestionNumber.setStyleSheet("color: gray; font-size: 12px;")

RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()  


layout_line1.addWidget(lb_Question, alignment=Qt.AlignHCenter | Qt.AlignVCenter)
layout_line1.addWidget(lb_QuestionNumber, alignment=Qt.AlignRight | Qt.AlignTop)  

layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addWidget(btn_Skip, stretch=2)  
layout_line3.addStretch(1)


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.setSpacing(5)


RadioButtons = QButtonGroup()
RadioButtons.addButton(rbtn_1)
RadioButtons.addButton(rbtn_2)
RadioButtons.addButton(rbtn_3)
RadioButtons.addButton(rbtn_4)

AnsGroupBox.hide()


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    btn_OK.setText('Ответить')
    RadioButtons.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioButtons.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Correct.setText(q.right_answer)
    lb_Question.setText(q.question)
    show_question()

def check_answer():
    if answers[0].isChecked():
        window.score += 1
        show_correct('Правильно!')
    elif any([btn.isChecked() for btn in answers[1:]]):
        show_correct('Неверно!')
    print('Статистика')
    print('- Верно отвечено:', window.score)
    print('- Всего вопросов:', window.total)
    print(f'- Рейтинг: {window.score / window.total * 100:.1f}%')

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def next_question():
    window.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    ask(questions_list[cur_question])
    lb_QuestionNumber.setText(f"Вопрос {window.total} из {len(questions_list)}")

def skip_question():
    window.total += 1  
    next_question()   
    print('Пропущен вопрос')
    print('- Верно отвечено:', window.score)
    print('- Всего вопросов:', window.total)

def click_ok():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


btn_OK.clicked.connect(click_ok)
btn_Skip.clicked.connect(skip_question)


questions_list = [
    Question('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Бразильский', 'Русский'),
    Question('Какой национальности не существует?', 'Энцы', 'Смурфы', 'Чулымцы', 'Алеуты'),
    Question('Какой цвет получается при смешивании синего и жёлтого?', 'зеленый', 'красный', 'белый', 'коричневый'),
    Question('Сколько дней в неделе?', '7', '51', '10', '8'),
    Question('Как называется звезда, вокруг которой вращается Земля', 'Солнце', 'Сириус', 'Вега', 'Марс'),
    Question('Какой месяц идёт после января', 'Февраль', 'Ноябрь', 'Март', 'Декабрь'),
    Question('Сколько пальцев на одной руке у человека?', '5', '6', '48', '4'),
    Question('Какой газ люди вдыхают при дыхании?', 'Кислород', 'Углекислый газ', 'азот', 'водород'),
    Question('Главный герой игры God of War?', 'Кратос', 'Арес', 'Атрей', 'Евгенний'),
    Question('Имя человека-паука?', 'Питер', 'Володя', 'Анатолий', 'Илон'),
]


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memory Card')
window.resize(400, 300)
window.show()

window.score = 0
window.total = 0
lb_QuestionNumber.setText(f"Вопрос {window.total} из {len(questions_list)}")
next_question()

app.exec()
