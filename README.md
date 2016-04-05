# edeals

This is the code associated with the EDEALS project as currently outlined in [our paper](https://www.usenix.org/conference/cooldc16/workshop-program/presentation/mcfadden) from the USENIX Workshop on Cool Topics on Sustainable Data Centers (CoolDC 16).

The project aims to assess the energy usage statistics of a moderately sized HPC datacenter toward the goal of reducing the datacenter's electricity bills and C02 footprint via [demand response load shifting](https://en.wikipedia.org/wiki/Demand_response).

These routines make up part of a larger project to develop demand response plug-ins for SLURM scheduler.

The project consists of 
1. [cluster electricity data API](tree/master/energy_data_collection_API), 
2. [analysis ipython notebooks](tree/master/prod_cluster) for analyzing production cluster electricity and SLURM data, 
3. [experiments and analysis scripts](tree/master/test_cluster) for smaller test clusters,
4. a description of the [cost optimization framework](cost_optim) we have analyzed
5. the files used to generate our [manuscript](tree/master/manuscript).
