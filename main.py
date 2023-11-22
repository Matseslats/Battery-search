batteries = []
best_battery = {
    "name": "N/A",
    "mAh": 0,
    "height": 0,
    "height": 0,
    "length": 0,
    "multiples": 10000000
}

MAX_WIDTH = 30
MAX_HEIGHT = 30
MAX_LENGTH = 14

# Open file
with open("data.csv") as file:
    header = file.readline() # Read header
    for line in file.readlines():
        # Read/parse line
        name, mAh, width, height, length = line.replace('\n', '').split(",")
        mAh = float(mAh)
        width = float(width)
        height = float(height)
        length = float(length)

        if (height > MAX_HEIGHT or width > MAX_WIDTH or length > MAX_LENGTH):
            continue # This battery does not fit, skip it

        # How many batteries can you pack in the tree orientations? Find it and the tot capacity
        multiples_1 = (MAX_HEIGHT // height) * (MAX_WIDTH // width) * (MAX_LENGTH // length)
        multiples_2 = (MAX_HEIGHT // length) * (MAX_WIDTH // height) * (MAX_LENGTH // width)
        multiples_3 = (MAX_HEIGHT // width) * (MAX_WIDTH // length) * (MAX_LENGTH // height)

        multiples = int(max(multiples_1, multiples_2, multiples_3))
        tot_mAh = mAh*multiples
        
        # Create a new bttery instance and add it to the array
        best_battery = dict(best_battery)
        best_battery["name"] = name
        best_battery["mAh"] = tot_mAh
        best_battery["width"] = width
        best_battery["height"] = height
        best_battery["length"] = length
        best_battery["multiples"] = multiples
        batteries.append(best_battery)

        # Debug output
        # print(multiples_1, multiples_2, multiples_3)
        # print(f"height: {MAX_HEIGHT // height}x = {height * MAX_HEIGHT // height}mm, width: {MAX_WIDTH // width}x = {width * MAX_WIDTH // width}mm, length: {MAX_LENGTH // length}x = {length* MAX_LENGTH // length}mm")
        # print(f"height: {MAX_HEIGHT // length}x = {length * MAX_HEIGHT // length}mm, width: {MAX_WIDTH // height}x = {height * MAX_WIDTH // height}mm, length: {MAX_LENGTH // width}x = {width* MAX_LENGTH // width}mm")
        # print(f"height: {MAX_HEIGHT // width}x = {width * MAX_HEIGHT // width}mm, width: {MAX_WIDTH // length}x = {length * MAX_WIDTH // length}mm, length: {MAX_LENGTH // height}x = {height* MAX_LENGTH // height}mm")
        # print("New best!", multiples, "of this battery is the most capacity you can fit")
        # print("===")

# Sort batteries
sorted_batteries_by_mAh = sorted(batteries, key=lambda d: d['mAh']) 

# Write to output file
with open("out.csv", "w") as outFile:
    outFile.write("Name,Multiples_used,Tot_cap\n")
    for battery in reversed(sorted_batteries_by_mAh):
        outFile.write(f"{battery['name']},{battery['multiples']},{battery['mAh']}\n")

# Print the best battery
# best_battery = sorted_batteries_by_mAh[-1]
# print(f"Best battery: {best_battery['multiples']} of '{best_battery['name']}' = {best_battery['mAh']}mAh")

