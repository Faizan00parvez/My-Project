import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_metric = psutil.cpu_percent()
    mem_metric = psutil.virtual_memory().percent

    # Improved threshold handling with flexibility
    high_usage_threshold = 80  # Customizable threshold for high usage (default: 80%)
    message = None
    if cpu_metric > high_usage_threshold or mem_metric > high_usage_threshold:
        message = "High CPU or Memory Usage Detected! Consider scaling up resources."

    return render_template("index.html", cpu_metric=cpu_metric, mem_metric=mem_metric, message=message)

if __name__ == '__main__':
    # Handle potential exceptions gracefully
    try:
        app.run(debug=True, host='0.0.0.0')
    except KeyboardInterrupt:
        print("Server stopped due to keyboard interrupt.")
    except Exception as e:
        print(f"An error occurred: {e}")
