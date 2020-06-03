import requests
from requests.auth import HTTPBasicAuth

ROOT_URL = 'https://www.reed.co.uk/api/1.0/search?'
JOB_DETAILS_ROOT = 'https://www.reed.co.uk/api/1.0/jobs/'


class ReedClient:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def search(self, **args):
        return self.process_request(ROOT_URL, args)

    def process_request(self, url, args):
        auth = HTTPBasicAuth(username=self.api_key, password='')
        r = requests.get(url, auth=auth, params=args)
        jobs = r.json()['results']
        total_results = r.json()['totalResults']

        if 'resultsToTake' in args.keys():

            if args['resultsToTake'] <= 100:
                return jobs

            else:
                results_to_take = args['resultsToTake']

        else:
            return jobs

        jobs_to_skip = 100
        remaining_jobs = results_to_take - jobs_to_skip

        while (len(jobs) < results_to_take) and (len(jobs) < total_results):
            args['resultsToSkip'] = jobs_to_skip
            args['resultsToTake'] = remaining_jobs
            r = requests.get(url, auth=auth, params=args)
            new_jobs = r.json()['results']
            jobs.extend(new_jobs)
            jobs_to_skip += 100
            remaining_jobs = results_to_take - jobs_to_skip

        return jobs

    def job_details(self, job_id):
        url = JOB_DETAILS_ROOT + str(job_id)
        return self.process_job_details_request(url)

    def process_job_details_request(self, url):
        auth = HTTPBasicAuth(username=self.api_key, password='')
        r = requests.get(url, auth=auth)
        return r.json()
