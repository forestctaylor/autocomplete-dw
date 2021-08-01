The application's backend is hosted with Flask, the frontend is a vanilla ReactJS application. 

To run this application, first we need to serve the backend. Point a terminal at the `autocomplete-dw-services` directory and run the following commands:
    - `$env:FLASK_APP = "flaskr"`
    - `$env:FLASK_ENV = "development"`
    - `python -m flask run`

To point the UI at the backend, navigate to the `autocomplete-dw-UI` directory with a terminal and run the following command:
    - `npm start`

A browser should pop up, otherwise navigate to `http://localhost:3000`, where the UI is hosted.