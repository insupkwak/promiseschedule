# app.py
from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_start_time(shower_time, dress_time, makeup_time, travel_time, appointment_time_hour, appointment_time_minute):
    preparation_time = shower_time + dress_time + makeup_time + travel_time
    total_minutes = (appointment_time_hour * 60 + appointment_time_minute) - preparation_time
    start_hour = total_minutes // 60
    start_minute = total_minutes % 60
    if start_hour < 0:
        start_hour += 24
    return start_hour, start_minute

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        ampm = request.form["ampm"]
        hour = int(request.form["hour"])
        minute = int(request.form["minute"])
        if ampm == "PM":
            hour += 12
        shower_time = int(request.form["shower_time"])
        dress_time = int(request.form["dress_time"])
        makeup_time = int(request.form["makeup_time"])
        travel_time = int(request.form["travel_time"])

        start_hour, start_minute = calculate_start_time(shower_time, dress_time, makeup_time, travel_time, hour, minute)

        if start_hour >= 12:
            ampm_start = "오후"
            if start_hour > 12:
                start_hour -= 12
        else:
            ampm_start = "오전"

        return render_template("result.html", start_hour=start_hour, start_minute=start_minute, ampm_start=ampm_start)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
