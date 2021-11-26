import sys
from form import Ui_form_app
from PyQt5 import QtCore, QtGui, QtWidgets
import requests as req

# Создание приложения
app = QtWidgets.QApplication(sys.argv) 
# Создание формы
form_app = QtWidgets.QWidget()
ui = Ui_form_app()
ui.setupUi(form_app)
form_app.show()
# Код самой логики приложения
language = 'ru'
def set_lang_rus():
    global language
    language = "ru"
    
def set_lang_eng():
    global language 
    language = "en"

def generation_osk():
    response = req.get("https://evilinsult.com/generate_insult.php",
            params={"lang": language, "type": "json"})
    insult = response.json()

    try:
        ui.received_osk.setText(insult["insult"])
    except KeyError:
        ui.received_osk.setText("Ошибка, попробуйте еще раз!")

ui.select_lang_eng.clicked.connect( set_lang_eng )
ui.select_lang_rus.clicked.connect(  set_lang_rus )

ui.get_osk.clicked.connect( generation_osk )


# Запуск приложения
