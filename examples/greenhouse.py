# Greenhouse log analyser — the guide's worked example.
# A week of invented temperature readings (degrees C), three per day,
# plus the soil-moisture percentage noted at each evening reading.
# The gardener's rule: water in the evening when the day's average
# temperature passed 24 degrees OR the soil moisture fell below 30%.

readings = [
    # (day, morning, midday, evening, soil_moisture_pct)
    ("Mon", 17.0, 24.0, 21.5, 41),
    ("Tue", 18.5, 26.5, 23.0, 36),
    ("Wed", 19.0, 28.0, 24.5, 29),
    ("Thu", 18.0, 25.5, 22.0, 33),
    ("Fri", 16.5, 23.5, 20.5, 38),
    ("Sat", 19.5, 29.0, 25.0, 27),
    ("Sun", 18.0, 26.0, 22.5, 31),
]

HOT_DAY = 24.0
DRY_SOIL = 30


def day_average(row):
    return (row[1] + row[2] + row[3]) / 3


def needs_water(row):
    return day_average(row) > HOT_DAY or row[4] < DRY_SOIL


print("Day  Average  Water?")
water_days = 0
for row in readings:
    avg = day_average(row)
    water = needs_water(row)
    if water:
        water_days += 1
    print("{}  {:6.2f}   {}".format(row[0], avg, "YES" if water else "no"))

all_temps = [t for row in readings for t in row[1:4]]
print()
print("Week's coolest reading: {:.1f}".format(min(all_temps)))
print("Week's warmest reading: {:.1f}".format(max(all_temps)))
print("Week's average:         {:.2f}".format(sum(all_temps) / len(all_temps)))
print("Evenings to water:      {}".format(water_days))
