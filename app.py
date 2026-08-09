from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder="templates")


# =========================
# MySQL Configuration
# =========================

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "local_service_finder"

mysql = MySQL(app)


# =========================
# Home Page
# =========================

@app.route("/")
def home():
    return render_template("home.html")


# =========================
# Register Page
# =========================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        password = request.form["password"]

        cur = mysql.connection.cursor()

        cur.execute(
            "INSERT INTO user(name,email,phone,password) VALUES(%s,%s,%s,%s)",
            (name, email, phone, password)
        )

        mysql.connection.commit()
        cur.close()

        return "Registration Successful"

    return render_template("register.html")


# =========================
# About Page
# =========================

@app.route("/about")
def about():
    return render_template("about.html")


# =========================
# Services Data
# =========================

services_data = {

    "Electrician": {
        "icon": "⚡",
        "description": "Electrical repair, wiring and installation services.",
        "provider": "Rahul Electrical Services",
        "experience": "5 Years",
        "contact": "9876543210",
        "location": "Pune",
        "price": "₹200 - ₹1000",
        "time": "9:00 AM - 8:00 PM",
        "rating": "⭐⭐⭐⭐⭐"
    },

    "Plumber": {
        "icon": "🚰",
        "description": "Pipe fitting and leakage repair services.",
        "provider": "Shree Plumbing",
        "experience": "4 Years",
        "contact": "9876500000",
        "location": "Mumbai",
        "price": "₹300 - ₹1200",
        "time": "8:00 AM - 7:00 PM",
        "rating": "⭐⭐⭐⭐"
    },

    "Carpenter": {
        "icon": "🪚",
        "description": "Furniture and wood work services.",
        "provider": "Perfect Wood Works",
        "experience": "6 Years",
        "contact": "9876511111",
        "location": "Nashik",
        "price": "₹500 - ₹2500",
        "time": "9:00 AM - 6:00 PM",
        "rating": "⭐⭐⭐⭐⭐"
    },

    "Painter": {
        "icon": "🎨",
        "description": "Interior and exterior painting services.",
        "provider": "Ramesh Painter",
        "experience": "7 Years",
        "contact": "9876522222",
        "location": "Pune",
        "price": "₹1000 - ₹5000",
        "time": "9:00 AM - 7:00 PM",
        "rating": "⭐⭐⭐⭐"
    },

    "AC Repair": {
        "icon": "❄️",
        "description": "Professional AC installation, gas filling, cooling issue repair, servicing and maintenance.",
        "provider": "Cool Air Services",
        "experience": "5 Years",
        "contact": "9876533333",
        "location": "Mumbai",
        "price": "₹500 - ₹2500",
        "time": "10:00 AM - 8:00 PM",
        "rating": "⭐⭐⭐⭐⭐"
    },

    "Cleaning Service": {
        "icon": "🧹",
        "description": "Professional home and office cleaning.",
        "provider": "Clean Home Services",
        "experience": "4 Years",
        "contact": "9876544444",
        "location": "Pune",
        "price": "₹400 - ₹2000",
        "time": "8:00 AM - 6:00 PM",
        "rating": "⭐⭐⭐⭐"
    },

    "Computer Repair": {
        "icon": "💻",
        "description": "Desktop and laptop repair services.",
        "provider": "Tech Solutions",
        "experience": "8 Years",
        "contact": "9876555555",
        "location": "Nashik",
        "price": "₹300 - ₹5000",
        "time": "10:00 AM - 7:00 PM",
        "rating": "⭐⭐⭐⭐⭐"
    },

    "Mobile Repair": {
        "icon": "📱",
        "description": "Mobile repair and software solutions.",
        "provider": "Mobile Care",
        "experience": "6 Years",
        "contact": "9876566666",
        "location": "Pune",
        "price": "₹200 - ₹3000",
        "time": "10:00 AM - 8:00 PM",
        "rating": "⭐⭐⭐⭐"
    },

    "Home Tutor": {
        "icon": "📚",
        "description": "Experienced home tutors for all subjects.",
        "provider": "Smart Tutors",
        "experience": "5 Years",
        "contact": "9876577777",
        "location": "Pune",
        "price": "₹500 - ₹1500",
        "time": "4:00 PM - 9:00 PM",
        "rating": "⭐⭐⭐⭐⭐"
    },

    "Beauty Parlour": {
        "icon": "💇‍♀️",
        "description": "Beauty and makeup services at home.",
        "provider": "Glow Beauty",
        "experience": "6 Years",
        "contact": "9876588888",
        "location": "Mumbai",
        "price": "₹500 - ₹5000",
        "time": "10:00 AM - 8:00 PM",
        "rating": "⭐⭐⭐⭐"
    },

    "Photographer": {
        "icon": "📸",
        "description": "Wedding and event photography services.",
        "provider": "Dream Clicks",
        "experience": "9 Years",
        "contact": "9876599999",
        "location": "Pune",
        "price": "₹5000 - ₹50000",
        "time": "By Appointment",
        "rating": "⭐⭐⭐⭐⭐"
    },

    "Car Mechanic": {
        "icon": "🚗",
        "description": "Car servicing and repair.",
        "provider": "Auto Garage",
        "experience": "8 Years",
        "contact": "9876512345",
        "location": "Pune",
        "price": "₹1000 - ₹10000",
        "time": "9:00 AM - 7:00 PM",
        "rating": "⭐⭐⭐⭐⭐"
    }
}


# =========================
# Services Page + Search
# =========================

@app.route("/services")
def services():

    search = request.args.get("search", "").strip()

    if search:
        filtered_services = {
            name: data
            for name, data in services_data.items()
            if search.lower() in name.lower()
        }
    else:
        filtered_services = services_data

    return render_template(
        "services.html",
        services=filtered_services,
        search=search
    )


# =========================
# Contact Page
# =========================

@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        # Save contact message in MySQL
        cur = mysql.connection.cursor()

        cur.execute(
            """INSERT INTO contact (name, email, message)
            VALUES (%s, %s, %s)""",
            (name, email, message)
        )

        mysql.connection.commit()
        cur.close()

        return """
        <html>
        <head>
            <title>Message Sent</title>

            <link
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
                rel="stylesheet"
            >
        </head>

        <body class="bg-light">

            <div class="container mt-5">

                <div class="card shadow p-5 text-center">

                    <h2 class="text-success">
                        ✅ Message Sent Successfully!
                    </h2>

                    <p class="mt-3">
                        Thank you for contacting Local Service Finder.
                    </p>

                    <a href="/contact" class="btn btn-primary">
                        Back to Contact
                    </a>

                </div>

            </div>

        </body>
        </html>
        """

    return render_template("contact.html")

# =========================
# Login Page
# =========================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        cur = mysql.connection.cursor()

        cur.execute(
            "SELECT * FROM user WHERE email=%s AND password=%s",
            (email, password)
        )

        user = cur.fetchone()

        cur.close()

        if user:
            return render_template("dashboard.html")

        else:
            return "<h2>Invalid Email or Password ❌</h2>"

    return render_template("login.html")


# =========================
# Service Details
# =========================

@app.route("/service/<name>")
def service_details(name):

    service = services_data.get(name)

    if service:

        cur = mysql.connection.cursor()

        cur.execute(
            "SELECT user_name, rating, review FROM review WHERE service_name=%s",
            (name,)
        )

        reviews = cur.fetchall()

        cur.close()

        return render_template(
            "service_details.html",
            service=service,
            name=name,
            reviews=reviews
        )

    return "<h2>Service Not Found ❌</h2>"


# =========================
# Book Service
# =========================

@app.route("/book/<name>", methods=["GET", "POST"])
def book_service(name):

    if request.method == "POST":

        fullname = request.form["fullname"]
        mobile = request.form["mobile"]
        address = request.form["address"]
        date = request.form["date"]
        time = request.form["time"]

        # Save booking in MySQL
        cur = mysql.connection.cursor()

        cur.execute(
            """INSERT INTO booking
            (service_name, fullname, mobile, address, booking_date, booking_time)
            VALUES (%s, %s, %s, %s, %s, %s)""",
            (name, fullname, mobile, address, date, time)
        )

        mysql.connection.commit()
        cur.close()

        # Booking Success Page
        return f"""
        <html>

        <head>
            <title>Booking Successful</title>

            <link
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css"
                rel="stylesheet"
            >
        </head>

        <body class="bg-light">

        <div class="container mt-5">

            <div class="card shadow p-4">

                <h2 class="text-success">
                    🎉 Booking Successful
                </h2>

                <hr>

                <h5>Service : {name}</h5>
                <h5>Name : {fullname}</h5>
                <h5>Mobile : {mobile}</h5>
                <h5>Address : {address}</h5>
                <h5>Date : {date}</h5>
                <h5>Time : {time}</h5>

                <br>

                <a
                    href="/service/{name}"
                    class="btn btn-primary"
                >
                    Back to Service
                </a>

            </div>

        </div>

        </body>

        </html>
        """

    return render_template(
        "book_service.html",
        name=name
    )

# =========================
# Provider Details
# =========================

@app.route("/provider/<name>")
def provider_details(name):

    return redirect(f"/service/{name}")


# =========================
# Submit Review
# =========================

@app.route("/review/<name>", methods=["POST"])
def review(name):

    user_name = request.form["user_name"]
    rating = request.form["rating"]
    review_text = request.form["review"]

    cur = mysql.connection.cursor()

    cur.execute(
        """
        INSERT INTO review
        (service_name, user_name, rating, review)
        VALUES (%s, %s, %s, %s)
        """,
        (name, user_name, rating, review_text)
    )

    mysql.connection.commit()
    cur.close()

    return redirect(f"/service/{name}")

# Admin Login

@app.route("/admin", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        cur = mysql.connection.cursor()

        cur.execute(
            "SELECT * FROM admin WHERE username=%s AND password=%s",
            (username, password)
        )

        admin = cur.fetchone()

        cur.close()

        if admin:
            return render_template("admin_dashboard.html")
        else:
            return "<h2>❌ Invalid Admin Username or Password</h2>"

    return render_template("admin_login.html")
@app.route("/admin/users")
def admin_users():

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT user_id, name, email, phone FROM user"
    )

    users = cur.fetchall()

    cur.close()

    return render_template(
        "admin_users.html",
        users=users
    )
@app.route("/admin/bookings")
def admin_bookings():

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT * FROM booking"
    )

    bookings = cur.fetchall()

    cur.close()

    return render_template(
        "admin_bookings.html",
        bookings=bookings
    )
@app.route("/admin/reviews")
def admin_reviews():

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT user_name, service_name, rating, review FROM review"
    )

    reviews = cur.fetchall()

    cur.close()

    return render_template(
        "admin_reviews.html",
        reviews=reviews
    )
@app.route("/admin/messages")
def admin_messages():

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT name, email, message FROM contact"
    )

    messages = cur.fetchall()

    cur.close()

    return render_template(
        "admin_messages.html",
        messages=messages
    )
@app.route("/admin/logout")
def admin_logout():

    return redirect("/admin")
@app.route("/logout")
def logout():
    return redirect("/login")
# =========================
# Run Application
# =========================

if __name__ == "__main__":
    app.run(debug=True)