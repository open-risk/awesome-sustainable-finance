[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

**Awesome Sustainable Finance**

A curated list of sustainable finance resources. The focus of the list is i) on code (tools, libraries, frameworks etc.) that fairly directly support any type of sustainable finance effort, and ii) open data that are useful in a sustainable finance context.

![Solarpunk Flag](./Solarpunk_Flag.png)

Image Credit: StarwallOfRadical.town, [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0), via Wikimedia Commons

Are you interested to contribute to this collection? [Here is how](CONTRIBUTING.md)

# Contents

As the list grows we may introduce more / different sub-categories. The current classification is as follows

- [Open Source Frameworks](#open-source-frameworks)
  - [Climate Finance](#climate-finance)
  - [Carbon Footprint](#carbon-footprint)
    - [Cloud Carbon Footprints](#cloud-carbon-footprints)
  - [Biodiversity Finance](#biodiversity-finance)
  - [Circular Economy](#circular-economy)
  - [Integrated Assessment Models](#integrated-assessment-models)
  - [Social Finance](#social-finance)
    - [Financial Inclusion](#financial-inclusion)
    - [Financial Literacy](#financial-literacy)
- [Open Data](#open-data)
  - [GHG Emissions](#ghg-emissions)
  - [Energy System](#energy-system)
  - [Other Sustainability Data](#other-sustainability-data)
- [Related Domains](#related-domains)

# Open Source Frameworks

This section focuses on projects  (Models and Tools) that are primarily code oriented (models, tools etc.). Projects are grouped by domain.

## Climate Finance

Frameworks and tools that are *directly* assisting the analysis of financial operations (e.g., transactions, securities, portfolios of contracts etc.) from a climate finance perspective

- [PACTA](https://github.com/2DegreesInvesting/PACTA_analysis) - Run the PACTA analysis on EQ & CB portfolios.
- [r2dii.analysis](https://github.com/2DegreesInvesting/r2dii.analysis) - Tools to Calculate Climate Targets for Financial Portfolios. 
- [SBTi Temperature Alignment tool](https://github.com/ScienceBasedTargets/SBTi-finance-tool) - This toolkit helps companies and financial institutions to assess the temperature alignment of current targets, commitments, and investment and lending portfolios, and to use this information to develop targets for official validation by the SBTi.
- [Equinox](https://github.com/open-risk/equinox) - Equinox is an open source platform that supports the holistic risk management of sustainable finance projects.
- [OS-Climate](https://github.com/os-climate) - Open Source Solutions to Enable Climate-Smart Investing.
- [blockchain-carbon-accounting](https://github.com/hyperledger-labs/blockchain-carbon-accounting) - This project implements blockchain applications for climate action and accounting, including emissions calculations, carbon trading, and validation of climate claims. It is part of the Linux Foundation's Hyperledger Climate Action and Accounting SIG.
- [ESG Reg Reporting](https://gitlab.com/finosfoundation/legend/reg-innovation/esg-reg-reporting) - A FINOS project to enable banks to consume 3rd party ESG data for the purposes of EU regulatory reporting.
- [open-climate-investing](https://github.com/opentaps/open-climate-investing) - Application and data for analyzing and structuring portfolios for climate investing.
- [climate-finance](https://github.com/ONEcampaign/climate-finance-package) - climate-finance is the python package to get, clean, and work with international public climate finance.

## Carbon Footprint (EEIO or LCA models)

Frameworks (via EEIO or LCA Models) that are indirectly supporting climate finance through input-output analysis of economic systems

- [pymrio](https://github.com/konstantinstadler/pymrio) - Multi-Regional Input-Output Analysis in Python.
- [PyIO](https://real.illinois.edu/pyio/) - Python Module for Input-Output Analysis.
- [iopy](https://github.com/WWakker/iopy) - Input-output data with Python.
- [pyLCAIO](https://github.com/MaximeAgez/pylcaio) - A Python class to hybridize lifecycle assessment (LCA) and environmentally extended input-output (EEIO) databases.
- [Scafandre](https://github.com/hubblo-org/scaphandre) - Energy consumption metrology agent.
- [cie-useeio-extensions](https://github.com/peterberr/cie-useeio-extensions) - A repository for ongoing work at Yale Center for Industrial Ecology with collaborators to make extensions to USEEIO
- [Cloud Carbon Footprint](https://github.com/cloud-carbon-footprint/cloud-carbon-footprint) - Cloud Carbon Footprint is a tool to estimate energy use (kilowatt-hours) and carbon emissions (metric tons CO2e) from public cloud usage.
- [AWS Sustainability Insights Framework (SIF)](https://github.com/aws-solutions-library-samples/guidance-for-aws-sustainability-insights-framework) - The AWS Sustainability Insights Framework (SIF) offers foundational software components that accelerate the design and implementation of applications to automate carbon footprint tracking.
- [US EEIO](https://github.com/USEPA/useeior) - An R package for building and using USEEIO models.
- [iomb](https://github.com/USEPA/IO-Model-Builder) - Python Input-Output Model Builder.
- [Node Carbon](https://github.com/sumn2u/node-carbon) - A Node Package for Measuring Carbon Footprints.
- [OpenClimate](https://github.com/Open-Earth-Foundation/OpenClimate) - A data utility for tracking climate action.
- [CityCatalyst](https://github.com/Open-Earth-Foundation/CityCatalyst) - Open Source carbon accounting for cities.
- [Leontief](https://github.com/open-risk/leontief) - Leontief is a C++ package to work with economic Input-Output models
- [openLCA](https://github.com/GreenDelta/olca-app) - Source code of openLCA
- [EXIOBASE-energy-accounts](https://github.com/Kajwan/EXIOBASE-energy-accounts) - Improving precision in an open-sourced procedure applicable to any MRIO database
- [OpenIO-Canada](https://github.com/CIRAIG/OpenIO-Canada) - Module to create symmetric Environmentally Extended Input-Output tables for Canada.
- [MARIO](https://github.com/it-is-me-mario/MARIO) - Multifunctional Analysis of Regions through Input-Output

## Biodiversity Finance

- [riskmapjnr](https://github.com/ghislainv/riskmapjnr) - The riskmapjnr Python package can be used to obtain maps of the spatial risk of deforestation and forest degradation

## Circular Economy

Models and Frameworks that indirectly support sustainable finance by helping track material flows and advancing the circular economy.

- [pycirk](https://bitbucket.org/CML-IE/pycirk/src/master/) - A python package to model Circular Economy policy and technological interventions in Environmentally Extended Input-Output Analysis starting from SUTs.
- [ODYM](https://github.com/IndEcol/ODYM) - Open Dynamic Material Systems Model.
- [brightway-lca](https://github.com/brightway-lca/brightway2) - Brightway2 is a framework for advanced life cycle assessment calculations. 
- [open supply chains](https://github.com/supplychainstudies/OpenSupplyChains) - Open source codebase behind Sourcemap that allows anyone to visualize and analyze supply chains.
- [PV ICE](https://github.com/NREL/PV_ICE) - An open-source tool to quantify Solar Photovoltaics (PV) Energy and Mass Flows in the Circular Economy, from a Reliability and Lifetime approach.
- [Circular Economy Lifecycle Assessment and VIsualization (CELAVI) framework ](https://github.com/NREL/celavi) - Codebase for the Circular Economy Lifecycle Assessment and VIsualization (CELAVI) modeling framework.

## Integrated Assessment Models

Integrated economic models (for macroeconomic scenarios) 

- [mimi](https://github.com/mimiframework/Mimi.jl) - Mimi is a Julia package that provides a component model for integrated assessment models.
- [MessageIX](https://github.com/iiasa/message_ix) - MESSAGEix is a versatile, dynamic, model framework for energy-engineering-economy-environment (E4) systems research.
- [aneris](https://github.com/iiasa/aneris) - Harmonization of Emissions Trajectories for Integrated Assessment Models.
- [premise](https://github.com/polca/premise) - PRospective EnvironMental Impact AsSEssment. Coupling the ecoinvent database with projections from Integrated Assessment Models (IAM).
- [DICE](https://github.com/psztorc/DICE) - Dynamic Integrated Climate-Economy Model of the Economics of Global Warming.
- [DICE++](https://github.com/swillner/dicepp) - C++-Implementation of the DICE Dynamic Integrated Climate-Economy Model of the Economics of Global Warming.
- [python-DICE](https://github.com/Shivamshaiv/Python-DICE) - Python 3.6 implementation of Dynamic Integrated Climate-Economy (DICE).
- [WITCH](https://github.com/witch-team/witchmodel) - World Induced Technical Change Hybrid model.
- [pyam](https://github.com/IAMconsortium/pyam) - Analysis & visualization of integrated-assessment and macro-energy scenarios.
- [nomenclature](https://github.com/IAMconsortium/nomenclature) - Working with IAMC-format project definitions.
- [IAMC Tools](https://github.com/IAMconsortium/iamc) - A collection of R tools for data analysis and diagnostics.
- [WorldDynamics.jl](https://github.com/worlddynamics/WorldDynamics.jl) - An open-source framework written in Julia for global integrated assessment models.
- [META](https://github.com/openmodels/META-2021) - The Model for Economic Tipping (point) Analysis 

## Social Finance

MicroFinance Frameworks and tools that support the social pillar of ESG, e.g. through financial inclusion and literacy tools and infrastructure

### Financial Inclusion

#### Mifos

- [Fineract](https://github.com/apache/fineract/) - Apache Fineract: A Platform for Microfinance.
- [mojaloop](https://github.com/mojaloop) - Open source software for creating payment platforms that will help unbanked people access digital financial services.

#### Interledger

- [rafiki](https://github.com/interledger/rafiki) - An open-source, comprehensive Interledger service for wallet providers, enabling them to provide Interledger functionality to their users. 
- [web-monetization](https://github.com/interledger/web-monetization-extension) - An open-source browser extension that enables Web Monetization.
- [interledger-rs](https://github.com/interledger/interledger-rs) - An easy-to-use, high-performance Interledger implementation written in Rust 
  
#### Other

- [Tazama](https://github.com/frmscoe/) - Open Source Real-Time Transaction Monitoring Software for Fraud and Money Laundering Detection.
- [tigerbeetle](https://github.com/tigerbeetle/tigerbeetle) - The distributed financial transactions database designed for mission critical safety and performance.
- [micro-finance](https://github.com/MicroPyramid/micro-finance) - Free Micro Finance Software.

### Social Vulnerability

- [SVInsight](https://github.com/mdp0023/SVInsight) - A python package for calculating an exploratory social vulnerability index (SVI). 

### Financial Literacy

- PLACEHOLDER

# Open Data

This section collects open data sources (API endpoints) with data relevant directly or indirectly for sustainable finance workflows

## GHG Emissions

- [EDGAR](https://edgar.jrc.ec.europa.eu/emissions_data_and_maps) - European Commission Emissions Database for Global Atmospheric Research
- [European Environment Agency](https://data.europa.eu/data/datasets/dat-2-en?locale=en) - EU Member States' greenhouse gas (GHG) emission projections
- [GHG Data](https://github.com/sphericalpm/ghgdata) - Greenhouse gas emissions data packaged for easy exploration and charting
- [EFDB](https://www.ipcc-nggip.iges.or.jp/EFDB/downloads.php) - IPCC Emission Factor Database (offline versions for MS,Apple,Linux)
- [bonsai_ipcc](https://gitlab.com/bonsamurais/bonsai/util/ipcc) - The bonsai_ipcc python package enables users to calculate national greenhouse gas (GHG) inventories based on the guidelines provided by the International Panel on Climate Change
- [openGHG](https://github.com/openghg/openghg) - A cloud platform for greenhouse gas (GHG) data analysis and collaboration.
- [FaIR](https://github.com/OMS-NetZero/FAIR) - FaIR (the Finite-amplitude Impulse-Response) climate model is a simple climate model, or emulator, useful for producing global mean temperature projections from a wide range of emissions or prescribed forcing scenarios
- [climate_categories](https://github.com/pik-primap/climate_categories) - Commonly used codes, categories, terminologies, and nomenclatures used in climate policy analysis in a nice Python package. 
  
## Energy System

- [GEM](https://www.gem.wiki/Main_Page) - GEM Wiki, the shared resource on all things energy: fossil fuels, renewable energy sources, environmental impacts, and the global movement to transition to a clean energy system
- [electricityMap](https://github.com/electricitymap/electricitymap-contrib) - A real-time visualisation of the CO2 emissions of electricity consumption
  - [electricityMap Data Sources](https://github.com/electricitymap/electricitymap-contrib/blob/master/DATA_SOURCES.md)
- [ETHOS.FINE](https://github.com/FZJ-IEK3-VSA/FINE) - Framework for Integrated Energy System Assessment
- [gridemissions](https://github.com/jdechalendar/gridemissions) - The tools in this repository power the visualization at energy.stanford.edu/gridemissions
- [Energy Access Explorer](https://github.com/energyaccessexplorer) - Online and interactive geospatial platform that enables energy planners, clean energy entrepreneurs, donors, and development institutions to identify high-priority areas for energy access interventions.
- [Energy Systems and Energy Economics](https://gitlab.ruhr-uni-bochum.de/ee) - Ruhr-Universität Bochum (RUB) GitLab repository cd2es Cordex tools
  
## Other Sustainability Data

- [SDG Data Repository (UK)](https://github.com/ONSdigital/sdg-data) - Data repository for SDGs

# Related Domains

Other awesome lists / resources that are more indirectly relevant for sustainable finance

- [Open Sustainable Technology](https://github.com/protontypes/open-sustainable-technology#carbon-intensity-and-accounting) - A curated list of open technology projects to sustain a stable climate, energy supply, and natural resources
- [Industrial Ecology Dashboard](https://github.com/IndEcol/Dashboard) - A collection of open source projects relevant for industrial ecology practitioners, hosted on GitHub and beyond
- [Climate Modeling](https://github.com/brian-rose/climlab) - Python package for process-oriented climate modeling
- [NTNU Course](https://github.com/iiasa/ntnu_iam_2022) - NTNU Integrated Assessment Modelling Course (2022)
- [climate econometrics](https://github.com/atrisovic/weather-panel.github.io/) - This is a repository for a practical guide to climate econometrics available at climateestimate.net
- [Open Climate](https://github.com/Open-Earth-Foundation/OpenClimate) - Independent Climate Accounting Network in support of Paris Agreement goals
- [Awesome Fintech](https://github.com/moov-io/awesome-fintech) - A curated collection of open source fintech libraries and resources.
