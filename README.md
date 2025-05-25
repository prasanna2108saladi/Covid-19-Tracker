Project Name: Real-time COVID-19 Tracker
Overview:
This project is a web-based application that provides live, up-to-date statistics on COVID-19 cases worldwide. It allows users to view the number of confirmed cases, recoveries, and deaths for selected countries in real-time.

Technologies Used:

Python as the backend programming language

Flask web framework to build the server and render web pages

HTML, CSS, JavaScript for frontend UI

Public API (such as disease.sh or covid19api.com) to fetch real-time COVID-19 data

Key Features:

Fetches live COVID-19 data from a trusted API

Displays global statistics as well as country-specific data

Responsive UI allowing users to select countries dynamically

Shows data points including total cases, active cases, recoveries, and deaths

Real-time updates without requiring manual page refresh (can be improved with AJAX or Flask features)

How It Works:

The Flask backend sends an API request to the COVID-19 data source whenever the user requests data for a specific country.

The API responds with the latest statistics in JSON format.

Flask processes this data and renders it dynamically into an HTML template (index.html) using Jinja2 templating.

The frontend displays the formatted data clearly and intuitively to the user.

Challenges Faced:

Handling asynchronous API calls and ensuring the data is updated smoothly

Managing errors when the API fails or returns unexpected data (implemented basic error handling)

Designing a clean UI that presents complex data simply and understandably

Learning Outcomes:

Gained hands-on experience with REST APIs and JSON data processing

Improved skills in building web applications using Flask and templating engines

Learned how to integrate backend and frontend components effectively

Understood the importance of real-time data handling and user experience in live applications

Potential Future Improvements:

Add interactive charts to visualize trends using libraries like Chart.js or Plotly

Implement search autocomplete for country selection

Cache API responses to reduce latency and API calls

Make the app fully mobile-responsive with improved UI design

Add user authentication to allow personalized saved views
