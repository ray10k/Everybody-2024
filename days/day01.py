
def monster_strength(letter:str) -> int:
    if letter == "B":
        return 1
    if letter == "C":
        return 3
    if letter == "D":
        return 5
    return 0

def puzzle_1(in_data:str) -> str:
    retval = 0
    for character in in_data:
        retval += monster_strength(character)
    return f"{retval}"

def puzzle_2(in_data:str) -> str:
    import itertools
    retval = 0
    
    for pair in itertools.batched(in_data,2):
        if "x" not in pair:
            retval += 2
        for character in pair:
            retval += monster_strength(character)
    return f"{retval}"

def puzzle_3(in_data:str) -> str:
    import itertools
    retval = 0
    
    for trio in itertools.batched(in_data,3):
        group_size = 3 - trio.count("x")
        if group_size == 3:
            retval += 6 # 3 monsters requiring 2 additional potions each.
        elif group_size == 2:
            retval += 2 # 2 monsters requiring 1 additional potion each.
        
        for character in trio:
            retval += monster_strength(character)
    
    return f"{retval}"

if __name__ == "__main__":
    import pathlib
    input_base = pathlib.Path(__file__).parent.parent / "inputs"
    def run_puzzle(puzzle_no:int, base_path:pathlib.Path):
        if (base_path / f"day01-{puzzle_no}.txt").exists():
            print(f"Running puzzle {puzzle_no}")
            src = input_base / f"day01-{puzzle_no}.txt"
            with open(src,"r") as data_in:
                data = data_in.read()
                result = eval(f"puzzle_{puzzle_no}(data)")
                print(f"Puzzle {puzzle_no}: {result}")
        else:
            print(f"No input available for puzzle {puzzle_no}")
    run_puzzle(1,input_base)
    run_puzzle(2,input_base)
    run_puzzle(3,input_base)