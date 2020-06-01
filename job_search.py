import urllib
import os

import click

from ReedClient import ReedClient
from util.DataProcessor import DataProcessor

env_vars = os.environ.copy()


@click.command()
@click.option('--query', required=True, type=str, help='Job search query')
@click.option('--num_jobs', default=10, help='Number of jobs to show')
@click.option('--since', default=7, help='How many days back to search')
@click.option('--location', default=None, type=str,
              help='Where to perform job search')
def main(query, num_jobs, since, location) -> None:
    API_KEY = env_vars['API_KEY']

    client = ReedClient(api_key=API_KEY)
    processor = DataProcessor()

    params = {
        'keywords': urllib.parse.quote_plus(query),
        'locationName': location
    }
    result = client.search(**params)

    all_jobs = processor.process_returned_data(result)

    relevant_jobs, date = processor.remove_irrelevant_jobs(all_jobs, since)

    if relevant_jobs.shape[0] == 0:
        print(f'Jobs posted since {date}: 0')
        return

    desired_cols = ['jobTitle',
                    'employerName',
                    'minimumSalary',
                    'locationName',
                    'jobId']

    num_rel_jobs = str(relevant_jobs.shape[0])
    print(f'Jobs posted since {date}: {num_rel_jobs}')
    print()

    for ind in relevant_jobs.index[:num_jobs]:
        job_info = relevant_jobs.iloc[ind][desired_cols]
        job_info['date'] = relevant_jobs.iloc[ind]['date'].strftime('%d %b')
        for field in job_info:
            print(field, end=' | ')
        print()
        print()


if __name__ == '__main__':
    main()
