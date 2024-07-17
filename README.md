# Coffee-Cartel
 <!-- -- .--..--..--..--..--..--..--..--..--..--..--..--..--. 
/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \
\ \/\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ \/ /
 \/ /`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'\/ / 
 / /\      ____  ___   _____  _____  _____  _____        / /\ 
/ /\ \    / ___|/ _ \ |  ___||  ___|| ____|| ____|      / /\ \
\ \/ /   | |   | | | || |_   | |_   |  _|  |  _|        \ \/ /
 \/ /    | |___| |_| ||  _|  |  _|  | |___ | |___        \/ / 
 / /\     \____|\___/ |_|    |_|    |_____||_____|       / /\ 
/ /\ \                                                  / /\ \
\ \/ /     ____     _     ____  _____  _____  _         \ \/ /
 \/ /     / ___|   / \   |  _ \|_   _|| ____|| |         \/ / 
 / /\    | |      / _ \  | |_) | | |  |  _|  | |         / /\ 
/ /\ \   | |___  / ___ \ |  _ <  | |  | |___ | |___     / /\ \
\ \/ /    \____|/_/   \_\|_| \_\ |_|  |_____||_____|    \ \/ /
 \/ /                                                    \/ / 
 / /\.--..--..--..--..--..--..--..--..--..--..--..--..--./ /\ 
/ /\ \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \/\ \
\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`-->

Team members: --> RAHEEM, PATRYK, ADEEL, ABDULGANI, PATRICK.

For: Super Coffee chain

Who: needs to analyze and visualize data (digital transformation)

The: Coffee Cartel

Is a: Digital Data transformation app

That: Stores and organizes companies sales info, standardizes transaction details and produces insightful reports and visualizations to facilitate data-driven decision-making for each branch.

Unlike: our competitors who merely provide raw data, we offer an intuitive, sustainable digital platform. Our competitively priced subscription model ensures adaptability to your company's evolving needs.

Our Product:  offers an intuitive, sustainable digital solution. It automatically cleans sensitive information, normalizes transaction details, and generates insightful reports and visualizations to support data-driven decision-making. Our well-priced subscription model, combined with the app's adaptability to your company's evolving needs, sets us apart in the market.


TRELLO --> https://trello.com/b/pNceXhOG/coffee-cartel

Setup Instructions 
git clone https://github.com/generation-de-nat1/Coffee-Cartel.git

change to the directory of the repository

docker compose up -d

create virtual environment in the same directory

python -m venv venv

activate virtual environment venv\Scripts\activate

create .env file with these parameters:
postgres_host = localhost
postgres_user = ######
postgres_pass = ######
postgres_port = ######
adminer_port =  ######

inside virtual environment
pip install -r requirements.txt

Use http://localhost:{adminer_port} to access adminer and use credentials chosen in .env file

NOTE : select PostgreSQL for system on adminer

Run the App

Compress-Archive -Path * -DestinationPath coffee-cartel-2_2.zip