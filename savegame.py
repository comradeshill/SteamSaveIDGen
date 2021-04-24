print("Enter your save game ID")

save_id = input()

if save_id == "00000666":
    f = open("user_steam_id.txt", "w")
    f.write("76561197960267366")
    f.close()
    print("Done. Press any key to exit.")
    input()

else:
    base_id = 76561197960267366
    base_match = "00000666"
    dec_input_id = int(save_id, 16)
    change = dec_input_id - int(base_match, 16)
    new_id = base_id + change
    f = open("user_steam_id.txt", "w")
    f.write(str(new_id))
    f.close()
    print("Done. Press any key to exit.")
    input()
