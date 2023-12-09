#!/usr/bin/env python3
import rospy as rp
from std_msgs.msg import String
from time import sleep
from flask import Flask, render_template, request

# Initialize ros node
rp.init_node("serv_pub")
rp.loginfo("hello from serv_pub")
# Create publisher
pub = rp.Publisher("/torta_cmd", String, queue_size=10)


# Initialize flask
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    max_linear = 0
    max_rotation = 0
    
    if request.method == "POST":
        max_linear = request.form.get("max_linear")
        max_rotation = request.form.get("max_angle")
        # Publish recieved values
        publish_str = "linear is " + str(max_linear) + " and angle is " + str(max_rotation)
        pub.publish(publish_str)
        rp.loginfo(publish_str)
    return render_template("index.html")

    

