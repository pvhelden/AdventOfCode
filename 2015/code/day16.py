import re

import polars as pl


def parse_sues(lines: [str]) -> pl.DataFrame:
    column_names = ['akitas', 'cars', 'cats', 'children', 'goldfish', 'perfumes', 'pomeranians', 'samoyeds', 'trees',
                    'vizslas']
    properties = pl.DataFrame(schema={name: int for name in column_names})
    for line in lines:
        current: {str: int} = {name: -1 for name in column_names}
        matches = re.findall(r'(\w+): (\d+)', line)
        for match in matches:
            current[match[0]] = int(match[1])
        properties = pl.concat([properties, pl.DataFrame(current)])
    return properties.with_row_index(offset=1)


def find_sue(lines: [str], to_find: {str: int}) -> int:
    df = pl.LazyFrame(parse_sues(lines))
    for key, value in to_find.items():
        df = df.filter(pl.col(key).eq(value) | pl.col(key).eq(-1))
    return df.collect()['index'][0]


def main(filename: str) -> tuple:
    with open(filename) as file:
        lines = file.read().splitlines()
        to_find = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5,
                   'trees': 3, 'cars': 2, 'perfumes': 1}
        return find_sue(lines, to_find), None
