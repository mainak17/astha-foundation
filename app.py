from flask import Flask, render_template
from utils import ReadJsonFile

app = Flask(__name__)

notification_data = ReadJsonFile.get_notifications('data/notifications.json')
unread_count = sum(1 for notification in notification_data if not notification["IsRead"])
notifications = {"data":notification_data,"UnreadCount":unread_count}

event_list = ReadJsonFile.get_event_names('data/events.json')


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

    return render_template('content.html',content=content,notifications=notifications,event_list=event_list)

@app.route('/events')
def events():

    data = ReadJsonFile.read_json_file('data/events.json')
    keys = ReadJsonFile.get_keys('data/events.json')
    content = {"type":"Events","body":data,"keys":keys}

    return render_template('content.html',content=content,notifications=notifications)

@app.route('/donations/delete/<donation_id>')
def delete_donation(donation_id):
    # Logic to delete the donation with the given donation_id
    return "Donation deleted successfully"

@app.route('/donations/submit/<donation_id>')
def submit_donation(donation_id):
    # Logic to delete the donation with the given donation_id
    return "Donation submitted successfully"


if __name__ == '__main__':
    app.run(debug=True)
