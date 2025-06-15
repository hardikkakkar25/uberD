🚖 Uber Clone – Pricing Module (Django + DRF)
A Django-based microservice for handling dynamic pricing logic similar to Uber/Ola. This includes base pricing, distance-based surcharges, time-of-day multipliers, and day-specific rates.

📁 Project Structure
bash
Copy
Edit
uber_clone/
├── uber_clone/           # Main project config
│   └── settings.py
├── pricing/              # App for pricing logic
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── serializers.py
├── manage.py
└── requirements.txt
🛠 Features
Base pricing with configurable distance

Additional per-km charge

Time-based multipliers (peak hours)

Day-of-week specific pricing

Wait-time charges after free minutes

REST API to calculate ride fare

🧰 Tech Stack
Python 3.11+

Django 5.2

Django REST Framework

MySQL / SQLite (configurable)

🔧 Setup Instructions
Clone the repo

bash
Copy
Edit
git clone https://github.com/yourusername/uber-clone-pricing.git
cd uber-clone-pricing
Create & activate virtual environment

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Configure Database
Update your DB credentials in settings.py.

Run Migrations

bash
Copy
Edit
python manage.py migrate
Create Superuser

bash
Copy
Edit
python manage.py createsuperuser
Run Server

bash
Copy
Edit
python manage.py runserver
📡 API Endpoint
URL: /api/calculate-price/
Method: POST
Payload:

json
Copy
Edit
{
  "distance_km": 12,
  "time_of_day": "17:30",
  "day_of_week": "Monday",
  "wait_minutes": 6
}
Response:

json
Copy
Edit
{
  "total_price": 185.0,
  "base_price": 100.0,
  "distance_price": 60.0,
  "wait_charge": 25.0,
  "time_multiplier": 1.0
}
✅ Todo
✅ Pricing config admin panel

✅ Dynamic pricing by day/time

⏳ Integrate with ride booking module

⏳ Add unit tests and CI

