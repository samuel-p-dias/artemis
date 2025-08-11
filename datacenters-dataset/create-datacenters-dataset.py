import csv
import random

datacenters = ["Datacenter1", "Datacenter2", "Datacenter3", "Datacenter4", 
                 "Datacenter5", "Datacenter6", "Datacenter7", "Datacenter8",
                 "Datacenter9", "Datacenter10"]

devices = random.randint(800_000, 1_500_000)  # number of devices per datacenter
months = range(1, 13)

# Filename for the CSV output
csv_filename = "datacenter_energy_demand.csv"

# Create and write to the CSV file
with open(csv_filename, mode="w", newline="") as file:
   writer = csv.writer(file)
   writer.writerow(["Datacenter ID", "Devices", "Month", "Air conditioning", "mWh total", "Order Size"])

   for datacenter_id in datacenters:
      for month in months:

         # Define the air conditioning factor based on the month
         if month in [9, 10, 11, 12, 1, 2, 3]:  # warmer months
               air_conditioning = round(random.uniform(0.43, 0.50), 2)
         else:  # cooler months
               air_conditioning = round(random.uniform(0.32, 0.40), 2)

         # Calculate the total energy demand in MWh and the order size
         mwh_total = round(devices * random.uniform(0.2, 0.4), 5)
         order = round(mwh_total * (1 + air_conditioning + 0.10))

         # Write the data to the CSV file
         writer.writerow([
               datacenter_id,
               devices,
               month,
               air_conditioning,
               mwh_total,
               order
         ])

print(f"CSV file '{csv_filename}' created successfully with energy demand data for datacenters.")
