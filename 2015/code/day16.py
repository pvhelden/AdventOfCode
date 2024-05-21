import re

import numpy as np
import polars as pl


def parse_sues(lines: list[str]) -> pl.DataFrame:
    column_names = ['akitas', 'cars', 'cats', 'children', 'goldfish', 'perfumes', 'pomeranians', 'samoyeds', 'trees',
                    'vizslas']
    schema = {name: pl.Float32 for name in column_names}
    properties = pl.DataFrame(schema=schema)
    for line in lines:
        current: {str: float} = {name: np.nan for name in column_names}
        matches = re.findall(r'(\w+): (\d+)', line)
        for match in matches:
            current[match[0]] = np.float32(match[1])
        properties = pl.concat([properties, pl.DataFrame(current, schema=schema)])
    return properties.with_row_index(offset=1)


def find_sue(lines: list[str], to_find: dict[str, int], exact=True) -> int:
    df = pl.LazyFrame(parse_sues(lines))
    operations = {key: pl.col(key).eq for key in to_find.keys()}
    if not exact:
        operations['cats'] = pl.col('cats').gt
        operations['trees'] = pl.col('trees').gt
        operations['pomeranians'] = pl.col('pomeranians').lt
        operations['goldfish'] = pl.col('goldfish').lt
    for key, value in to_find.items():
        df = df.filter(pl.col(key).eq(np.nan) | operations[key](value))
    return df.collect()['index'][0]


def main(filename: str) -> tuple:
    with open(filename) as file:
        lines = file.read().splitlines()
        to_find = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5,
                   'trees': 3, 'cars': 2, 'perfumes': 1}
        return find_sue(lines, to_find), find_sue(lines, to_find, exact=False)
