# Battery Backup Time Calculator

print("===== Battery Backup Time Calculator =====")

voltage = float(input("Enter battery voltage (V): "))
capacity = float(input("Enter battery capacity (Ah): "))
load = float(input("Enter load power (W): "))
efficiency = float(input("Enter system efficiency (%): "))

backup_time = (voltage * capacity * (efficiency / 100)) / load

print("\nBattery Backup Time =", round(backup_time, 2), "hours")

# Convert hours into minutes
backup_minutes = backup_time * 60
print("Battery Backup Time =", round(backup_minutes, 2), "minutes")