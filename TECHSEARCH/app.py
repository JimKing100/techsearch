# Import Flask package

from flask import Flask, request, render_template
import pandas as pd
import re
import string


def create_app():
    # Create Flask web server, makes the application
    app = Flask(__name__)

    # Routes determine location
    @app.route("/")
    def home():
        return render_template('index.html')

    @app.route("/search", methods=['GET'])
    def input():
        return render_template('search.html')

    @app.route("/output", methods=['POST'])
    def output():
        df = pd.read_csv('https://raw.githubusercontent.com/JimKing100/techsearch/master/data/scrape_results1.csv')
        df = df.drop(df.columns[0], axis=1)

        title = request.values['title']
        city = request.values['city']
        result_df = df.loc[(df['job'] == title) & (df['city'] == city)]
        r_title = result_df['job'].iloc[0]
        r_city = result_df['city'].iloc[0]
        r_count = result_df['counts'].iloc[0]
        r_lsalary = result_df['low_salary'].iloc[0]
        r_hsalary = result_df['high_salary'].iloc[0]

        r_skills = re.sub('['+string.punctuation+']', '', result_df['skills'].iloc[0]).split()

        return render_template('response.html',
                               title='Search Results',
                               r_title=r_title,
                               r_city=r_city,
                               r_count=r_count,
                               r_lsalary=r_lsalary,
                               r_hsalary=r_hsalary,
                               r_skills=r_skills
                               )

    @app.route("/about")
    def about():
        return render_template('about.html')

    return app
