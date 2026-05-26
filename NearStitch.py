# =========================================================
# NearStitch - AI Powered Fashion Designer Booking System
# CFAI Project using CO1 to CO6
# =========================================================

from dataclasses import dataclass
from typing import List
import heapq
import random
import time

# =========================================================
# CO1: PEAS MODEL
# Performance  -> Accurate recommendation
# Environment  -> Users, designers, booking system
# Actuators    -> Booking confirmation
# Sensors      -> User input, ratings, budget
# =========================================================

# =========================================================
# CO1: Dataclass for AI State Representation
# =========================================================

@dataclass
class Designer:

    name: str
    rating: float
    address: str
    contact: str
    city: str
    budget: str
    cost: int
    slots: List[str]


# =========================================================
# CO1: Knowledge Representation using Lists
# =========================================================

designers = [

    Designer(
        "Perfect Fit Tailor",
        4.8,
        "MG Road",
        "9876543210",
        "Hyderabad",
        "Premium",
        500,
        ["10 AM", "1 PM"]
    ),

    Designer(
        "Fashion Stitch Tailor",
        4.5,
        "Main Market",
        "9123456780",
        "Hyderabad",
        "Medium",
        800,
        ["10 AM", "5 PM"]
    ),

    Designer(
        "Smart Style Tailor",
        4.7,
        "City Center",
        "9012345678",
        "Hyderabad",
        "Low",
        400,
        ["1 PM"]
    )
]

# =========================================================
# CO1: Dictionary for Customer Records
# =========================================================

customers = {}

# =========================================================
# CO2: BFS Search
# =========================================================

def bfs_search(city):

    queue = []
    visited = set()

    for d in designers:

        queue.append(d)

    while queue:

        current = queue.pop(0)

        if current.name not in visited:

            visited.add(current.name)

            if current.city == city:

                return current

    return None


# =========================================================
# CO2: DFS Search using Recursion
# =========================================================

def dfs_search(index, city, visited):

    if index >= len(designers):

        return None

    current = designers[index]

    if current.name in visited:

        return None

    visited.add(current.name)

    if current.city == city:

        return current

    return dfs_search(index + 1, city, visited)


# =========================================================
# CO2: UCS Search using Priority Queue
# =========================================================

def ucs_search(city):

    pq = []

    for d in designers:

        if d.city == city:

            heapq.heappush(
                pq,
                (d.cost, d.name, d)
            )

    if pq:

        return heapq.heappop(pq)[2]

    return None


# =========================================================
# CO2: Heuristic Function
# =========================================================

def heuristic(designer):

    return 5 - designer.rating


# =========================================================
# CO2: A* Search
# =========================================================

def astar_search(city):

    pq = []

    for d in designers:

        if d.city == city:

            g = d.cost
            h = heuristic(d)

            f = g + h

            heapq.heappush(
                pq,
                (f, d.name, d)
            )

    if pq:

        return heapq.heappop(pq)[2]

    return None


# =========================================================
# CO2: Greedy Search
# =========================================================

def greedy_search(city):

    best = None

    for d in designers:

        if d.city == city:

            if best is None or d.rating > best.rating:

                best = d

    return best


# =========================================================
# CO3: CSP Booking Constraint
# =========================================================

def book_slot(designer, slot):

    if slot in designer.slots:

        return True

    return False


# =========================================================
# CO3: Explainability
# =========================================================

def explain_failure(slot):

    print("\nConstraint Failed")
    print("Reason : Slot", slot, "Unavailable")


# =========================================================
# CO4: Utility Function
# =========================================================

def utility_function(designer):

    return (designer.rating * 100) - designer.cost


# =========================================================
# CO4: Minimax Concept
# =========================================================

def minimax(userCost, designerProfit):

    if userCost < designerProfit:

        return "Designer Advantage"

    return "Customer Advantage"


# =========================================================
# CO4: Alpha Beta Pruning
# =========================================================

def alpha_beta(alpha, beta):

    if alpha >= beta:

        return "Branch Pruned"

    return "Continue Search"


# =========================================================
# CO5: Bayesian Probability
# =========================================================

def bayes_probability(designer):

    return designer.rating / 5


# =========================================================
# CO5: Sensor Fusion
# =========================================================

def sensor_fusion(rating, availability, cost):

    return (rating + availability) - cost


# =========================================================
# CO6: Performance Profiling
# =========================================================

def profile_search():

    start = time.time()

    bfs_search("Hyderabad")

    end = time.time()

    print("\nSearch Runtime :", end - start)


# =========================================================
# MAIN PROGRAM
# =========================================================

print("====== Welcome to NearStitch ======")

# =========================================================
# LOCATION
# =========================================================

print("\nSelect Location")
print("1 Telangana")
print("2 Andhra Pradesh")

locationChoice = int(input("\nEnter Choice : "))

# =========================================================
# CITY
# =========================================================

if locationChoice == 1:

    print("\nCities Available")
    print("1 Hyderabad")
    print("2 Warangal")

    cityChoice = int(input("\nEnter Choice : "))

    if cityChoice == 1:

        city = "Hyderabad"

    else:

        city = "Warangal"

else:

    print("\nCities Available")
    print("1 Vijayawada")
    print("2 Guntur")

    cityChoice = int(input("\nEnter Choice : "))

    if cityChoice == 1:

        city = "Vijayawada"

    else:

        city = "Guntur"

# =========================================================
# DISPLAY TAILORS
# =========================================================

print("\nTailor Shops in", city)

count = 1

for d in designers:

    if d.city == city:

        print("\n" + str(count), d.name)
        print("Rating  :", d.rating, "⭐")
        print("Address :", d.address)
        print("Contact :", d.contact)

        count += 1

# =========================================================
# TAILOR CHOICE
# =========================================================

tailorChoice = int(input("\nEnter Tailor Choice : "))

selectedTailor = designers[tailorChoice - 1]

# =========================================================
# SEARCH OPTION
# =========================================================

searchName = input("\nEnter tailor shop name to search : ")

found = False

for d in designers:

    if d.name.lower() == searchName.lower():

        print("\nTailor Found")

        print("Name    :", d.name)
        print("Rating  :", d.rating, "⭐")
        print("Address :", d.address)
        print("Contact :", d.contact)

        found = True

if not found:

    print("Tailor Not Found")

# =========================================================
# AI SEARCH OPTIONS
# =========================================================

print("\nAI Search Options")
print("1 BFS")
print("2 DFS")
print("3 UCS")
print("4 A*")
print("5 Greedy")

searchChoice = int(input("\nEnter AI Search Choice : "))

result = None

if searchChoice == 1:

    result = bfs_search(city)

elif searchChoice == 2:

    result = dfs_search(0, city, set())

elif searchChoice == 3:

    result = ucs_search(city)

elif searchChoice == 4:

    result = astar_search(city)

elif searchChoice == 5:

    result = greedy_search(city)

# =========================================================
# DRESS MODELS
# =========================================================

print("\nDress Models Available")

print("1 Blouse Stitching - 500")
print("2 Chudidar Stitching - 800")
print("3 Lehenga Stitching - 1500")
print("4 Kids Dress - 400")

dressChoice = int(input("\nEnter Choice : "))

if dressChoice == 1:

    dress = "Blouse"
    cost = 500

elif dressChoice == 2:

    dress = "Chudidar"
    cost = 800

elif dressChoice == 3:

    dress = "Lehenga"
    cost = 1500

else:

    dress = "Kids Dress"
    cost = 400

# =========================================================
# CUSTOMER DETAILS
# =========================================================

name = input("\nEnter Customer Name : ")

phone = input("\nEnter Phone Number : ")

address = input("\nEnter Address : ")

customers[phone] = name

# =========================================================
# PICKUP DETAILS
# =========================================================

pickupDate = input("\nEnter Pickup Date (dd/mm/yyyy) : ")

pickupTime = input("\nEnter Pickup Time : ")

stitchingDays = int(input("\nEnter Stitching Days : "))

# =========================================================
# CO3: Constraint Checking
# =========================================================

booking = book_slot(result, pickupTime)

if not booking:

    explain_failure(pickupTime)

# =========================================================
# GST CALCULATION
# =========================================================

gst = cost * 0.05

totalCost = cost + gst

# =========================================================
# ORDER ID
# =========================================================

orderID = "NST" + str(random.randint(1000,9999))

# =========================================================
# FINAL BILL
# =========================================================

print("\n=====================================")
print("            NEARSTITCH BILL          ")
print("=====================================")

print("\nOrder ID       :", orderID)

print("\nCustomer Name  :", name)
print("Phone Number   :", phone)
print("Address        :", address)

print("\nCity           :", city)

print("\nTailor Shop    :", result.name)

print("\nDress Model    :", dress)

print("\nStitching Cost :", cost)
print("GST (5%)       :", gst)
print("Total Cost     :", totalCost)

print("\nPickup Date    :", pickupDate)
print("Pickup Time    :", pickupTime)

print("\nDelivery Info :")
print("Delivery person will collect your cloth.")
print("Estimated stitching time :", stitchingDays, "days")

# =========================================================
# CO4: Utility Evaluation
# =========================================================

utility = utility_function(result)

print("\nUtility Score  :", utility)

# =========================================================
# CO5: Probability Reasoning
# =========================================================

probability = bayes_probability(result)

print("AI Probability :", probability)

fusion = sensor_fusion(
    result.rating,
    1,
    result.cost
)

print("Sensor Fusion Score :", fusion)

# =========================================================
# CO4: Decision Making
# =========================================================

print("\nMinimax Result :",
      minimax(cost, result.cost))

print("Alpha Beta :",
      alpha_beta(5, 3))

print("\n=====================================")
print("       Thank you for using NearStitch")
print("=====================================")

# =========================================================
# CO6: Runtime Profiling
# =========================================================

profile_search()