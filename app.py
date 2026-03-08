from flask import Flask, render_template

app = Flask(__name__)


students = [
    {"name": "Амангельдиева Адия", "photo": "students/adiya.jpg.jpeg", "compliment": "Ты очень нежная, умная и искренняя 🌸"},
    {"name": "Арайлым Сағындық", "photo": "students/araylym.jpg.jpeg", "compliment": "Ты сильная и целеустремлённая ✨"},
    {"name": "Асел Мансурбек", "photo": "students/assel.jpg.jpeg", "compliment": "В тебе столько света и доброты 💖"},
    {"name": "Бисембек Дариға", "photo": "students/dariga.jpg.jpg", "compliment": "Ты уверенная и очень красивая 🌷"},
    {"name": "Дильназ Шәмен", "photo": "students/dilnaz.jpg.jpeg", "compliment": "Ты вдохновляешь своей искренностью ✨"},
    {"name": "Дүйсеш Аружан", "photo": "students/aruzhan.jpg.jpeg", "compliment": "Ты яркая и талантливая 💕"},
    {"name": "Еркебай Сымбат", "photo": "students/symbat.jpg.jpeg", "compliment": "Ты стильная и умная 🌸"},
    {"name": "Жазыбекова Жанерке", "photo": "students/zhanerke.jpg.jpeg", "compliment": "Ты уверенно идёшь к целям ✨"},
    {"name": "Жаннұр Бибітқызы", "photo": "students/zhannur.jpg.jpeg", "compliment": "Ты очень тёплый человек 💖"},
    {"name": "Куанышова Алина", "photo": "students/alina.jpg.jpeg", "compliment": "Ты нежная и красивая 🌷"},
    {"name": "Қахарман Ақтоты", "photo": "students/aktoty.jpg.jpeg", "compliment": "Ты сияешь своей улыбкой ✨"},
    {"name": "Мелс Сабина", "photo": "students/sabina.jpg.jpeg", "compliment": "Ты креативная и особенная 💕"},
    {"name": "Сұлтанғалиева Бақытгүл", "photo": "students/bakytgul.jpg.jpeg", "compliment": "Ты сильная и мудрая 🌸"},
    {"name": "Төребай Альбина", "photo": "students/albina.jpg.jpeg", "compliment": "Ты светлый человек 💖"},
    {"name": "Жәкібай Айдана", "photo": "students/aidana.jpg.jpeg", "compliment": "Ты вдохновляющая и талантливая ✨"},
]  

@app.route("/")
def index():
    return render_template("index.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)

    