from flask import Flask, render_template
from utils import ReadJsonFile

app = Flask(__name__)

notification_data = ReadJsonFile.get_notifications('data/notifications.json')
unread_count = sum(1 for notification in notification_data if  notification["Status"]=="unread")
notifications = {"data":notification_data,"UnreadCount":unread_count}

@app.route('/')
def index():
    return render_template('index.html',notifications=notifications)

@app.route('/members')
def members():

    data = ReadJsonFile.read_json_file('data/members.json')
    keys = ReadJsonFile.get_keys('data/members.json')
    content = {"type":"Members","body":data,"keys":keys}

    return render_template('content.html',content=content,notifications=notifications)

@app.route('/donations')
def donations():

    data = ReadJsonFile.read_json_file('data/donations.json')
    keys = ReadJsonFile.get_keys('data/donations.json')
    content = {"type":"Donations","body":data,"keys":keys}

    return render_template('content.html',content=content,notifications=notifications)

@app.route('/events')
def events():

    data = ReadJsonFile.read_json_file('data/events.json')
    keys = ReadJsonFile.get_keys('data/events.json')
    content = {"type":"Events","body":data,"keys":keys}

    return render_template('content.html',content=content,notifications=notifications)


if __name__ == '__main__':
    app.run(debug=True)
