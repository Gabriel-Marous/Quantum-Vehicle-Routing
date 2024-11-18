

![title](images/qvrp_logo4.png)

## Motivation
This project is part of an initiative by Open Quantum Institute to leverage quantum computing for the UN sustainable development goals. In this project, we aim to develop methods to more efficiently route food from producers to consumers. By doing so, we hope to reduce waste and emmisions while providing versatile tools to connect small farmers to the global supply chain. Read our preliminary report and why we believe that quantum computing in the [OQI 2024 Sustainable Development Goal Use Cases Whitepaper](https://lnkd.in/dGjVEHHt)!

## Getting Started

### Create a Virtual Environment

It is highly recommended that you create a virtual environment for the dependencies of this project, and conda is recommended for this (this requires that you install anaconda first).

To create an environment with all the dependencies for this project, run

```bash
conda create --name dwave_env --file requirements.txt
```

Then activate this environment with

```bash
conda activate dwave_env
```

### Get an Access Token for DWave

You will need a token to run code on DWave hardware which is not included in this repository since the repository is public and I don't want strangers using my limited compute time. To do so, first [create a DWave account](https://www.dwavesys.com/solutions-and-products/ocean/). After your account is created, you will get a token which is on the left pannel of the account screen (you may need to scroll down). This page will also show you how many hours you have left for the month on the annealer. Once you get a token, create a file ```credentials.py``` and create a variable ```TOKEN``` and set it equal to your token string. The ```.gitignore``` file is configured to ignore the ```credentials.py``` file when you publish any code to the public GitHub, so your token will be safe. 

## File Overview
* ```vrp.py``` outlines the implementations of the objective functions and constraints for various QUBO representations of the Vehicle Routing Problem
* ```vrp_test.ipynb``` demonstrates these implementations (partially complete) on various sample routing problems

## Other Notes
Running any file that calls on the dwave annealer will use up some of your compute time for the month (likely ~0.5%). There is no need to be stingy, but take advantage of how a markdown saves the states of variables to avoid rerunning simulations if you do not have to.