from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    data = None
    country = 'USA'  # default country
    
    if request.method == 'POST':
        country = request.form.get('country')
    
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
    else:
        data = None
    
    return render_template('index.html', data=data, country=country)

if __name__ == '__main__':
    app.run(debug=True)
