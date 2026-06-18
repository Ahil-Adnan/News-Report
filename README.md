📰 News Report

A responsive news headlines web app built with Flask and the Currents API. Browse top stories by category or search for any topic — all displayed in a clean card-based layout.

🔍 Features


Browse news by category: Technology, Business, Sports, Entertainment, Health
Keyword search across live news articles
Responsive article card grid with images, author, and publish date
Graceful fallback for articles with no image


🛠️ Tech Stack


Backend: Python, Flask
Frontend: HTML, Jinja2, CSS
API: Currents API
Environment: python-dotenv


📁 Project Structure

News-Report/
├── app.py
├── .env
├── Templates/
│   ├── base.html
│   └── index.html
└── static/
    ├── css/
    │   └── main.css
    └── images/
        └── placeholder.png

🚀 Getting Started

1. Clone the repository

bashgit clone https://github.com/Ahil-Adnan/News-Report.git
cd News-Report

2. Install dependencies

bashpip install flask requests python-dotenv

3. Get a free API key

Sign up at currentsapi.services and grab your API key.

4. Create a .env file

CURRENTS_API_KEY=your_api_key_here

5. Run the app

bashpython app.py

Then open http://127.0.0.1:5000 in your browser.

🎨 Design Notes

The layout and card structure were built from scratch using CSS. AI tools were used to assist with styling refinements — including the colour scheme, card hover effects, and responsive grid layout — which I then reviewed, tweaked, and adjusted to fit the overall design direction I had in mind.

📌 Notes

Some articles may not include an image; a placeholder is shown in those cases, which is a simple grey background
This is a development project and is not deployed publicly.
This project is used to demonstrate my skills in FLASK and basic python, css and html.
