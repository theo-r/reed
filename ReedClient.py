import requests
from requests.auth import HTTPBasicAuth

ROOT_URL = 'https://www.reed.co.uk/api/1.0/search?'
JOB_DETAILS_ROOT = 'https://www.reed.co.uk/api/1.0/jobs/'


class ReedClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def search(self, **args):
        return self.process_request(ROOT_URL, args)

    def process_request(self, url, args):
        auth = HTTPBasicAuth(username=self.api_key, password='')
        r = requests.get(url, auth=auth, params=args)
        jobs = r.json()['results']
        total_results = r.json()['totalResults']
        jobs_to_skip = 100

        while jobs_to_skip < total_results:
            args['resultsToSkip'] = jobs_to_skip
            r = requests.get(url, auth=auth, params=args)
            new_jobs = r.json()['results']
            jobs.extend(new_jobs)
            jobs_to_skip += 100

        return jobs

    def job_details(self, job_id):
        url = JOB_DETAILS_ROOT + str(job_id)
        return self.process_job_details_request(url)

    def process_job_details_request(self, url):
        auth = HTTPBasicAuth(username=self.api_key, password='')
        r = requests.get(url, auth=auth)
        return r.json()
