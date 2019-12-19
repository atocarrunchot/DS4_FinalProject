# Project Scope

## Introduction:

Colombia’s power generation matrix is 70% hydroelectrically based which means that hydrology (study of the movement, distribution and management of water) has a huge impact in the national price of energy. It is well known that the price of power generation is inversely related to the water supply availability in areas where the National Interconnected System (SIN) has hydroelectric power plants.

The power system comprises different entities that make the analysis and understanding of their relationships a challenging endeavor. The first main component are the generators, these are companies in charge of the power generation, as mentioned before, most of the power generated in Colombia comes from hydroelectric power stations, however other sources contributing to the power generation are fossil fuels, coal, eolian energy, etc. All these generators are connected to a national grid system where other entities, distributors and trading companies, are responsible for the billing and distribution to the industries and households. At the center of this process there is a coordinator which oversees the whole system. This coordinator must plan and track the power system in order to guarantee constant supply of electric energy to the country, moreover they are in charge of managing the electric market and distributing the money earned by each one of the generators. 

All these entities, as well as other variables (water sources location, weather, etc.), make the price of electric energy highly fluctuating and there is not a clear understanding of how much each factor contributes to this variability.

## Scope:

This project aims to characterize the price variability of power generation in the Interconnected National System (SIN) based on the space-time variability of the water supply available in the SIN generation areas.

## Hypothesis: “Space-time hydrological variability affects the price of energy in Colombia"


## Data sources:

The data of interest has been trimmed down to the following datasets

- National Oceanic and Atmospheric Administration (NOAA): macroclimatic indicators
XM: Operation Coordinator (data from 2000 to 2019)
The data can be found in different modules

- Hydrology Module: contributions, reserves, and monthly discharges (Water dumpings)
Offer Module: Real availability (Kwh), agents, sources, etc.
Transactional and Price Modules, National stock price.

All operational data can be found in daily format. The data can be found in the following link (http://informacioninteligente10.xm.com.co/Pages/Default.aspx)

- Geographical: Reservoir location
TRMM Precipitation: Precipitation data taken with remote sensor in the tropics

## App: 

The proposed project contemplates a dashboard implementation where the relationships between the different variables are related to the price of electric energy as a function of time.

Primary users: The projected client for this project is the coordinator (XM), for whom a better understanding of the impact of space-time variability of water supply is crucial in planning the system response for the country’s needs. 

## Versions: Initially there are three proposed versions

- **V-I**: Simple dashboard that groups the data monthly and shows the overall effect of the variables found to influence the price of electric energy in Colombia. 

- **V-II**: Dashboard that groups the data daily and shows the critical variables that determine the price of electric energy

- **V-III**: Forecasting model of the price of electric energy as a function of the critical variables/features found to be the most influential on the price variability. In this final version the proposed forecasting model might be trained from either daily or monthly data depending on the findings in the previous stages.

The general workflow of the app development process involves the following stages:

- Stage 0: Analysis of the modules and their relationships (EDA)
- Stage 1: ETL Process: preparation, normalization and uploading of the data to the database
- Stage 2: Factor visualization dashboard
- Stage 3: Modeling, validation and predictor deployment

