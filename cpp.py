from flask import Flask , render_template


app = Flask(__name__)

@app.route('/')
def index():
    star_pattern = generate_star_pattern()
    return render_template('stars.html', star_pattern=star_pattern)

def generate_star_pattern():
    pattern = []
    for row in range(7):
        row_pattern = []
        for col in range(5):
            if (col == 0 or col == 4) or ((row == 0 or row == 3) and (col > 0 and col < 4)):
                row_pattern.append("*")
            else:
                row_pattern.append(" ")
        pattern.append("".join(row_pattern))
    return pattern

if __name__ == '__main__':
    app.run(debug=True)
    

