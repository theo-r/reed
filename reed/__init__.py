""" Reed API """
from time import time, sleep
from requests import Session
from requests.auth import HTTPBasicAuth

ROOT_URL = "https://www.reed.co.uk/api/1.0/search?"
JOB_DETAILS_ROOT = "https://www.reed.co.uk/api/1.0/jobs/"
MAX_ATTEMPTS = 3
OFFSET = 100


class ReedClient(Session):
    """ ReedClient which inherits the requests.Session object """
    def __init__(self, api_key: str) -> None:
        self.auth = HTTPBasicAuth(username=api_key, password='')
        self.last_call = time()
        super().__init__()

    def get(self, url, **kwargs):
        """ GET request with response raising for status when not ok """
        kwargs.setdefault("auth", self.auth)
        delay = kwargs.pop("delay", 3)
        attemps = 0
        response = super().get(url, **kwargs)
        while response.status_code == 429 or attemps < MAX_ATTEMPTS:
            delay = response.headers.get("Retry-After", delay)
            sleep(min(0, (self.last_call + delay) - time()))
            response = super().get(url, **kwargs)
            self.last_call = time()
            delay += 1
            attemps += 1
        if not response.ok:
            response.raise_for_status()
        self.last_call = time() + response.headers.get("Retry-After", 0)
        return response

    def search(self, **kwargs) -> list:
        """ Perform a job search with given key word arguments. """
        jobs = self.get(ROOT_URL, **kwargs).json()["results"]
        if kwargs.get("resultsToTake", OFFSET) <= OFFSET:
            return jobs
        remaining_jobs = kwargs["resultsToTake"] - OFFSET
        while remaining_jobs > 0:
            kwargs.update({
                "resultsToSkip": OFFSET, "resultsToTake": remaining_jobs})
            jobs.extend(self.get(ROOT_URL, **kwargs).json()["results"])
            remaining_jobs -= OFFSET
        return jobs

    def job_details(self, job_id: int) -> dict:
        """ Retrieve details of the job with given id. """
        if not isinstance(job_id, int):
            raise ValueError("{job_id!r} must be type {int!r}")
        return self.get(JOB_DETAILS_ROOT + str(job_id)).json()
