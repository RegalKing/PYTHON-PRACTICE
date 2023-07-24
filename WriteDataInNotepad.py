def write_data_to_file(filename):
    data_dict = {}
    
    # Read existing data from the file (if any)
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, *ratings = line.strip().split(',')
                data_dict[name] = [float(rating) for rating in ratings]
    except FileNotFoundError:
        pass
    
    # Prompt for new player names and ratings
    while True:
        player_name = input("Player's name? (Press Enter to stop): ")
        if not player_name:
            break
        
        ratings_input = input("Their rating? (separate ratings by commas): ")
        player_ratings = [float(rating) for rating in ratings_input.split(',')]
        
        if player_name in data_dict:
            data_dict[player_name].extend(player_ratings)
        else:
            data_dict[player_name] = player_ratings
    
    # Write the updated data back to the file
    with open(filename, 'w') as file:
        for name, ratings in data_dict.items():
            avg_rating = sum(ratings) / len(ratings)
            avg_formatted = f"{avg_rating:.2f}"
            ratings_str = ", ".join(str(rating) for rating in ratings)
            file.write(f"{name} - {ratings_str} [{avg_formatted}]\n")

if __name__ == "__main__":
    output_file = input("Enter the filename to store the data: ")
    write_data_to_file(output_file)
