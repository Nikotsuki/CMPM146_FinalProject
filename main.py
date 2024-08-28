from htn_planner import load_breeding_data, decompose_task
import sys

def main():
    # Load the breeding data
    breeding_data = load_breeding_data("breeding_data.json")
    
    # Test the decompose_task function
    pets_we_have = ["Lifmunk", "Cattiva"]  # Example of pets we currently have
    desired_pet = "Vixy"  # The pet we want to breed

    #sys.setrecursionlimit(20000)
    
    # Decompose the task to see the required breeding steps
    tasks = decompose_task(desired_pet, breeding_data, pets_we_have)
    
    # Print the decomposed tasks
    print(f"Tasks to breed {desired_pet}:")
    for task in tasks:
        parent_1 = breeding_data["parents"][task[0]]
        parent_2 = breeding_data["parents"][task[1]]
        print(f"Breed {parent_1} with {parent_2}")

if __name__ == "__main__":
    main()
