# Redash YouTube Analytics Chat Add-on

## Overview

Our company aims to significantly enhance its data analysis capabilities, focusing on comprehensive YouTube data exploration. This project involves building a Redash chat add-on that enables team members to extract insights from multiple Redash dashboards and connected databases using natural language. The add-on facilitates seamless conversation in a question-and-answer format, empowering autonomous knowledge discovery.

## Business Need

Our company's BI dashboards serve not only to monitor business processes but also to transform data collected from various systems into actionable insights. This project aims to offer a competitive edge in understanding digital content consumption trends and drive strategic decisions based on comprehensive data analysis.

## Scope

The project encompasses:

- Developing a Redash add-on in the frontend and an intelligence backend.
- Translating user queries into:
  - Summary of visualizations in the current dashboard.
  - Insights about data returned by existing SQL queries.
  - Auto-generated SQL queries and visualizations.
  - Auto-generated new Redash dashboards from existing and auto-generated SQL queries and their associated visualizations.

## Data

The data includes:

- Video metadata for all videos uploaded to our YouTube channel.
- Time series viewership metadata for all videos uploaded to our YouTube channel.
- Time series comments for all videos uploaded to our YouTube channel.
- Time series transcribed text for selected videos uploaded to our channel.


## Repository structure

```
.
├── backend                 <--- Quack backend code
│  ├── controllers          <--- API controllers
│  ├── Models               <--- Models/Entities.
│  ├── services             <--- nlp, db, and redash services.
│  ├── utils                <--- Helper and utils functions.
│  └── app.py               <--- API entry point
├── data                    <--- Where data should be located.
├── redash                  <--- Redash source code with chat plugin
│  |── client               <--- Front end code of the project
│  |── redash               <--- Backend logic
│  └── make                 <--- Make file for docker configs
├── tests                   <--- Unit tests for python code.
│  └── backend              <--- VBackend tests
├── README.md               <--- This file
└── requirements.txt        <--- Dependencies

```

## Key Components

### Quart Backend

The Quart backend serves as the intelligence engine for the Redash YouTube Analytics Chat Add-on. It provides the necessary endpoints and logic to handle user queries, translate them into actionable tasks, interact with the database, and communicate with the frontend.
Features

 * Natural Language Processing (NLP): Utilizes NLP techniques to understand user queries in natural language format.
 * SQL Query Generation: Generates SQL queries based on user input to retrieve data from the connected databases.
 * Data Retrieval and Processing: Handles data retrieval from the database and processes it to generate insights or visualizations.
 * Integration with Redash: Communicates with the Redash frontend to provide seamless interaction within the Redash environment.


### Redash
Redash helps you make sense of your data, it connect and query your data sources, build dashboards to visualize data and share them with your company.Combined with the backend Redash empowers users to effortlessly transform their natural language queries into actionable insights through dynamically generated dashboards. By leveraging cutting-edge technologies and intuitive user interfaces, automatic dashboard generation streamlines the data exploration process, enabling users to make informed decisions more efficiently.


## Setup Instructions

1. Clone this repository to your local environment.
2. Install requirements
3. Setup .env file and write important keys
4. run the make file on redash folder
5. run the backend backend/app.py

## Usage

Once the setup is complete, login to redash and write your questions to generate and visualize from your youtube source.

## Contributors

- [@abyt101](https://github.com/AbYT101) - Abraham Teka

<br>

## Challenge by

![10 Academy](https://static.wixstatic.com/media/081e5b_5553803fdeec4cbb817ed4e85e1899b2~mv2.png/v1/fill/w_246,h_106,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/10%20Academy%20FA-02%20-%20transparent%20background%20-%20cropped.png)
