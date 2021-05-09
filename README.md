# tech_savvy_Maverick

## CrossSell_Upsell Problem Statement

In this project, we have built a hybrid recommender system based on user based collaborative filtering and context aware filtering technique to recommend products to the customer for cross selling and upselling. Unsupervised learning algorithm K-Means Clustering is used to determine the location cluster to which the customer belongs based on their geographical coordinates. The insights gained from this are used to suggest products based on user-user based cosine similarity. This recommender system will thus help to increase its profit margins.

## Steps to run the app locally:

1. Download the github zip file submitted and unzip it or clone the repo. 
2. Python3 should be pre-installed in your local machine. 
3. Open the terminal and create a virtual environment by running the following command:
```
python3 -m venv env
```
4. To activate the virtual environment just created run the following command:
```
.\env\Scripts\activate
```
5. To install all the required modules, run the following command:
```
pip install -r requirements.txt
```
6. To run the app:
```
env FLASK_ENV=development FLASK_APP=app.py flask run
```
7. Open http://127.0.0.1:5000/apidocs on your web browser to use the app.
8. After getting recommendations, if you wish to see the map (story behind the given predictions) open http://127.0.0.1:5000/map on the web browser.
9. To view the ipynb file with folium map displayed, go to https://nbviewer.jupyter.org and enter https://github.com/bafnayash/tech_savvy_Maverick/blob/main/Maverick_2.ipynb in the box.

## UI

<img src = "https://github.com/bafnayash/tech_savvy_Maverick/blob/main/UI_screenshots/UI1.png" height = "261" width = "464"> <img src = "https://github.com/bafnayash/tech_savvy_Maverick/blob/main/UI_screenshots/UI2.png" height = "261" width = "464" align = "right">
<br> <br>
<img src = "https://github.com/bafnayash/tech_savvy_Maverick/blob/main/UI_screenshots/Recommend.png" height = "261" width = "464"> <img src = "https://github.com/bafnayash/tech_savvy_Maverick/blob/main/UI_screenshots/Map.png" height = "261" width = "464" align = "right">
