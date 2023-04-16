# shit's documented here: https://ccs-specs.icpc.io/2021-11/ccs_system_requirements#teamstsv

import csv
import random

# read TSV

rows = []

with open(0) as f:
	reader = csv.reader(f, delimiter='\t', quotechar='"')

	for row in reader:
		rows.append(row)

# remove header

teams = rows[3:]

# read teams

out = [
	["accounts", "1"]
]

def gen_pwd():
	WORDS = ["karwa", "karaoke", "kompetition", "konkours", "kalvitie", "koala", "kangourou", "kampus", "kwality"]

	a = random.choice(WORDS)
	b = random.choice(WORDS)
	c = random.randint(69, 420)

	return f"{a}-{b}-{c}"

for team in teams:
	id_ = team[0]
	teamname = team[9]
	
	user_1 = team[11]
	user_2 = team[15]

	out.append(["team", teamname, user_1.split()[0].lower(), gen_pwd()])

# write TSV (accounts.tsv)

for row in out:
	print('\t'.join(map(lambda field: f'"{field}"', row)))
