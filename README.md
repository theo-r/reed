# Python wrapper for the Reed API

## API Credentials

The API needs to be called with a reed.co.uk API Key. This key needs to be passed
into the ReedClient constructor.

```python
from ReedClient import ReedClient

client = ReedClient(api_key=YOUR_API_KEY)
```

You can sign up for an API key [here](https://www.reed.co.uk/developers/jobseeker)

## API Parameters

### Job Search

**keywords** - 
Query. By default terms are ANDed.

**employerId** - 
id of employer posting job

**employerProfileId** -	
profile id of employer posting job

**keywords** - 
any search keywords

**locationName** -	
the location of the job

**distanceFromLocation** -	
distance from location name in miles (default is 10)

**permanent** - 	
true/false

**contract** -	
true/false

**temp** - 	
true/false

**partTime** -  	
true/false

**fullTime** - 
true/false

**minimumSalary** -	
lowest possible salary e.g. 20000

**maximumSalary** -	
highest possible salary e.g. 30000

**postedByRecruitmentAgency** -
true/false

**postedByDirectEmployer** -
true/false

**graduate** -	
true/false

**resultsToTake** -	
maximum number of results to return (defaults and is limited to 100 results)

**resultsToSkip** -	
number of results to skip (this can be used with resultsToTake for paging)