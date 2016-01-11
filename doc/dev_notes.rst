AIKIF Dev Notes
===================================================
Current Tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- mapper to read CSV files
provide sample CSV files

- logging
use logging module instead of standard file logging in cls_log

- bias
bias module mostly working, but values will need tweaking (when all 
areas are multiplied the result is too low - may need to change from 
0 -> 1 to 0 -> 2 where 1 is 'no difference'

- core data
using the core data module, load sample data to core tables via bias module

Upcoming Tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- integrate vais to run simulations. Should include world.py and environment.py


Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- Ontology - not sure whether to create core ontology, or allow one to be derived.



Log of Work
---------------------------------------------------

- 2015-11-28 Started Developers logbook
Made this file to keep focused on core concepts

- 2015-11-29 Working on Bias calculation.
Not sure if this is final implementation but Bias class currently needs
all parameters to do calculation. Need another class to handle the mapping
of CoreData or information with partial metadata to call the Bias class.

changed start bias to 1 instead of zero as each metadata element uses 
multiplication, meaning it would have always been zero
    self.bias_rating = 1  # everything starts unbiased
    
Started Controversy class stub to handle noise and disputes on facts

- 2015-12-03 Bias starting values
Originally returned a weighting from 0 to 1 based on the sources.
Due to fractions multiplying resulting in very small numbers, adding 0.5 to bias calculations which means actual range is 0.5 -> 1.5 (still testing)
    
- 2015-12-08 Rethinking Ontology
Will not be linking to upper Ontology as originally intended so will focus on the mapping process and classifications.

- 2015-12-19 updating Toolbox and adding additional tools

- 2016-01 Research Notes: core_data
Started scripts/res_core_data.rst which is an automatically generated RST file which I hope will show the usefulness of the various methods of mapping data. Have tried several methods in AIKIF so the idea is to document the methods so as not to repeat past mistakes.