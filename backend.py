from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('homepage.html')

@app.route('/calendar')
def calendar():
  return render_template('calendar.html')

@app.route('/schedule')
def schedule():
  return render_template('schedule.html')

@app.route('/todo')
def todo():
  return render_template('todo.html')

@app.route('/habit')
def habit():
  return render_template('habit.html')

app.run(host='0.0.0.0', port=81)