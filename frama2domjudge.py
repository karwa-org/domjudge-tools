# shit's documented here: https://ccs-specs.icpc.io/2021-11/ccs_system_requirements#teamstsv
# adding data through jury interface: https://www.domjudge.org/snapshot/manual/import.html

import csv
import random
import string

# read TSV

rows = []

with open(0) as f:
	reader = csv.reader(f, delimiter='\t', quotechar='"')

	for row in reader:
		rows.append(row)

# remove header

rows = rows[3:]

# setup

teams = [
	["teams", 1]
]

accounts = [
	["accounts", 1]
]

random.seed(69)

def gen_pwd():
	WORDS = ["karwa", "karaoke", "kompetition", "konkours", "kalvitie", "koala", "kangourou", "kampus", "kwality"]

	a = random.choice(WORDS)
	b = random.choice(WORDS)
	c = random.randint(69, 420)

	return f"{a}-{b}-{c}"

BASE_OTHER = 0000
BASE_UCL = 1000
BASE_UMONS = 2000

# read teams

team_map = {}

for team in rows:
	institution = team[10]
	base = BASE_OTHER

	if institution == "UCLouvain":
		base = BASE_UCL

	elif institution == "UMons":
		base = BASE_UMONS

	id_ = int(team[0])
	teamname = team[9]

	user_1 = team[11]
	user_2 = team[15]

	teams.append([id_, base + id_, 0, teamname, institution, institution, "BEL"])
	team_map[teamname] = id_

# read accounts

for team in teams[1:]:
	teamname = team[3]
	username = "".join(filter(lambda x: x in string.ascii_letters, teamname)).lower()
	password = gen_pwd()

	id_ = str(team_map[teamname])
	accounts.append(["team", username + id_, username + id_, password])

# write TSV's (teams.tsv & accounts.tsv)

def write_tsv(name, rows):
	with open(f"{name}.tsv", "w") as f:
		for row in rows:
			f.write('\t'.join(map(str, row)) + '\n')

write_tsv("teams", teams)
write_tsv("accounts", accounts)
