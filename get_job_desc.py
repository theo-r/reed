import json
from util.HTMLParser import MyHTMLParser

import click

from ReedClient import ReedClient


@click.command()
@click.option('--job_id', default=1, help='Reed job id')
def print_job_desc(job_id):
    """Simple program that displays job descriptions."""
    with open('creds.json', 'r') as f:
        creds = json.load(f)

    API_KEY = creds['API_KEY']
    client = ReedClient(API_KEY)
    result = client.job_details(job_id=job_id)
    job_desc_html, job_url = result['jobDescription'], result['jobUrl']
    parser = MyHTMLParser()
    print(job_url)
    parser.feed(job_desc_html)


if __name__ == '__main__':
    print_job_desc()
