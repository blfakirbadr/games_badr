from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    games = {
        "ألعاب الأكشن": [
            {
                "title": "Elden Ring",
                "image": "/static/images/elden_ring.jpg",
                "description": "تحديات ضخمة في عالم خيالي.",
                "download": "https://store.steampowered.com/app/1245620/Elden_Ring/",
                "video": "https://www.youtube.com/watch?v=AKXiKBnzpBQ"
            },
            {
                "title": "God of War",
                "image": "/static/images/god_of_war.jpg",
                "description": "أسطورة كريتوس في عالم الآلهة.",
                "download": "https://www.playstation.com/en-us/games/god-of-war/",
                "video": "https://www.youtube.com/watch?v=K0u_kAWLJOA"
            },
            {
                "title": "Spider-Man",
                "image": "/static/images/spiderman.jpg",
                "description": "تحكم في سبايدرمان وسط نيويورك.",
                "download": "https://www.playstation.com/en-us/games/marvels-spider-man/",
                "video": "https://www.youtube.com/watch?v=b5_-vUjDFvE"
            },
            {
                "title": "GTA V",
                "image": "/static/images/gta_v.jpg",
                "description": "حرية كاملة في عالم مفتوح.",
                "download": "https://www.rockstargames.com/V/",
                "video": "https://www.youtube.com/watch?v=QkkoHAzjnUs"
            },
            {
                "title": "Resident Evil Village",
                "image": "/static/images/resident_evil_village.png",
                "description": "رعب وبقاء في قرية غامضة.",
                "download": "https://store.steampowered.com/app/1196590/Resident_Evil_Village/",
                "video": "https://www.youtube.com/watch?v=QJvmdGBE4Ec"
            }
        ],
        "ألعاب الرياضة": [
            {
                "title": "eFootball 2024",
                "image": "/static/images/efootball_2024.webp",
                "description": "كرة قدم مجانية بتحديثات مستمرة.",
                "download": "https://www.konami.com/efootball/en/",
                "video": "https://www.youtube.com/watch?v=Jk4tDsqz3PI"
            },
            {
                "title": "EA Sports FC 26",
                "image": "/static/images/ea_fc26.webp",
                "description": "تجربة واقعية مع نجوم الكرة.",
                "download": "https://www.ea.com/games/ea-sports-fc",
                "video": "https://www.youtube.com/watch?v=o3V-GvvzjE4"
            }
        ],
        "ألعاب باتل رويال": [
            {
                "title": "PUBG",
                "image": "/static/images/pubg.webp",
                "description": "قتال حتى آخر لاعب.",
                "download": "https://pubg.com/",
                "video": "https://www.youtube.com/watch?v=UCDtkZbTnYY"
            },
            {
                "title": "Apex Legends",
                "image": "/static/images/apex_legends.webp",
                "description": "فرق سريعة بأسلحة متطورة.",
                "download": "https://www.ea.com/games/apex-legends",
                "video": "https://www.youtube.com/watch?v=innmNewjkuk"
            },
            {
                "title": "Fortnite",
                "image": "/static/images/fortnite.webp",
                "description": "باتل رويال مع بناء وتحديات.",
                "download": "https://www.fortnite.com/",
                "video": "https://www.youtube.com/watch?v=2gUtfBmw86Y"
            },
            {
                "title": "Call of Duty: Warzone",
                "image": "/static/images/cod_warzone.webp",
                "description": "أكشن عالي الجودة في ساحات قتال ضخمة.",
                "download": "https://www.callofduty.com/warzone",
                "video": "https://www.youtube.com/watch?v=0E44DClsX5Q"
            },
            {
                "title": "Blood Strike",
                "image": "/static/images/blood_strike.webp",
                "description": "لعبة جديدة تجمع بين السرعة والتكتيك.",
                "download": "https://www.blood-strike.com/ar/",
                "video": "https://www.youtube.com/watch?v=vf93VxS-kGQ"
            }
        ]
    }
    return render_template("index.html", games=games)

if __name__ == '__main__':
    app.run(debug=True)