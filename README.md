# Python wrapper for the Reed API

## API Paramaters

### Job Search

**q** - 
Query. By default terms are ANDed. To see what is possible, use our [advanced search](http://www.indeed.com/advanced_search) page to perform a search and then check the url for the q value.

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