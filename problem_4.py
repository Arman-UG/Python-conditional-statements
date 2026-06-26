passenger_rating = 4.8      
is_account_flagged = False  
is_rush_hour = True         # Let's test with Rush Hour ON
available_drivers = 3       
base_fare = 150.0           

# --- GATE 1: SECURITY & AVAILABILITY ---
if is_account_flagged or passenger_rating < 3.0:
    print("Ride Canceled: Account safety check failed.")
elif available_drivers == 0:
    print("Ride Canceled: No drivers available in your area right now.")

# --- GATE 2: THE PRICING PIPELINE ---
else:
    # Start our calculation pipeline
    final_fare = base_fare
    
    # Step A: Apply Surge if applicable
    if is_rush_hour:
        if available_drivers < 5:
            final_fare = base_fare * 1.5  # Heavy surge
        else:
            final_fare = base_fare * 1.2  # Mild surge
            
    # Step B: Apply VIP Discount to whatever the fare is right now
    if passenger_rating > 4.7:
        final_fare = final_fare - 20
        print("🎉 VIP Reward: ₹20 loyalty discount applied!")

    # Step C: One single print statement for the final result
    print("Ride Confirmed!")
    print("Final Fare: ₹", final_fare)