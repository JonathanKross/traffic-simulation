
# Road Rage
## A Traffic Simulation to Finding the Ideal Speed Limit

### Project Description
We have a 1 kilometer section of road being built and do not know what the speed limit should be. This notebook simulates the 1 kilometer of road.

### Project Assumptions
* Drivers want to go up to the assigned speed limit, initially set at 120 km/hr (33.33 m/s).
* The average car is 5 meters long.
* Drivers want at least a number of meters equal to their speed in meters/second between them and the next car.
* Drivers will accelerate 2 m/s up to their desired speed as long as they have room to do so.
* If another car is too close, drivers will match that car's speed until they have room again.
* If a driver would hit another car by continuing, they stop (i.e., potentially trigger a traffic jam).
* Drivers will randomly (10% chance each second) slow by 2 m/s.
* This section of road is one lane going one way.
* Drivers enter the road at the speed they left.
* Simulation starts with 30 cars per kilometer, evenly spaced.
* Even though this road is not circular, treat it as such in order to generate a continuous flow of traffic.

### To View This Notebook
Just click on the `road-rage.ipynb` file above.

### To Run This Notebook
#### System Requirements / Installation

* You will need to have **python3** installed on your machine.

* Clone this repo.

* Create a virtual environment in your working directory.

* Within the working directory, install the requirements file by running the following command-line prompt: **`pip install -r requirements.txt`**.

#### Opening the Notebook
* Using a command-line program, navigate to the folder containing the downloaded file and run the following line: **`ipython notebook road-rage.ipynb`**
