#!/usr/bin/env python2

# DB- API Code to connect to PostgreSQL database

import psycopg2

# Top 3 articles query
top_three_article_query = """select ar.title, count(*) as num from log l,
                        articles ar where ar.slug = substring(l.path,10)
                        and status = '200 OK' group by ar.title order by
                        num desc limit 3;"""

# Popular authors query
popular_author_query = """select au.name, count(*) as num from log l,
                        articles ar, authors au where ar.slug =
                        substring(l.path,10) and ar.author = au.id and
                        status = '200 OK' group by au.name order by num
                        desc;"""

# Day where pages view results in more than 1% error query
error_query = """select date(time) as day,
                round(100.0*sum(case status when '200 OK' then 0 else
                1 end)/count(status),2) as percent from log group by
                day having round(100.0*sum(case status when '200 OK'
                then 0 else 1 end)/count(status),2) > 1.0 order by day;"""


def run_query(query):
    """Connects to database news and executes the input query and
    fetches the statement results in the results variable"""
    db_connect = psycopg2.connect("dbname=news")
    statement = db_connect.cursor()
    statement.execute(query)
    results = statement.fetchall()
    db_connect.close()
    return results


def get_results(results):
    """Individually pulls the results from and prints output in plain text."""
    for result in results:
        print '\t' + str(result[0]) + ' - ' + str(result[1])
    print '\n'


def top_three_articles():
    """Return the top three articles visited from the news database"""
    print 'The top three article views from the news are (# in views):\n'
    results = run_query(top_three_article_query)
    get_results(results)


def popular_author():
    """Returns the most popular authors based on amount of views"""
    print 'The most popular authors ranked from high to low based on the ' \
          'amount of views (# in views):\n'
    results = run_query(popular_author_query)
    get_results(results)


def errors():
    """Returns the days when the article page loads in error"""
    print 'Days on which requests lead to more than 1 percent in errors ' \
          '(# in %):\n'
    results = run_query(error_query)
    get_results(results)


top_three_articles()
popular_author()
errors()
