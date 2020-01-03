# techsearch
Winter Hackathon - Tech Job Search

The contents include the following:

data - the preprocessed data

- scrape_results.csv - An initial test set of the preprocessed data for use in testing the flask app.
- scrape_results1.csv - The final set of preprocessed data from 1/2/20 for use in the flask app.
- techsearch_p1.csv - Part 1 of the final set of scraped data from Indeed.com dated 1/2/20 scraping 15 pages per job/city.
- techsearch_p2.csv - Part 2 of the final set of scraped data from Indeed.com dated 1/2/20 scraping 15 pages per job/city.

preprocess - the preprocessing Jupyter notebooks

- nlp.ipynb - The Natural Language Processing (NLP) module converting the raw scraped data into the final dataframe.
- scraper.ipynb - The Indeed.com scraping module used to scrape the raw job listings by job and city.

configuration files - the files needed to set up and configure the proper environment

- Pipfile and Pipfile.lock - The environment files
- Procfile - The Heroku configuration file

TECHSEARCH - the Flask app

- static - a directory with the static web site content (css, images and other static content)
- templates - a directory with the html pages
- app.py - the main executable for the Flask app


 
