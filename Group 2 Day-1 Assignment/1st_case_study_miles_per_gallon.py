def main():
    # Initialize variables to keep track of total miles and gallons
    total_miles = 0.0
    total_gallons = 0.0

    while True:
        # Prompt the user to input gallons used
        gallons = float(input("Enter the gallons used (-1 to end): "))
        
        # Check for sentinel value
        if gallons == -1:
            break
        
        # Prompt the user to input miles driven
        miles = float(input("Enter the miles driven: "))
        
        # Calculate and display miles per gallon for the current tankful
        mpg = miles / gallons
        print(f"The miles/gallon for this tank was {mpg:.6f}")
        
        # Update total miles and total gallons
        total_miles += miles
        total_gallons += gallons

    # Calculate and display the combined miles per gallon if total_gallons is not zero
    if total_gallons != 0:
        combined_mpg = total_miles / total_gallons
        print(f"\nThe overall average miles/gallon was {combined_mpg:.6f}")
    else:
        print("\nNo data entered.")

# Run the main function
if __name__ == "__main__":
    main()
