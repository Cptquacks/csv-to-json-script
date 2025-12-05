import json

def read_csv_lines(path: str, parse_symbol: str = '|') -> list[list[str]]:
    new_csv_lines : list[list[str]] = []

    with open(file = f'{path}', mode = 'r', encoding='UTF-8') as readen_file: 
        for line in readen_file.readlines():
            new_csv_lines.append(
                line
                .replace('\n', '')
                .split(parse_symbol)
            )

    return new_csv_lines

def convert_csv_lines(path: str, primary_key: str = '') -> dict:
    print(f'Diving into {path}')
    if primary_key.__len__() > 0 : primary_key += '-'

    new_json_lines : dict = {}
    get_csv_lines : list[list[str]] = read_csv_lines(path)
    csv_lines_heading : list[str] = get_csv_lines[0]
    

    x : int = 0;y : int = 0
    key_index : int = 0


    for line in get_csv_lines:
        if (key_index != 0) : 
            new_json_lines[f'{primary_key}{key_index}'] = {}

        key_index += 1


    print(f'generated {key_index-2} id\'s \n')
    key_index = 0


    for line in get_csv_lines:

        for element in line:
            if (key_index == 0) : break
            try:
                if (x != 0) : 
                    new_json_lines[f'{primary_key}{key_index}'] [csv_lines_heading[x]] = element
            except IndexError:
                print(f"Error on index {x}")

            x+=1

        key_index += 1;x = 0



    return new_json_lines

def write_to_json(output: str, data: dict) -> None:
    with open(file=f'{output}', mode='w', encoding='UTF-8') as write_to:
        json.dump(data, write_to, indent=4, separators=(',', ':'),)

def write_to_jsonl(output: str, data: dict) -> None:
    new_json_list : list[dict] = [data]
    with open(file=f'{output}', mode='w', encoding='UTF-8') as write_to:
        json.dump(new_json_list, write_to, indent=4, separators=(',', ':'),)