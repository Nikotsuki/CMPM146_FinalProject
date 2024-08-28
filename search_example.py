import json

def load_breeding_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
    
def get_child(pal1, pal2, breeding_data):
    for pair in breeding_data["parents"].items():
        #print(pair)
        if pair[1] == pal2:
            pal2_key = pair[0]
    child = breeding_data["results"][pal1][pal2_key]
    return child

def traceback(pals_we_have, target_pal):
    
    return

def search_for_child(breeding_data, pals_we_have, target_pal):
    search = True
    while search != False:
        new_pals = []
        for pal in pals_we_have:
            for pals in pals_we_have:
                child = get_child(pal, pals, breeding_data)
                if child == target_pal:
                    #traceback(pals_we_have, target_pal)
                    print(child)
                    search = False
                    return
                if child not in pals_we_have and child not in new_pals:
                    new_pals.append(child)
        #print(new_pals)
        if not new_pals:
            print("No path found")
            return
        for pal in new_pals:
            pals_we_have.append(pal)
        print(pals_we_have)


def main():
    breeding_data = load_breeding_data("breeding_data.json")
    pals_we_have = ["Lifmunk", "Cattiva", "Pengullet"]
    desired_pal = "Foxparks"
    search_for_child(breeding_data, pals_we_have, desired_pal)

if __name__ == "__main__":
    main()