from flask import Flask, render_template, jsonify
import random
import time
		   

app = Flask(__name__, template_folder='templates')

live_open_price = []  # Initialize empty list for live open prices
live_close_price = []  # Initialize empty list for live close prices

def generate_pnl_data():
    actual_pnl = 0
    ideal_pnl = 0
    actual_pnl += 3 * random.randint(-5, 10)
    ideal_pnl += 3 * random.randint(-5, 10)
    return {'actual_pnl': actual_pnl, 'ideal_pnl': ideal_pnl}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pnl_data')
def get_pnl_data():
    return generate_pnl_data()

@app.route('/strat_data')
def get_strat_data():
    global live_open_price, live_close_price

    while True:
					 
        if len(live_open_price) <= len(live_close_price):
            live_open_price.append(random.randint(1, 100))
        else:
            live_close_price.append(random.randint(1, 100))
        
        if len(live_open_price) == len(live_close_price):
            ratio_data = [x / y for x, y in zip(live_open_price, live_close_price)]
            data = {
                'live_open_price': live_open_price,
                'live_close_price': live_close_price
            }
            return jsonify(data)

        time.sleep(1)
if __name__ == '__main__':
    app.run(debug=True)