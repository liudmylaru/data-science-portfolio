# Data Science Portfolio

Here is repository of data csience projects made by me presented in form of Jupyter Notebooks. Used data for the projects is in each project directory and for demonstration purposes only.

## Contents

- ### Machine Learning in Python

    - [Titanic competition](https://github.com/liudmylaru/data-science-portfolio/blob/master/20_datascience_workflow/titanic_for_kaggle.ipynb)\
    Goals: explore a workflow to make competing in the Kaggle Titanic competition.\
    Methods: preprocess and explore the data, engineer new features, select the best-performing features, select and tune different algorithms, make a submission to kaggle.

    - [Building A Handwritten Digits Classifier](https://github.com/liudmylaru/data-science-portfolio/blob/master/19_handwritten_digits_classifier/digits_classifier.ipynb)\
    Goals: build models that can classify handwritten digits.\
    Methods: K-nearest neighbors model, neural network with one, two and three hidden layers.
    
    - [Predicting Bike Rentals](https://github.com/liudmylaru/data-science-portfolio/blob/master/18_predict_bike_rentals/bike_rentals.ipynb)\
    Goals: using detailed data on the number of bicycles people rent by the hour and day, predict the total number of bikes people rented in a given hour.\
    Methods: explore correlated data, calculate features, linear regression, decision trees, random forests.

    - [ Predicting the stock market](https://github.com/liudmylaru/data-science-portfolio/blob/master/17_predict_stock_market/improved.py)\
    Goals: using historical data on the price of the S&P500 Index to make predictions about future prices.\
    Methods: handle datetime data, use rolling function to generate indicators for model, LinearRegression.

    - [Predicting House Sale Prices](https://github.com/liudmylaru/data-science-portfolio/blob/master/16_predict_house_sale_prices/house_sale_prices.ipynb)\
    Goals: predict house sale price with housing data for the city of Ames, Iowa, United States from 2006 to 2010.\
    Methods: set up a pipeline of functions, feature engineering, feature selection, train and test with LinearRegression model.

    - [Predicting Car Prices](https://github.com/liudmylaru/data-science-portfolio/blob/master/15_predict_car_prices/car_prices.ipynb)\
    Goals: predict a car's market price using its attributes.\
    Methods: k-nearest neighbors algorithm.

- ### Probability and Statistics in Python

    - [Winning Jeopardy](https://github.com/liudmylaru/data-science-portfolio/blob/master/14_winning_jeopardy/winning_jeopardy.ipynb)\
    Goals: work with a dataset of Jeopardy questions to figure out some patterns in the questions that could help to win.\
    Methods: normalize text and columns, find ovelapping answers and questions, apply chi-squared test for low-value and high-value questions.
    
    - [Finding the Best Markets to Advertise In](https://github.com/liudmylaru/data-science-portfolio/blob/master/13_find_best_markets_to_advertise_in/best_markets.ipynb)\
    Goals: to find out the two best markets to advertise programming courses of the e-learning company.\
    Methods: summarize distributions, measure the variability of a distribution.

    - [Investigating Fandango Movie Ratings](https://github.com/liudmylaru/data-science-portfolio/blob/master/12_fandango_movie_ratings/movie_ratings.ipynb)\
    Goals: analyze more recent movie ratings data to determine whether there has been any change in Fandango's rating system after Hickey's analysis.\
    Methods: sampling, variables, scales of measurement, and frequency distributions. 

- ### SQLite and Python

    - [Designing and Creating a Database](https://github.com/liudmylaru/data-science-portfolio/blob/master/11_design_create_batabase/create_db.ipynb)\
    Goals: use statistics on baseball games from the 1800s (from https://www.retrosheet.org/) to design and create a database.\
    Methods: import data into SQLite, design a normalized database schema, create tables for schema, insert data into schema.

    - [Answering Business Questions using SQL](https://github.com/liudmylaru/data-science-portfolio/blob/master/10_%20answer_business_questions_with_sql/%20business_q_a_with_sql.ipynb)\
    Goals: analyze the Chinook database, which contains information about a fictional digital music shop - like a mini-iTunes store.\
    Methods: sql query to extract the relevant data and create plots where necessary to visualize the data.

    - [Analyzing CIA Factbook Data](https://github.com/liudmylaru/data-science-portfolio/blob/master/09_analys_cia_factbook_with_sqlite/cia_factbook_with_sqlite.ipynb)\
    Goals: use Python SQLite workflow to explore, analyze, and visualize data from CIA Factbook Data.\
    Methods: select summary statistics, outliers, use subqueries, cast resuls.

- ### Python for Data Analysis

    - [Star Wars Survey](https://github.com/liudmylaru/data-science-portfolio/blob/master/08_star_wars_survey/star_wars_survey.ipynb)\
    Goals: use survey data to declare that “The Empire Strikes Back” is the best of the Star Wars movies.\
    Methods: clean and mmap yes/no, checkbox and rank columns, use mean() and sum() on columns to find highest-ranked and most seen movie, use binary segments (gender) to analize data.

    - [Analyzing NYC High School Data](https://github.com/liudmylaru/data-science-portfolio/blob/master/07_nyc_high_school_data/nyc_high_schools.ipynb)\
    Goals: compare demographic factors such as race, income, and gender with SAT scores to determine whether the SAT is a fair test.\
    Methods: plot bar of the correlations, scatter plot, make a map by district. 

    - [Clean And Analyze Employee Exit Surveys](https://github.com/liudmylaru/data-science-portfolio/blob/master/06_%20clean_employee_exit_surveys/clean_exit_surveys.ipynb)\
    Goals: combine the results for surveys from employees in two depatments of institute to answer the qestions about reasons of resigning.\
    Methods: clean data with vectorized string methods, transform data with apply() and applymap(), drop missing or unnecessary values with fillna(), dropna(), and drop(), combine data with concat().

    - [Visualizing The Gender Gap In College Degrees](https://github.com/liudmylaru/data-science-portfolio/blob/master/05_visualize_gender_gap_in_degree/gender_gap.ipynb)\
    Goals: visualizing the gender gap across college degrees in STEM fields, which stands for science, technology, engineering, and mathematics.\
    Methods: subplot grid layout, hide x-axis labels, set y-axis labels, add a horizontal line, export to a file.
    
    - [Visualizing Earnings Based On College Majors](https://github.com/liudmylaru/data-science-portfolio/blob/master/04_visualize_salaries_after_college/salaries_after_college.ipynb)\
    Goals: explore and analize dataset on the job outcomes of students who graduated from college using visualizations.\
    Methods: pandas, scatter plots, histograms, scatter matrix plot, bar plots.

    - [Exploring Ebay Car Sales Data](https://github.com/liudmylaru/data-science-portfolio/blob/master/03_clean_data_used_cars/used_cars.ipynb)\
    Goals: clean the data and analyze the included used car listings.\
    Methods: map column names, convert string columns to numeric, work with outliers, explore datetime data, handle incorrect years data, aggregate and combine data to explore.
    
    - [Exploring Hacker News Posts](https://github.com/liudmylaru/data-science-portfolio/blob/master/02_hacker_news/hacker_news.ipynb)\
    Goals: analyse "Ask" and "Show" posts from Hacker News site to determine which more popular and find out is there a better time to publish posts to get more reads.\
    Methods: manipulate strings, work with timedate datatype, use object-oriented concepts.
    
    - [App Profiles for the App Store and Google Play Markets](https://github.com/liudmylaru/data-science-portfolio/blob/master/01_mobile_app_profiles/mob_apps.ipynb)\
    Goals: analyze data about approximately 10,000 Android apps from Google Play and approximately 7,000 iOS apps from the App Store to understand what type of apps are likely to attract more users.\
    Methods: clean data, select relevant to the goal data, work with frequency tables.
