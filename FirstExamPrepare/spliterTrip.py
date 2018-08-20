travel = float(input())
fuel_tank = float(input())
heavy_wind = float(input())

non_heavy = travel - heavy_wind
non_heavy_cunsum = non_heavy * 25
heavy_cunsum = heavy_wind * 25 * 3 / 2
fuel_cunsum = non_heavy_cunsum + heavy_cunsum
tolerance = fuel_cunsum * 5 / 100
total_fuel_cunsum = fuel_cunsum + tolerance
remaining_fuel = fuel_tank - total_fuel_cunsum

print('Fuel needed: {0:.2f}L'.format(total_fuel_cunsum))
if remaining_fuel >= 0.0:
    print('Enough with {0:.2f}L to spare!'.format(remaining_fuel))
else:
    print('We need {0:.2f}L more fuel.'.format(-remaining_fuel))