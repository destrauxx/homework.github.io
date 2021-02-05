from flask import Flask, render_template, request, url_for
from superhero_api import SuperHeroAPI

app = Flask(__name__)
s = SuperHeroAPI()

@app.route('/', methods=['POST', 'GET'])
def index():
    user_character_name = request.form.get('name')
    try:
        image_url = s.get_hero_image_url(f'{user_character_name}')
        id_ = s.get_id(f'{user_character_name}')
        name = user_character_name.title()
        hero_stats = s.get_hero_stats(s.parse_name(f'{user_character_name}'))
        combat = hero_stats['combat']
        durability = hero_stats['durability']
        intelligence = hero_stats['intelligence']
        power = hero_stats['power']
        speed = hero_stats['speed']
        strength = hero_stats['strength']
        return f'''
        <head><link rel="stylesheet" href="static/css/style.css"></head>
        <div class="card">
        <div class='card-wrapper'>
            <div class='card-wrapper-herobox'>
                <p class='card-wrapper-herobox_id'>Id: {id_}</p>
                <p class='card-wrapper-herobox_name'>Name: {name}</p>
                <div class='card-wrapper-herobox-stats'>
                    <p class='card-wrapper-herobox-stats_stats'>Stats</p>
                    <p class='card-wrapper-herobox-stats_combat'>Combat: {combat}</p>
                    <p class='card-wrapper-herobox-stats_durability'>Durability: {durability}</p>
                    <p class='card-wrapper-herobox-stats_intelligence'>Intelligence: {intelligence}</p>
                    <p class='card-wrapper-herobox-stats_power'>Power: {power}</p>
                    <p class='card-wrapper-herobox-stats_speed'>Speed: {speed}</p>
                    <p class='card-wrapper-herobox-stats_strength'>Strength: {strength}</p>
                </div>
                <form action="" method="post">
                    <input class='name' type="text" name="name" placeholder='Введи имя персонажа:'>
                    <input class='send_name' type="submit" value="Найти">
                </form>
                <div class="card-wrapper-image">
                    <img src="{image_url}" name='image' class="image">
                </div>
            </div>
        </div>
    </div>'''
    except:
        return render_template('index.html')
       
