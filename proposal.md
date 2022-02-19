### Motivation and purpose:

Our role: Independent data science consultants

Target audience: Client - a workplace wellbeing consultancy and their
respective employer clients.

Our client is a global workplace wellbeing consultancy startup. Their
core product offering, the Quality of Work Life survey and accompanying
report (QWL) measures workplace wellbeing through a comprehensive
assessment of company culture, employee health, and employee access to
health and wellbeing services. Right now, despite having many large
clients, all of their analysis and reporting is still done by hand in
Excel spreadsheets. Our app will pull the employee survey responses from
CSV files, and generate different visualisations of the data to answer
questions about the most important areas of focus for a given employer
to improve or maintain their culture of employee health and wellbeing.

In the short term, this will have two key benefits for our client: 1)
They will save time in generating future reports, whereby they can pull
charts directly from the dashboard, which aligns to best practises in
data visualisation, rather than creating them manually; and 2) They will
be able to rapidly generate different visualisations for slices of the
data - this is particularly useful if they are on a call with one of
their employer clients who asks a specific question, like “what are the
average wellbeing scores across employees of different seniorities in
JUST our Hong Kong offices?”

In the medium to long term, this will also be able to be rolled out
directly to BEI Vita’s clients so that they can gain these insights
directly on an ongoing basis. We will base our use case and project on
the medium to long term goal of creating an employer facing dashboard,
to answer the overarching question “How is the health of my employees,
and in what ways can I support their health?”

### Description of the data

The dashboard will be visualising a dataset describing survey data. This
dataset is derived from the Quality of Work Life survey, an internally
compiled data from BEI Vita based on responses from a single employer
client company. The dataset contains over 147 rows of data and provides
useful information about employee health and wellbeing building on a set
of survey questions. A timestamp for each employee response is a row in
the dataset where employee id and any personal information is completely
anonymized. Given the nature of survey, boolean, categorical and ordinal
data types are predominant in the dataset.

As our aim is to develop a solution to help BEI Vita and their clients
easily understand employee wellbeing, the dashboard will focus primarily
on numeric columns that include an advanced calculation for an overall
score, ordinal features (ranking questions) and quantitative metric
derived from responses given in the survey for their experience. These
variables will be useful in providing insights on the current state of a
company’s employee’s wellbeing and health.

### Research questions and usage scenarios

#### Case Scenario:

We were hired as Data Science Consultants, by a global workplace
wellbeing consultancy startup BEI Vita. The startup consults for other
big companies across the globe and suggests areas of improvements with
respect to employee wellbeing, company culture and employee retention.
To better gauge the health of the company they consult, they carry out
employee surveys. BEI Vita collects and analyses these surveys, manually
generates dashboards and insights and benchmarks the key employee
wellbeing KPIs against the global standard.

While the immediate ‘case in point’ is the application described in
motivation and purpose, we have decided to illustrate the long-term goal
of this project to be a client facing dashboard, as it illustrates both
any internal uses BEI Vita might have for the dashboard in the
short-term, as well as all utility to their clients in the long-term.

#### Case in Point:

Ms. Guan Yin, is the Chief Human Resource Officer(CHRO) of HCTC, a
global bank with presence in Asia, Europe and Americas. Due to the
prevailing worldwide pandemic, she keeps getting the news that the
employees are quitting their jobs and those who are staying are not very
motivated. To gauge the impact and to take corrective actions she has
hired “BEI Vita”, a startup who are experts in this field.

BEI Vita has reached out to us for help with this assignment and to make
an automated dashboard that they can use across different clients. Right
now, despite having many large clients, all of their analysis and
reporting is still done by hand in Excel. They want make a holistic
dashboard so that when an user (in this case Ms. Guan Yin) logs on to
the “Quality of Work Life” dashboard, she will be able to explore data
collected through the survey and to interpret the effect of different
factors on employee health and well-being. This would help identify the
areas of intervention and improvements. She wants the dashboard to be
sufficiently detailed and flexible so that she can view these measures
across different geographies and different employee levels (seniorities/
ranks).

When Ms. Guan Yin looks at the dashboard, she may find that the
employees in developing countries are not very engaged, and in
particular that they are struggling with their feelings of fulfilment.
From these insights, she decides to then contract BEI Vita to train the
senior and mid-level managers of these geographies on how to motivate
their colleagues and reportees.
