# NearStitch – AI Powered Fashion Designer Booking System

NearStitch is a Python-based AI project developed for CFAI.  
The project helps users search nearby tailor shops, select dress stitching services, book appointments, and generate bills automatically.

---

# Project Features

- Tailor shop searching
- AI-based recommendation system
- Dress model selection
- Customer booking system
- Pickup and delivery details
- Bill generation
- GST calculation
- Order ID generation
- Runtime profiling

---

# AI Concepts Used

## CO1 – Intelligent Agent
- PEAS Model
- Knowledge Representation
- Dataclass Representation

## CO2 – Search Algorithms
- BFS
- DFS
- UCS
- A* Search
- Greedy Search

## CO3 – Constraint Satisfaction
- Slot checking
- Booking validation

## CO4 – Decision Making
- Utility Function
- Minimax
- Alpha-Beta Pruning

## CO5 – Probabilistic Reasoning
- Bayesian Probability
- Sensor Fusion

## CO6 – Performance Profiling
- Runtime calculation

---

# Technologies Used

- Python 3
- Dataclasses
- Heap Queue
- Random Module
- Time Module

---

# How to Run

## Step 1
Install Python 3.

## Step 2
Save the file as:

```bash
nearstitch.py
```

## Step 3
Open terminal or command prompt.

## Step 4
Run the program:

```bash
python nearstitch.py
```

---

# User Flow

1. Select location
2. Select city
3. View tailor shops
4. Choose tailor
5. Select AI search algorithm
6. Select dress model
7. Enter customer details
8. Enter pickup details
9. Generate bill

---

# Full Example Output

```text
====== Welcome to NearStitch ======

Select Location
1 Telangana
2 Andhra Pradesh

Enter Choice : 1

Cities Available
1 Hyderabad
2 Warangal

Enter Choice : 1

Tailor Shops in Hyderabad

1 Perfect Fit Tailor
Rating  : 4.8 ⭐
Address : MG Road
Contact : 9876543210

2 Fashion Stitch Tailor
Rating  : 4.5 ⭐
Address : Main Market
Contact : 9123456780

3 Smart Style Tailor
Rating  : 4.7 ⭐
Address : City Center
Contact : 9012345678

Enter Tailor Choice : 1

Enter tailor shop name to search : Perfect Fit Tailor

Tailor Found

Name    : Perfect Fit Tailor
Rating  : 4.8 ⭐
Address : MG Road
Contact : 9876543210

AI Search Options
1 BFS
2 DFS
3 UCS
4 A*
5 Greedy

Enter AI Search Choice : 4

Dress Models Available

1 Blouse Stitching - 500
2 Chudidar Stitching - 800
3 Lehenga Stitching - 1500
4 Kids Dress - 400

Enter Choice : 1

Enter Customer Name : Jhanasri
Enter Phone Number : 9876543210
Enter Address : Hyderabad

Enter Pickup Date (dd/mm/yyyy) : 10/05/2026
Enter Pickup Time : 10 AM
Enter Stitching Days : 5

=====================================
            NEARSTITCH BILL
=====================================

Order ID       : NST4521

Customer Name  : Jhanasri
Phone Number   : 9876543210
Address        : Hyderabad

City           : Hyderabad

Tailor Shop    : Perfect Fit Tailor

Dress Model    : Blouse

Stitching Cost : 500
GST (5%)       : 25.0
Total Cost     : 525.0

Pickup Date    : 10/05/2026
Pickup Time    : 10 AM

Delivery Info :
Delivery person will collect your cloth.
Estimated stitching time : 5 days

Utility Score  : -20.0
AI Probability : 0.96
Sensor Fusion Score : -494.2

Minimax Result : Customer Advantage
Alpha Beta : Branch Pruned

=====================================
       Thank you for using NearStitch
=====================================

Search Runtime : 0.00012
```

---

# Future Enhancements

- GUI Application
- Database Integration
- Online Payment System
- Mobile App
- Machine Learning Recommendation
- Web Application

---

# Developed By

Jhanasri Thota  
KL University Hyderabad

---

# Repository Name

```text
NearStitch-Python_2520090121
```

---

# Project File Reference

Source code reference: :contentReference[oaicite:0]{index=0}
