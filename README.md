# Area indexing structure

Solution to area-indexing problem, written in Python using TDD.

## Requirements

Python 3.7 and pipenv are required.

## Commands

Install environment:  
`pipenv install`

Run tests (using pipenv interpreter):  
`python -m pytest app/tests`

Run measurements (using pipenv interpreter):  
`python measurements.py`

## Problem statement
Circular areas can be created on a plane in bulk. Areas are defined by:
- latitude
- longitude
- radius
- id

The goal is to find the most efficient way of checking which areas contain given point.  
This should be achieved using the following interface:

```python
class BaseAreaIndex(ABC):

    @abstractmethod
    def bulk_create(self, areas):
        """
        :param list(tuple) areas: area description should contain latitude, longitude, radius and id.
        """

    @abstractmethod
    def query(self, lat, long):
        """
        :param float lat:
        :param float long:
        :return: all areas that include given point.
        :rtype: list
        """
```

## Remarks
Sets were used instead of lists since it helps avoid errors with duplicate values and allows for useful operations (like set union).

There were no restrictions placed on latitude and longitude range because it doesn't impact the logic.

## Solutions
This repository contains a brute force solution as well as a more efficient one.

### Brute force
Brute force solution saves all areas in a list and iterates over them, checking whether given point is within an area using circle equation.
We can notice that:
- The more areas there are the longer it takes to check them.  
- No matter how many areas there are - it takes the  same amount of time to check one of them.  

Therefore time complexity is `O(n)`.  
Implementation of brute force solution can be found in `app.structure.SimpleAreaIndex`.


### Range-based solution
During `bulk_create`:
1. Calculate boundaries for each area (min/max latitude/longitude)
2. Project latitude and longitude boundaries at X and Y axes
3. Save a set of areas for each section of each projection

During `query`:
1. Select sets of areas for corresponding latitude and longitude ranges
2. Discard areas that are not present in both sets
3. Verify all selected areas using circle equation

More detailed examples of projections can be found in `app.tests.test_range`.

Disadvantages:
1. Takes up more memory than brute force
2. Takes more time to create the structure
3. More complex then brute force

Advantages:
1. No need to iterate over all areas which makes querying faster

Implementation of brute force solution can be found in `app.structure.RangeBasedAreaIndex`.

Time complexity is still `O(n)` but this solution allows us to discard unneeded areas faster.

Measurements showed almost 2 times faster performance with range-based solution.
```
# Initializing simple area index: 0.0009999275207519531
# Initializing range based index: 0.008000612258911133
# Querying simple area index: 20.059147357940674
# Querying range based index: 12.539716958999634
```

## Known issues
`app.range` requires further refactor, but thankfully there are unit tests.
