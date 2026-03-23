# -------------------------------------------
# Exercise: The Manchester Program
# -------------------------------------------
#
# GOAL: 
# Solve these standalone "Logic Puzzles".
# You must handle errors, validate strings, and manage data structures.
#
# -------------------------------------------

# -------------------------------------------
# Task 1: The Etihad Stadium Seating Checker
# -------------------------------------------
# CONCEPT: 
# In professional ticketing systems, we use functions to categorise users 
# automatically. This prevents human error at the gate. This task requires 
# you to use "Nested Logic" (if-statements inside if-statements) to 
# ensure fans get the correct ticket type based on their status.
#
# TODO:
# 1. Create a function 'get_stadium_access'.
# 2. Ask for the user's 'age' and if they have a 'membership' (yes/no).
# 3. Validation: The age must be a number. If they type "ten", the program 
#    shouldn't crash—it should tell them to enter a digit.
# 4. Logic: 
#    - If they are under 12, they need a "Junior Blue" pass.
#    - If 12-65 AND have a membership, they get "General Admission".
#    - If 12-65 but NO membership, they are directed to the "Ticket Office".
#    - If over 65, they get the "Legends Lounge" access.
# 5. Call the function and ensure it prints the specific result.

# Write your code below:


# -------------------------------------------
# Task 2: The Northern Quarter Café Tab
# -------------------------------------------
# CONCEPT: 
# Point of Sale (POS) systems use dictionaries to map items to their 
# prices. This allows a business to change a price in one place without 
# rewriting the whole program. You will practice retrieving data 
# and performing calculations with conditional discounts.
#
# TODO:
# 1. Create a dictionary called 'menu' with 3 Manchester-themed food items 
#    (e.g. "Bury Black Pudding Benedict": 9.50, "Vimto Glazed Ribs": 12.00).
# 2. Ask the user to input the name of the dish they want to order.
# 3. Logic:
#    - Use a conditional to check if that dish exists in your dictionary.
#    - If it exists, ask "How many portions?".
#    - Calculate the total: (Price of dish * Number of portions).
#    - Apply a "MCR Resident Discount": If the total is over £20, take £5 off.
#    - Print a receipt showing the final price.
# 4. If the dish doesn't exist, print "Sorry, that's not on the menu today."

# Write your code below:


# -------------------------------------------
# Task 3: The Deansgate Traffic Logger
# -------------------------------------------
# CONCEPT: 
# Real-world data is often "messy" (users add extra spaces or random 
# capitalisation). "Data Sanitisation" is the process of cleaning this 
# data before it enters a database. This task uses a loop to build a 
# reliable list of clean, standardised records.
#
# TODO:
# 1. Create an empty list called 'traffic_log'.
# 2. Create a loop that keeps asking for a 'vehicle_type' (Bus, Taxi, Car).
# 3. The loop should only end if the user types "STOP".
# 4. Inside the loop, you must "sanitise" the input:
#    - Remove any accidental spaces (e.g. "  bus  " becomes "bus").
#    - Convert it to lowercase so "TAXi" and "taxi" are treated the same.
# 5. If the input is valid (one of the three types), .append() it to the list.
# 6. If it's invalid (and not "STOP"), print "Invalid vehicle—entry ignored."
# 7. After the loop ends, print the total number of vehicles logged.

# Write your code below:


# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------

# Extension 1: The Curry Mile Multi-Search
# -------------------------------------------
# CONCEPT: 
# Data is rarely just a simple list; it is usually a "List of Dictionaries." 
# This mirrors how professional databases work. To find specific 
# information (like a high-rated restaurant), you must iterate through 
# the list and "filter" the results based on multiple conditions.
#
# TODO:
# 1. Create a list 'restaurants' containing 4 dictionaries. 
#    Each needs: "name", "cuisine", and "rating" (1-5).
# 2. Ask the user: "What cuisine are you looking for?"
# 3. Ask the user: "What is the minimum rating you accept (1-5)?"
# 4. Use a loop to search the list.
# 5. Requirement: Only print the restaurant if BOTH the cuisine matches 
#    AND the rating is equal to or higher than what the user asked for.
# 6. If no restaurants meet both criteria, print "No matches found on Wilmslow Road."

# Write your code below:


# Extension 2: The Trafford Centre Security Gate
# -------------------------------------------
# CONCEPT: 
# Cybersecurity and access control rely on strict input validation. 
# If a user provides an ID that doesn't follow the "Business Rules," the 
# system must reject it. You will practice using Boolean flags or 
# while-loops to enforce specific formatting rules.
#
# TODO:
# 1. Create a function 'validate_staff_id'.
# 2. Ask the user for a Staff ID.
# 3. A valid ID must meet these 3 rules:
#    - Rule 1: Must be exactly 6 characters long.
#    - Rule 2: Must start with the letters "MCR".
#    - Rule 3: Must not contain any spaces.
# 4. Use a 'while' loop. If the ID fails any of these rules, explain 
#    EXACTLY which rule was broken and ask again.
# 5. Once a valid ID is entered, print "Access Granted to Trafford Centre."

# Write your code below:


# Extension 3: The Bee Network - Ticket Audit
# -------------------------------------------
# CONCEPT: 
# Transport systems like Greater Manchester's "Bee Network" deal with 
# thousands of ticket transactions daily. Often, a programmer must 
# "Audit" these lists to find specific ticket types or calculate 
# daily totals. You will practice iterating through a list, 
# transforming string data, and using a "Counter" to provide 
# a report for Transport for Greater Manchester (TfGM).
#
# TODO:
# 1. Create a list called 'daily_tickets' containing at least 8 ticket 
#    types (e.g. "Peak-Single", "Off-Peak-Day", "Student-Pass").
# 2. Requirement: Ensure some tickets contain the word "Peak" and 
#    some contain the word "Pass".
# 3. Create a function 'run_ticket_audit' that loops through the list.
# 4. Inside the loop, you must perform the following logic:
#    - Rule 1: If the ticket contains the word "Peak", print: 
#      "Validating High-Traffic Ticket: [Ticket Name]".
#    - Rule 2: If the ticket contains the word "Pass", print: 
#      "Season Ticket Detected - Check Photo ID for [Ticket Name]".
#    - Rule 3: For any other ticket, print: "Standard Fare: [Ticket Name]".
# 5. Requirement: Create a 'peak_total' variable. Every time Rule 1 is met, 
#    add 1 to this total.
# 6. After the loop finishes, print a final summary: 
#    "Audit Complete. Total Peak-Time tickets processed: [peak_total]".

# Write your code below:


# -------------------------------------------
# ADVANCED: The Manchester Weather Analyst
# -------------------------------------------
# CONCEPT: 
# Data analysis involves "aggregating" information (turning a large 
# list of numbers into useful stats). This program simulates a 
# weather station report, requiring you to perform multiple mathematical 
# passes over a dataset to provide a final safety assessment.
#
# TODO:
# 1. Create a list of daily rainfall totals (in mm) for a week: [5, 12, 0, 8, 15, 2, 9].
# 2. Create a function 'analyse_rain' that calculates 3 things:
#    - The 'Total Rainfall' for the week (sum).
#    - The 'Average Rainfall' (total / 7).
#    - The 'Dry Days': Count how many days had 0mm of rain.
# 3. Logic: If the Average Rainfall is over 8mm, print "Warning: Flood Risk."
# 4. Logic: If there are more than 2 dry days, print "Unusually sunny for Manchester!"
# 5. Return all three calculated values and print them in a clean summary.

# Write your code below:
