marvelchars= {
        
"starlord":
    {"real name": "peter quill",
    "powers": "dance moves",
    "archenemy": "thanos"},

"mystique":
    {"real name": "raven darkholme",
    "powers": "shape shifter",
    "archenemy": "professor x"},

"hulk":
    {"real name": "bruce banner",
    "powers": "super strength",
    "archenemy": "adrenalin"}
        }    

def print_character_info(char_name, char_stat, char_value):
    formatted_output = f"{char_name.get(char_stat).title()}'s {char_stat.get(char_value)} is {char_value.title()}"
    print(formatted_output)


character = "starlord"
stat = "real name"
char_value = marvelchars[character][stat]
print_character_info(character, stat, char_value)

character = "mystique"
stat = "real name"
char_value = marvelchars[character][stat]
print_character_info(character, stat, char_value)

character = "hulk"
stat = "real name"
char_value = marvelchars[character][stat]
print_character_info(character, stat, char_value)

