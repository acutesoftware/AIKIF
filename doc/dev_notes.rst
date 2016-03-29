AIKIF Dev Notes
===================================================
Current Tasks
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
- mapper to read CSV files
provide sample CSV files

- bias
bias module mostly working, but values will need tweaking (when all 
areas are multiplied the result is too low - may need to change from 
0 -> 1 to 0 -> 2 where 1 is 'no difference'

- core data
using the core data module, load sample data to core tables via bias module

- agents
 issue with using Agents in worlds (under VAIS)

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

- 2016-01-14 Moved World generator to VAIS package
moved the worlds.py, world_generator.py and associated tests from AIKIF to VAIS (virtual-AI-simulator) package.
Makes sense for VAIS to handle worlds rather than AIKIF which needs to focus on the actual data handling. 

- 2016-01-19 mapper get_maps_stats
working on mapper to show basic stats of map files

- 2016-01-31 fixing issues with using Agents in worlds (under VAIS)
agent location needs to be fully redone in a later stage. At the moment VAIS holds the old AIKIF World and WorldGenerator class which run agents, however the locations of the agents are stored and managed separately which isnt optimal.

- 2016-02-05 testing loading real data
setting up local folder and config / mappings to load real data. Not many changes likely to AIKIF package apart from new toolbox modules.
The external program should use the package via config files.

- 2016-03-29 clean up of tests 
Clean up tests and remove redundant print statements. Show output on both Linux and Windows
