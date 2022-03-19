# Quality of Work Life
A dashboard exploring Employee well being in corporate world across geographies

-   Authors: Abhiket Gaurav, Berkay Bulut, Kyle Ahn, Morgan Rosenberg

### Overview:
Employee wellbeing is a major concern in today's corporate world. Many employees quit their jobs as they find the work pressure to be too high, or company culture not suitable to their needs. It is commonly known in industry that to replace even the most junior employee is upwards of 25% of their annual salary; this figure only increases as seniority increases.

This dashboard will help employers view and understand the health of their employee base to then take proactive steps to keep their employees happy, healthy, and 'here' (retained). It can be used to monitor employee's work life quality in multiple dimensions such as their overall feeling, workshop preference and meaninfulness at work.

## Current Live Dashboard Image:
![alt text](https://github.com/UBC-MDS/quality_of_work_life/blob/main/doc/live_dashboard.png)

## Usefull Links:

- [Live Dashboard Link](https://quality-of-work-life-bei-vita.herokuapp.com/)
- [Proposal Link](https://github.com/UBC-MDS/quality_of_work_life/blob/main/proposal.md)


## Dashboard Filter:

1. Country: The work life quality data can be filtered by country. To get a better understanding on a global scale or a regional scale.
2. Nationality: The work life quality data can be filtered by nationality. To get a better understanding from a nationality perspective


## Explanation
This app is an executive summary of surveys that were conducted to identify the employees' quality of work life. On the top left corner, the name of the company, BEI Vita, is shown to represent where this dashboard belongs to. On the top centre, the name of the client that this dashboard is built for is included. The app contains a landing page that shows the distribution of important variables such as "contributor of employees' quality of work life", "ratings of employees feeling acknowledgment", and "total score of employees' quality of work life". On the top right corner, there are filters for users to select the relevant demographics and regions (i.e. survey results only from Japan). On the centre right, we have one label, "Average Score", which summarises all the data into a single KPI value for swift interpretation. On the very far right, there is a scroll bar to allow users to scroll up and down to view more content. Overall, this app offers a holistic view of the employees' quality of work life in one simple dashboard.

## Using with Docker
In order to use with Docker, you need to install Docker first on your machine. After installing Docker, you can run the following command to run the app:
1. Fist build the docker container image:
`docker-compose build --no-cache`
2. Run the docker container:
`docker-compose up`
3. Open the browser to the following link:
`http://localhost:8000`


## Contributing

Interested in contributing? Check out the [contributing guidelines](https://github.com/UBC-MDS/quality_of_work_life/blob/main/CONTRIBUTING.md). Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

For this project, we used `Dash` for dashboarding, `Altair` and `Plotly` for charts, and `Heroku` for deployment. Initial dashboard sketch can be found [here](https://github.com/UBC-MDS/quality_of_work_life/blob/main/doc/labelled_dashboard_sketch.png).

Do check out the following links to learn more about plotly and dash:

* [Dash Python User Guide](https://dash.plotly.com/)
* [Dash interactive visualization](https://dash.plotly.com/interactive-graphing)
* [Altair documentation](https://altair-viz.github.io/index.html)
* [Plotly Python documentation](https://plotly.com/python/)

## License

`quality_of_work_life` was created by Abhiket Gaurav, Berkay Bulut, Kyle Ahn, Morgan Rosenbery. It is licensed under the terms of the [MIT license](https://github.com/UBC-MDS/quality_of_work_life/blob/main/LICENSE).

## Contributors
---
The names of core development team is listed below.

|           Name          |
|:-----------------------:|
|      Abhiket Gaurav     |
|      Berkay Bulut       |    
|        Kyle Ahn         |
|    Morgan Rosenberg     |
