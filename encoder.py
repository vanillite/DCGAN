import os

def main():
    base_dir = "generatedLevels"
    object_map = {"goal": "g",
                "key": "+",
                "nokey": "A",
                "withkey": ".",
                "floor": ".",
                "wall": "w",
                "monsterQuick": "1",
                "monsterNormal": "2",
                "monsterSlow": "3",
                "floor goal": "g",
                "floor key": "+",
                "floor nokey": "A",
                "floor withkey": ".",
                "floor monsterQuick": "1",
                "floor monsterNormal": "2",
                "floor monsterSlow": "3"}
    
    generators = ["constructiveLevelGenerator", "randomLevelGenerator"]

    for generator in generators:
        for level in range(0,100):
            path = os.path.join(base_dir,generator, f'zelda_lvl{level}.txt')
            level_map = {" ": "."}
            with open(path) as file:
                lines = [line for line in file]
            lines = iter(lines)

            line = next(lines)
            while not "LevelDescription" in line:
                if not ">" in line:
                    line = next(lines)
                    continue

                c, s = line.strip().split(" > ")
                level_map[c] = object_map[s]

                line = next(lines) 
            line = next(lines)
            new_contents = []
            while line:
                new_contents.append("".join(replace_char(c, level_map) for c in line))
                line=next(lines, 0)

            output_dir = os.path.join(base_dir, "processed_levels", generator)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir, exist_ok=True)
            output_path = os.path.join(output_dir, f'zelda_lvl{level}.txt')

            with open(output_path, 'w') as output_file:
                output_file.write("".join(new_contents))

def replace_char(char, dict):
    if char in dict:
        return dict[char]
    return char 

if __name__ == "__main__":
    main()