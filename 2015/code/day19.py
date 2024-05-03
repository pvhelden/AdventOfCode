import re


def parse_replacements(lines: [str]) -> [(str, str)]:
    return [tuple(line.split(' => ')) for line in lines]


def count_molecules(lines: [str], molecule: str) -> int:
    replacements = parse_replacements(lines)
    distinct_molecules = set()
    for atom, replacement in replacements:
        for match in re.finditer(atom, molecule):
            new_molecule = molecule[:match.start()] + replacement + molecule[match.end():]
            distinct_molecules.add(new_molecule)
    return len(distinct_molecules)


def get_reverse_replacements_dict(lines: [str]) -> dict[str, str]:
    return {replacement: atom for line in lines for atom, replacement in [line.split(' => ')]}


def count_min_steps(lines: [str], molecule: str) -> int:
    reverse_replacements = get_reverse_replacements_dict(lines)
    steps = 0
    while molecule != 'e':
        modified = False
        i = 0
        keys = [*reverse_replacements.keys()]
        while not modified:
            index = molecule.find(keys[i])
            if index != -1:
                molecule = molecule[:index] + reverse_replacements[keys[i]] + molecule[index + len(keys[i]):]
                modified = True
            i += 1
        steps += 1
    return steps


def main(filename: str) -> tuple:
    with open(filename) as file:
        lines = file.read().splitlines()
        molecule = ('CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRn'
                    'CaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiB'
                    'CaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArT'
                    'iTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiR'
                    'nTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl')
        return count_molecules(lines, molecule), count_min_steps(lines, molecule)
