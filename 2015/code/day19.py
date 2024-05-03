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


def main(filename: str) -> tuple:
    with open(filename) as file:
        lines = file.read().splitlines()
        molecule = ('CRnSiRnCaPTiMgYCaPTiRnFArSiThFArCaSiThSiThPBCaCaSiRnSiRnTiTiMgArPBCaPMgYPTiRnFArFArCaSiRnBPMgArPRn'
                    'CaPTiRnFArCaSiThCaCaFArPBCaCaPTiTiRnFArCaSiRnSiAlYSiThRnFArArCaSiRnBFArCaCaSiRnSiThCaCaCaFYCaPTiB'
                    'CaSiThCaSiThPMgArSiRnCaPBFYCaCaFArCaCaCaCaSiThCaSiRnPRnFArPBSiThPRnFArSiRnMgArCaFYFArCaSiRnSiAlArT'
                    'iTiTiTiTiTiTiRnPMgArPTiTiTiBSiRnSiAlArTiTiRnPMgArCaFYBPBPTiRnSiRnMgArSiThCaFArCaSiThFArPRnFArCaSiR'
                    'nTiBSiThSiRnSiAlYCaFArPRnFArSiThCaFArCaCaSiThCaCaCaSiRnPRnCaFArFYPMgArCaPBCaPBSiRnFYPBCaFArCaSiAl')
        return count_molecules(lines, molecule), None
