import unidecode

with open('miembros.txt', 'r', encoding='utf-8') as file:
    members = file.readlines()
    members = [member.strip() for member in members]

mapping = {}
for num in range(len(members)):
    print(members[num])
    name, surename = members[num].split(' ')
    mapping[unidecode.unidecode(name[0] + surename[:2]).lower()] = name + ' ' + surename


def to_command(command_name: str, name: str):
    return '\\newcommand{\\' + command_name + '}[1]{[\\textit{' + name + '}]: #1\\\\}\n'


def general_command():
    return '\\newcommand{\\phab}[2]{[\\textit{#1}]: #2\\\\}'


with open('macrosnombres.sty', 'w', encoding='utf-8') as file:
    file.write('\\ProvidesPackage{macrosnombres}[2018/12/05 Macros CAi]\n')
    for command, name in mapping.items():
        file.write(to_command(command, name))
    file.write(general_command())
