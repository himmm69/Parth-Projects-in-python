
from flask import Flask 
from helper import pets
# instance of flask
app = Flask(__name__)

@app.route('/')
def index():
    return  '''<h1> Adopt a Pet!</h1>
    <p> Browse through the links below to find your new furry friend:</p> 
    <ul>
     <li><a href = '/animals/dogs'>Dogs</a></li>
     <li><a href = '/animals/cats'>Cats</a></li>
     <li><a href = '/animals/rabbits'>Rabbits</a></li>
     </ul>'''

@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = f'<h1>List of {pet_type.capitalize()}</h1>'
    
    html += '<ul>'
    
    # Use enumerate to get both the pet and its index
    for index, pet in enumerate(pets[pet_type]):
        # Create <li> element for each pet's name with link
        html += f'<li><a href="/animals/{pet_type}/{index}">{pet["name"]}</a></li>'
    
    html += '</ul>'
    
    return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
    # Correct way to access the specific pet
    pet = pets[pet_type][pet_id]
    html = f'<h1>{pet["name"]}</h1>'
    html += f'<img src="{pet["url"]}">'
    html += f'<p>{pet["description"]}</p>'
    html += '<ul>'
    html += f'<li>Breed: {pet["breed"]}</li>'
    html += f'<li>Age: {pet["age"]}</li>'
    html += '</ul>'
    return html