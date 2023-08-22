from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #Home page
def index():
  return render_template('homepage.html')

@app.route('/calendar') #Calender page
def calendar():
  return render_template('calender.html')

@app.route('/schedule') #Schedule page
def schedule():
  return render_template('schedule.html')

@app.route('/habit-tracker') #Habit page
def habit_tracker():
  return render_template('habit.html')

@app.route('/to-do') #To-do page
def to_do():
  return render_template('todo.html')

app.run(host='0.0.0.0', port=81)