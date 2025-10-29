import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from datetime import datetime, timedelta
import random
import threading
import queue
import os
import matplotlib
# Use a non-interactive backend
matplotlib.use('Agg')

# Simulated IoT traffic data class
class TrafficIoTSimulator:
    def __init__(self, intersection_count=4):
        self.intersection_count = intersection_count
        self.intersections = {}

        # Initialize intersections with random traffic conditions
        for i in range(1, intersection_count + 1):
            self.intersections[f"Intersection-{i}"] = {
                "vehicle_count": random.randint(5, 30),
                "average_speed": random.randint(15, 55),
                "congestion_level": random.choice(["Low", "Medium", "High"]),
                "wait_time": random.randint(10, 120),
                "pedestrians": random.randint(0, 15),
                "emergency_vehicle": random.random() < 0.05
            }

        # Traffic light status for each intersection (N, E, S, W)
        self.traffic_lights = {}
        for i in range(1, intersection_count + 1):
            # Initialize with random light status
            self.traffic_lights[f"Intersection-{i}"] = {
                "North": random.choice(["Red", "Green", "Yellow"]),
                "East": random.choice(["Red", "Green", "Yellow"]),
                "South": random.choice(["Red", "Green", "Yellow"]),
                "West": random.choice(["Red", "Green", "Yellow"])
            }

        # Historical data for analysis
        self.history = {
            "timestamp": [],
            "intersection": [],
            "vehicle_count": [],
            "average_speed": [],
            "congestion_level": [],
            "wait_time": []
        }

    def update_traffic_data(self):
        """Simulate IoT sensor data updates"""
        for intersection in self.intersections:
            # Update with realistic variations
            self.intersections[intersection]["vehicle_count"] = max(0,
                self.intersections[intersection]["vehicle_count"] + random.randint(-5, 5))

            self.intersections[intersection]["average_speed"] = max(5, min(60,
                self.intersections[intersection]["average_speed"] + random.randint(-8, 8)))

            # Update congestion level based on vehicle count and speed
            if self.intersections[intersection]["vehicle_count"] > 25 or self.intersections[intersection]["average_speed"] < 20:
                self.intersections[intersection]["congestion_level"] = "High"
            elif self.intersections[intersection]["vehicle_count"] > 15 or self.intersections[intersection]["average_speed"] < 35:
                self.intersections[intersection]["congestion_level"] = "Medium"
            else:
                self.intersections[intersection]["congestion_level"] = "Low"

            # Update wait time based on congestion
            if self.intersections[intersection]["congestion_level"] == "High":
                self.intersections[intersection]["wait_time"] = random.randint(60, 180)
            elif self.intersections[intersection]["congestion_level"] == "Medium":
                self.intersections[intersection]["wait_time"] = random.randint(30, 90)
            else:
                self.intersections[intersection]["wait_time"] = random.randint(5, 40)

            self.intersections[intersection]["pedestrians"] = max(0,
                self.intersections[intersection]["pedestrians"] + random.randint(-3, 3))

            # Small chance for emergency vehicle
            self.intersections[intersection]["emergency_vehicle"] = random.random() < 0.05

            # Record history
            self.history["timestamp"].append(datetime.now())
            self.history["intersection"].append(intersection)
            self.history["vehicle_count"].append(self.intersections[intersection]["vehicle_count"])
            self.history["average_speed"].append(self.intersections[intersection]["average_speed"])
            self.history["congestion_level"].append(self.intersections[intersection]["congestion_level"])
            self.history["wait_time"].append(self.intersections[intersection]["wait_time"])

    def update_traffic_lights(self):
        """Update traffic light states based on traffic conditions"""
        for intersection in self.intersections:
            # Determine which direction has highest priority
            directions = ["North", "East", "South", "West"]

            # If there's an emergency vehicle, prioritize its direction
            if self.intersections[intersection]["emergency_vehicle"]:
                # Simulate emergency vehicle coming from a random direction
                priority_direction = random.choice(directions)

                # Set that direction to green, others to red
                for direction in directions:
                    if direction == priority_direction:
                        self.traffic_lights[intersection][direction] = "Green"
                    else:
                        self.traffic_lights[intersection][direction] = "Red"
            else:
                # Normal traffic management logic
                # For simplicity, cycle through directions
                green_index = -1

                for i, direction in enumerate(directions):
                    if self.traffic_lights[intersection][direction] == "Green":
                        green_index = i
                        self.traffic_lights[intersection][direction] = "Yellow"
                    elif self.traffic_lights[intersection][direction] == "Yellow":
                        self.traffic_lights[intersection][direction] = "Red"

                # Move green to next direction
                next_green = (green_index + 1) % len(directions)
                self.traffic_lights[intersection][directions[next_green]] = "Green"

    def get_current_data(self):
        """Return current traffic data as a DataFrame"""
        data = []
        for intersection in self.intersections:
            row = {
                "Intersection": intersection,
                "Vehicles": self.intersections[intersection]["vehicle_count"],
                "Avg Speed (km/h)": self.intersections[intersection]["average_speed"],
                "Congestion": self.intersections[intersection]["congestion_level"],
                "Wait Time (s)": self.intersections[intersection]["wait_time"],
                "Pedestrians": self.intersections[intersection]["pedestrians"],
                "Emergency": "YES" if self.intersections[intersection]["emergency_vehicle"] else "NO"
            }
            data.append(row)
        return pd.DataFrame(data)

    def get_traffic_light_status(self):
        """Return current traffic light status"""
        data = []
        for intersection in self.traffic_lights:
            row = {
                "Intersection": intersection,
                "North": self.traffic_lights[intersection]["North"],
                "East": self.traffic_lights[intersection]["East"],
                "South": self.traffic_lights[intersection]["South"],
                "West": self.traffic_lights[intersection]["West"]
            }
            data.append(row)
        return pd.DataFrame(data)

    def get_historical_data(self, minutes=30):
        """Get historical data for the last specified minutes"""
        if not self.history["timestamp"]:
            return pd.DataFrame()

        cutoff = datetime.now() - timedelta(minutes=minutes)
        df = pd.DataFrame(self.history)
        return df[df["timestamp"] >= cutoff]

# Headless Smart Traffic Management System
class HeadlessTrafficManagementSystem:
    def __init__(self, simulator):
        self.simulator = simulator
        self.data_queue = queue.Queue()
        self.running = False
        self.output_dir = "traffic_data_output"

        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def start(self):
        """Start the traffic management system"""
        self.running = True

        # Start the simulator in a background thread
        self.simulator_thread = threading.Thread(target=self.run_simulator)
        self.simulator_thread.daemon = True
        self.simulator_thread.start()

        # Start the data processing
        self.process_data()

    def run_simulator(self):
        """Run the traffic simulator in background"""
        while self.running:
            # Update simulator data
            self.simulator.update_traffic_data()
            self.simulator.update_traffic_lights()

            # Put new data in queue for processing
            traffic_data = self.simulator.get_current_data()
            light_data = self.simulator.get_traffic_light_status()
            self.data_queue.put((traffic_data, light_data))

            # Optimize traffic conditions algorithmically
            self.optimize_traffic()

            time.sleep(1)  # Update every second

    def optimize_traffic(self):
        """Apply AI/ML-based traffic optimization"""
        # In a real system, this would contain advanced algorithms
        # For simulation, we'll implement a basic optimization logic

        for intersection in self.simulator.intersections:
            # Check for severe congestion and adjust traffic patterns
            if self.simulator.intersections[intersection]["congestion_level"] == "High":
                # Simulate notifying nearby intersections to prepare for increased flow
                # In reality, this would adjust light timing and lane direction
                pass

            # Handle emergency vehicles with priority routing
            if self.simulator.intersections[intersection]["emergency_vehicle"]:
                # Priority light sequencing already handled in simulator
                pass

    def process_data(self):
        """Process traffic data and generate reports/visualizations"""
        iteration = 0

        try:
            while self.running and iteration < 30:  # Run for 30 iterations
                if not self.data_queue.empty():
                    traffic_data, light_data = self.data_queue.get_nowait()

                    # Print current traffic conditions
                    print(f"\n--- Traffic Condition Report #{iteration+1} ---")
                    print(traffic_data[["Intersection", "Vehicles", "Avg Speed (km/h)", "Congestion", "Wait Time (s)"]])

                    # Print traffic light status
                    print("\n--- Traffic Light Status ---")
                    print(light_data)

                    # Generate visualization if we have enough historical data
                    if iteration % 5 == 0:  # Every 5 iterations
                        self.generate_reports(iteration)

                    iteration += 1

                time.sleep(1)

            # Generate final report
            self.generate_final_report()
            print("\nTraffic simulation completed. Reports generated in the 'traffic_data_output' directory.")

        except KeyboardInterrupt:
            print("\nTraffic management system stopped by user.")
            self.running = False

    def generate_reports(self, iteration):
        """Generate traffic reports and visualizations"""
        historical_data = self.simulator.get_historical_data(minutes=30)

        if historical_data.empty:
            return

        # Create visualization with multiple subplots
        fig = plt.figure(figsize=(15, 10))
        fig.suptitle(f"Traffic Management Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", fontsize=16)

        # 1. Traffic volume plot
        ax1 = fig.add_subplot(2, 2, 1)
        for intersection in self.simulator.intersections:
            intersection_data = historical_data[historical_data["intersection"] == intersection]
            ax1.plot(intersection_data["timestamp"], intersection_data["vehicle_count"], label=intersection)

        ax1.set_title("Traffic Volume Over Time")
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Vehicle Count")
        ax1.legend(loc="best")

        # 2. Average speed plot
        ax2 = fig.add_subplot(2, 2, 2)
        for intersection in self.simulator.intersections:
            intersection_data = historical_data[historical_data["intersection"] == intersection]
            ax2.plot(intersection_data["timestamp"], intersection_data["average_speed"], label=intersection)

        ax2.set_title("Average Speed Over Time")
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Speed (km/h)")
        ax2.legend(loc="best")

        # 3. Congestion distribution
        ax3 = fig.add_subplot(2, 2, 3)
        congestion_counts = historical_data["congestion_level"].value_counts()
        ax3.pie(congestion_counts, labels=congestion_counts.index, autopct='%1.1f%%',
                colors=['green', 'yellow', 'red'])
        ax3.set_title("Congestion Level Distribution")

        # 4. Wait time by intersection
        ax4 = fig.add_subplot(2, 2, 4)
        avg_wait_time = historical_data.groupby("intersection")["wait_time"].mean()
        ax4.bar(avg_wait_time.index, avg_wait_time.values)
        ax4.set_title("Average Wait Time by Intersection")
        ax4.set_ylabel("Wait Time (seconds)")
        ax4.tick_params(axis='x', rotation=45)

        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/traffic_report_{iteration}.png")
        plt.close(fig)

        # Save data to CSV
        traffic_data = self.simulator.get_current_data()
        traffic_data.to_csv(f"{self.output_dir}/traffic_data_{iteration}.csv", index=False)

        # Generate a text report
        with open(f"{self.output_dir}/report_{iteration}.txt", "w") as f:
            f.write(f"TRAFFIC MANAGEMENT SYSTEM REPORT\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

            f.write("CURRENT TRAFFIC CONDITIONS\n")
            f.write("=========================\n")
            f.write(traffic_data.to_string(index=False))
            f.write("\n\n")

            f.write("TRAFFIC LIGHT STATUS\n")
            f.write("===================\n")
            f.write(self.simulator.get_traffic_light_status().to_string(index=False))
            f.write("\n\n")

            f.write("TRAFFIC ANALYSIS\n")
            f.write("===============\n")

            # Average congestion level
            congestion_map = {"Low": 1, "Medium": 2, "High": 3}
            avg_congestion = historical_data["congestion_level"].map(congestion_map).mean()

            f.write(f"Average Congestion Level: {avg_congestion:.2f}/3.00\n")
            f.write(f"Total Vehicle Count: {historical_data['vehicle_count'].sum()}\n")
            f.write(f"Average Wait Time: {historical_data['wait_time'].mean():.2f} seconds\n")
            f.write(f"Average Speed: {historical_data['average_speed'].mean():.2f} km/h\n")

    def generate_final_report(self):
        """Generate comprehensive final report"""
        historical_data = self.simulator.get_historical_data(minutes=30)

        if historical_data.empty:
            return

        # Create a more detailed final report
        fig = plt.figure(figsize=(15, 15))
        fig.suptitle("SMART TRAFFIC MANAGEMENT SYSTEM - FINAL REPORT", fontsize=16)

        # 1. Traffic volume heatmap
        ax1 = fig.add_subplot(3, 2, 1)
        # Convert intersection and timestamp to categorical for heatmap
        pivot_data = historical_data.pivot_table(
            index="intersection",
            columns=pd.Grouper(key="timestamp", freq="1min"),
            values="vehicle_count",
            aggfunc="mean"
        ).fillna(0)

        im = ax1.imshow(pivot_data.values, aspect='auto', cmap='YlOrRd')
        ax1.set_title("Traffic Volume Heatmap")
        ax1.set_ylabel("Intersection")
        ax1.set_xlabel("Time")
        ax1.set_yticks(np.arange(len(pivot_data.index)))
        ax1.set_yticklabels(pivot_data.index)
        plt.colorbar(im, ax=ax1, label="Vehicle Count")

        # 2. Congestion level trend
        ax2 = fig.add_subplot(3, 2, 2)
        congestion_map = {"Low": 1, "Medium": 2, "High": 3}

        for intersection in self.simulator.intersections:
            subset = historical_data[historical_data["intersection"] == intersection]
            ax2.plot(subset["timestamp"], subset["congestion_level"].map(congestion_map),
                     label=intersection, marker='o')

        ax2.set_title("Congestion Level Trend")
        ax2.set_ylabel("Congestion Level (1=Low, 2=Medium, 3=High)")
        ax2.set_xlabel("Time")
        ax2.legend(loc="best")

        # 3. Speed vs. Vehicle Count scatter
        ax3 = fig.add_subplot(3, 2, 3)
        for intersection in self.simulator.intersections:
            subset = historical_data[historical_data["intersection"] == intersection]
            ax3.scatter(subset["vehicle_count"], subset["average_speed"],
                       label=intersection, alpha=0.7)

        ax3.set_title("Speed vs. Vehicle Count")
        ax3.set_xlabel("Vehicle Count")
        ax3.set_ylabel("Average Speed (km/h)")
        ax3.legend(loc="best")

        # 4. Wait Time Distribution
        ax4 = fig.add_subplot(3, 2, 4)
        wait_bins = [0, 30, 60, 90, 120, 150, 180]
        ax4.hist(historical_data["wait_time"], bins=wait_bins, alpha=0.7, color='orange')
        ax4.set_title("Wait Time Distribution")
        ax4.set_xlabel("Wait Time (seconds)")
        ax4.set_ylabel("Frequency")

        # 5. Emergency Vehicle Events
        ax5 = fig.add_subplot(3, 2, 5)
        emergency_counts = {}

        for intersection in self.simulator.intersections:
            emergency_counts[intersection] = sum(
                1 for flag in [self.simulator.intersections[intersection]["emergency_vehicle"]
                              for _ in range(len(historical_data))] if flag
            )

        bars = ax5.bar(emergency_counts.keys(), emergency_counts.values(), color='red')
        ax5.set_title("Emergency Vehicle Events by Intersection")
        ax5.set_ylabel("Count")
        ax5.tick_params(axis='x', rotation=45)

        # 6. System Efficiency Metrics
        ax6 = fig.add_subplot(3, 2, 6)

        # Calculate efficiency metrics (lower is better)
        efficiency_metrics = {
            "Avg Wait Time": historical_data["wait_time"].mean(),
            "Congestion Score": historical_data["congestion_level"].map(congestion_map).mean() * 33.33,  # Scale to 0-100
            "Speed Reduction": 100 - (historical_data["average_speed"].mean() / 60 * 100)  # As percentage of max speed
        }

        ax6.bar(efficiency_metrics.keys(), efficiency_metrics.values(), color=['blue', 'orange', 'green'])
        ax6.set_title("System Efficiency Metrics (Lower is Better)")
        ax6.set_ylabel("Score")
        ax6.set_ylim(0, 100)

        for i, v in enumerate(efficiency_metrics.values()):
            ax6.text(i, v + 5, f"{v:.1f}", ha='center')

        plt.tight_layout()
        plt.savefig(f"{self.output_dir}/final_report.png")
        plt.close(fig)

        # Save comprehensive data to CSV
        historical_data.to_csv(f"{self.output_dir}/historical_data_final.csv", index=False)

        # Generate text summary report
        with open(f"{self.output_dir}/final_summary_report.txt", "w") as f:
            f.write("SMART TRAFFIC MANAGEMENT SYSTEM - FINAL SUMMARY\n")
            f.write("=============================================\n\n")

            f.write(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Simulation Duration: {len(historical_data['timestamp'].unique())} seconds\n")
            f.write(f"Intersections Monitored: {len(self.simulator.intersections)}\n\n")

            f.write("TRAFFIC PERFORMANCE METRICS\n")
            f.write("==========================\n")
            f.write(f"Average Vehicle Count per Intersection: {historical_data.groupby('intersection')['vehicle_count'].mean().mean():.2f}\n")
            f.write(f"Average Speed: {historical_data['average_speed'].mean():.2f} km/h\n")
            f.write(f"Average Wait Time: {historical_data['wait_time'].mean():.2f} seconds\n\n")

            congestion_dist = historical_data["congestion_level"].value_counts(normalize=True) * 100
            f.write("CONGESTION DISTRIBUTION\n")
            f.write("======================\n")
            for level, percentage in congestion_dist.items():
                f.write(f"{level}: {percentage:.2f}%\n")

            f.write("\nEMERGENCY VEHICLE RESPONSES\n")
            f.write("==========================\n")
            for intersection, count in emergency_counts.items():
                f.write(f"{intersection}: {count} emergency events\n")

            f.write("\nINTERSECTION PERFORMANCE RANKING\n")
            f.write("==============================\n")

            # Calculate an overall performance score for each intersection
            # Lower score is better (less congestion, higher speed, less wait time)
            intersection_performance = []

            for intersection in self.simulator.intersections:
                subset = historical_data[historical_data["intersection"] == intersection]

                congestion_score = subset["congestion_level"].map(congestion_map).mean()
                speed_score = 60 / subset["average_speed"].mean() if subset["average_speed"].mean() > 0 else float('inf')
                wait_score = subset["wait_time"].mean() / 60  # Normalize by max expected wait time

                # Overall score (lower is better)
                overall_score = (congestion_score + speed_score + wait_score) / 3

                intersection_performance.append({
                    "intersection": intersection,
                    "score": overall_score,
                    "avg_congestion": congestion_score,
                    "avg_speed": subset["average_speed"].mean(),
                    "avg_wait": subset["wait_time"].mean()
                })

            # Sort by score (ascending)
            intersection_performance.sort(key=lambda x: x["score"])

            # Print ranking
            for i, perf in enumerate(intersection_performance):
                f.write(f"{i+1}. {perf['intersection']} - Score: {perf['score']:.2f} ")
                f.write(f"(Avg Congestion: {perf['avg_congestion']:.2f}, ")
                f.write(f"Avg Speed: {perf['avg_speed']:.2f} km/h, ")
                f.write(f"Avg Wait: {perf['avg_wait']:.2f}s)\n")

            f.write("\nSYSTEM RECOMMENDATIONS\n")
            f.write("======================\n")

            # Generate recommendations based on data
            if historical_data["wait_time"].mean() > 60:
                f.write("- Optimize traffic light timing to reduce high average wait times\n")

            high_congestion = historical_data[historical_data["congestion_level"] == "High"]
            if len(high_congestion) > len(historical_data) * 0.3:  # More than 30% high congestion
                f.write("- Implement traffic diversion strategies to reduce overall congestion\n")

            if historical_data["average_speed"].mean() < 30:
                f.write("- Consider speed flow optimization techniques to improve average speeds\n")

            # Find most congested intersection
            int_congestion = historical_data.groupby("intersection")["congestion_level"].apply(
                lambda x: (x == "High").mean())
            most_congested = int_congestion.idxmax()
            if int_congestion.max() > 0.5:  # More than 50% high congestion
                f.write(f"- Focus immediate attention on {most_congested} which shows critical congestion levels\n")

            f.write("- Consider dynamic lane allocation during peak congestion periods\n")
            f.write("- Evaluate emergency response protocols which successfully handled ")
            f.write(f"{sum(emergency_counts.values())} emergency vehicle events\n")


if __name__ == "__main__":
    # Create traffic simulator with 4 intersections
    traffic_simulator = TrafficIoTSimulator(intersection_count=4)

    # Create and start the headless traffic management system
    traffic_system = HeadlessTrafficManagementSystem(traffic_simulator)
    print("Starting Smart Traffic Management System (Headless Mode)...")
    print("Data will be saved to the 'traffic_data_output' directory")
    traffic_system.start()
