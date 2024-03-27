"""
Environment: Python 3.11
Requirements: numpy, simpy, pandas

"""
import random
import simpy
import duckdb
import pandas as pd
import numpy as np

from collections import defaultdict

random.seed(123456)
np.random.seed(123456)

global PASSENGER_TRACKER
DUCKCONN = duckdb.connect('temp_db')

def setup_db():
    DUCKCONN.execute(
        """
        CREATE TABLE IF NOT EXISTS simulation_results (
        passenger_arrival INT,
        number_of_servers INT,
        number_of_scanners INT,
        simulation_duration INT,
        total_passengers INT,
        percentage_passengers_cleared FLOAT,
        min_time FLOAT,
        max_time FLOAT,
        mean_time FLOAT,
        median_time FLOAT,
        minmax_diff_time FLOAT,
        iteration_1 FLOAT,
        iteration_2 FLOAT,
        iteration_3 FLOAT,
        iteration_4 FLOAT,
        iteration_5 FLOAT,
        iteration_6 FLOAT,
        iteration_7 FLOAT,
        iteration_8 FLOAT,
        iteration_9 FLOAT,
        iteration_10 FLOAT
        );
        """
    )

    # DUCKCONN.execute("DROP TABLE simulation_results")
    result = DUCKCONN.execute("SELECT * FROM simulation_results")
    print(result.fetchall())

class AirportSecurity:
    def __init__(self, env: simpy.Environment, num_servers: int, server_response_time,
                 num_queue: int, queue_response_time:dict):

        self.env = env

        self.server = simpy.Resource(env, num_servers)
        self.server_time = server_response_time

        self.scan_queue = simpy.Resource(env, num_queue)
        self.queue_time = queue_response_time

    def boarding(self, passenger_id: int):
        ts_boarding = np.random.exponential(self.server_time)
        yield self.env.timeout(ts_boarding)
        #print(f"[{passenger_id}] Cleared Boarding in {ts_boarding}")

    def scanner(self, passenger_id: int):
        ts_scanning = np.random.uniform(**self.queue_time)
        yield self.env.timeout(ts_scanning)
        #print(f"[{passenger_id}] Cleared Scanner in {ts_scanning}")



def passenger(passenger_id, env: simpy.Environment, airport_security: AirportSecurity):

    #print(f"[{passenger_id}] Entered {env.now}")
    start_time = env.now
    PASSENGER_TRACKER[passenger_id] = {"start_time": start_time}

    with airport_security.server.request() as request:
        t_s = env.now
        yield request
        yield env.process(airport_security.boarding(passenger_id))
        PASSENGER_TRACKER[passenger_id]["server"] = env.now - t_s

    with airport_security.scan_queue.request() as request:
        t_s = env.now
        yield request
        yield env.process(airport_security.scanner(passenger_id))
        PASSENGER_TRACKER[passenger_id]["scanner"] = env.now - t_s

    PASSENGER_TRACKER[passenger_id]["end_time"] = env.now
    PASSENGER_TRACKER[passenger_id]["total_duration"] = (PASSENGER_TRACKER[passenger_id]["end_time"] -
                                                         PASSENGER_TRACKER[passenger_id]["start_time"])
    #print(f"[{passenger_id}] Done {env.now}")

def simulate(env: simpy.Environment, num_servers, server_response_time,
             num_queue, queue_response_time,
             passenger_arrival, passenger_interval):

    sg_airport_security = AirportSecurity(env, num_servers, server_response_time, num_queue, queue_response_time)

    passenger_id = 1
    while True:
        passenger_arrival_interval = np.random.exponential(1/passenger_interval)
        yield env.timeout(passenger_arrival_interval)

        passengers_arrived = np.random.poisson(passenger_arrival)
        for _ in range(passengers_arrived):
            env.process(passenger(passenger_id, env , sg_airport_security))
            passenger_id += 1

def generate_results():
    df = pd.read_sql_query("SELECT * FROM simulation_results", DUCKCONN)
    df.to_csv("simulation_results.csv", index=False, mode="w", header=True)
    print("Data exported to 'simulation_results.csv'")

setup_db()
for l1, s1, q1 in [(50, x2, x3) for x2 in range(1, 25) for x3 in range(1, 25)]:

    results = []
    percentage_valid = []
    passenger_count = []

    # Runtime
    SIMULATION_DURATION = 60  # 1 unit (Minute), 60 unit = 1 Hour, 720 unit = 12 hour

    # Passenger Arrival
    LAMBDA_ONE = l1 #50
    LAMBDA_EXP_ONE = 0.2  # Minute

    # SERVER
    NUMBER_OF_SERVERS = s1 #12  # 9 for 720 time unit
    LAMBDA_EXP_TWO = 0.75  # Minute

    # PERSONAL SCANNER
    NUMBER_OF_CHECK_QUEUE = q1 #15  # 12 for 720 time unit
    TIME_DISTRIBUTION = {"low": 0.5, "high": 1}  # Minute
    iterations = 10

    for simulation_iteration in range(iterations):
        env = simpy.Environment()
        run_config = {
            "passenger_arrival": LAMBDA_ONE,
            "passenger_interval": LAMBDA_EXP_ONE,
            "num_servers": NUMBER_OF_SERVERS,
            "server_response_time": LAMBDA_EXP_TWO,
            "num_queue": NUMBER_OF_CHECK_QUEUE,
            "queue_response_time": TIME_DISTRIBUTION,
        }

        PASSENGER_TRACKER = defaultdict(dict)
        env.process(simulate(env, **run_config))
        env.run(until=SIMULATION_DURATION)

        total_wait_time = sum([ _.get("total_duration", 0) for _ in PASSENGER_TRACKER.values()])
        total_valid = sum([1 if _.get("total_duration") else 0 for _ in PASSENGER_TRACKER.values()])

        print(f"ITER {simulation_iteration}: AVERAGE DURATION TAKEN = {total_wait_time/total_valid}, {total_valid = }, {total_valid/len(PASSENGER_TRACKER)}")
        results.append(total_wait_time/total_valid)
        percentage_valid.append(total_valid/len(PASSENGER_TRACKER))
        passenger_count.append(len(PASSENGER_TRACKER))

    print(f"""
    TOTAL ITERATIONS RAN : {iterations}
    
    {results = }
    {passenger_count = }
    {percentage_valid = }
    {np.mean(percentage_valid) = }
    {round(np.mean(passenger_count),0) = }
    Minimum Time: {min(results)}
    Mean Time: {np.mean(results)}
    Median Time: {np.median(results)}
    Maximum Time: {max(results)}
    MinMaxSpread: {max(results) - min(results)}
    10 Percentile: {np.quantile(results, 0.1)}
    90 Percentile: {np.quantile(results, 0.9)}
    IQR: {np.quantile(results, 0.9) - np.quantile(results, 0.1)}
    """)

    DUCKCONN.execute(f"""
        INSERT INTO simulation_results VALUES (
        {LAMBDA_ONE},
        {NUMBER_OF_SERVERS},
        {NUMBER_OF_CHECK_QUEUE},
        {SIMULATION_DURATION},
        {round(np.mean(passenger_count),0)},
        {np.mean(percentage_valid)},
        {min(results)},
        {max(results)},
        {np.mean(results)},
        {np.median(results)},
        {max(results) - min(results)},
        {results[0]},
        {results[1]},
        {results[2]},
        {results[3]},
        {results[4]},
        {results[5]},
        {results[6]},
        {results[7]},
        {results[8]},
        {results[9]}
        )
        """)


generate_results()