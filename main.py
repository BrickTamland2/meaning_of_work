#%% import packages

import pickle
import sim_occs
import semchange
import simdim
import sim_oneterm


#%% load data

with open('./data/models_all.pickle', 'rb') as handle:
    models_all = pickle.load(handle)


#%%  most similar terms

for x, y in models_all.items():
    print(x)
    print(y.most_similar("work"))

# --> work has a different meaning before 1850

#%% visualize word embeddings over time (PCA mit keyword als passiv)

semchange.semchange(models_all, "work", rangelow=1810, rangehigh=2000, rangestep=60, export=False)


#%% association of work with different dimension

# set up dictionary and define "work"

keywords = dict()

keywords['work'] = [
    "work", "works", "worked", "working", "job", "jobs",
    "career", "careers",
    "profession", "professions", "professional",
    "occupation", "occupations",
    "employment", "employed",
    "labor", "labors"
]

for i in keywords['work']:
    for year, model in google.items():
        if model[i].all() == google[1840]['biology'].all():
            if year >= 1850:
                print(str(year) + ": " + i)



#%% smith: toil (einzelne Begriffe anzeigen?)

keywords['toil'] = [
    "hard", "struggle", "toil", "trouble", "suffer", "endure", "arduous", "strenuous", "grind"
]

simdim.simdim(models_all, keywords, 'work', 'toil', trend=3, diff=False, rangelow=1850, rangehigh=2000, rangestep=10)
simdim.simdim(models_all, keywords, 'work', 'toil')


keywords['leisure'] = ["leisure", "ease", "rest", "recreation", "relaxation", "freedom"]
simdim.simdim(models_all, keywords, 'work', 'leisure')

simdim.simdim(models_all, keywords, 'work', 'toil', 'leisure')


keywords['hard'] = ['hard']
keywords['struggle'] = ['struggle']
keywords['toil'] = ['toil']
keywords['trouble'] = ['trouble']
keywords['suffer'] = ['suffer']
keywords['endure'] = ['endure']
keywords['arduous'] = ['arduous']
keywords['strenuous'] = ['strenuous']

simdim.simdim(models_all, keywords, 'work', 'hard', 'struggle', 'toil', 'trouble',
              'suffer', 'endure', 'arduous', 'strenuous')


keywords['fun'] = ["fun", "enjoy", "pleasant", "happy", "like", "love", "delight"]
simdim.simdim(models_all, keywords, 'work', 'fun')
simdim.simdim(models_all, keywords, 'work', 'toil', 'fun')

keywords['stress'] = ["stress", "exhausting", "tired"]
simdim.simdim(models_all, keywords, 'work', 'stress')
simdim.simdim(models_all, keywords, 'work', 'toil', 'stress')

keywords['emotion'] = [
    "pleasant", "interesting", "boring", "fulfilling", "meaningful", "meaningless",
    "hard", "struggle", "toil", "trouble", "suffer", "endure", "arduous", "strenuous"
]
simdim.simdim(models_all, keywords, 'work', 'emotion')

keywords['commodity'] = [
    "market", "exchange", "trade", "hire", "rent"
]
simdim.simdim(models_all, keywords, 'work', 'commodity')  # nicht sehr spannend


sim_oneterm.sim_oneterm(models_all, keywords, 'work', 'duty')  # auch teil von "patriot"

sim_oneterm.sim_oneterm(models_all, keywords, 'work', 'pleasant')


#%% marx: alienation (extrinsic vs. intrinsic)

keywords['mat'] = [
                    "earn", "earns", "earning", "earnings",
                    "wage", "wages", "salary", "income", "remuneration", "pay",
                    "secure", "security", "insecure", "insecurity"
]


keywords['secure'] = [
                      "secure", "security", "insecure", "insecurity"
]


keywords['postmat'] = ["interesting", "boring", "fulfilling", "meaningful", "meaningless", "useful", "useless",
                       "expression", "creative"]

simdim.simdim(models_all, keywords, 'work', 'mat')
simdim.simdim(models_all, keywords, 'work', 'postmat')
simdim.simdim(models_all, keywords, 'work', 'secure')

simdim.simdim(models_all, keywords, 'work', 'mat', 'postmat')

keywords['useful'] = ["useful", "society"]
simdim.simdim(models_all, keywords, 'work', 'useful')


keywords['status'] = [
    "prestigious", "honorable", "esteemed", "influential", "reputable", "distinguished",
    "eminent", "illustrious", "renowned", "acclaimed"
]
simdim.simdim(models_all, keywords, 'work', 'mat', 'postmat', 'status')

keywords['social'] = ["colleague", "colleague", "friend", "friends", "people"]
simdim.simdim(models_all, keywords, 'work', 'social')

simdim.simdim(models_all, keywords, 'work', 'mat', 'postmat', 'status', 'social')


#%% weber: wealth & religion

keywords['rich'] = ["wealth", "wealthy", "rich", "affluence", "affluent"]
keywords['poor'] = ["poor", "poverty", "impoverished", "destitute", "needy"]
simdim.simdim(models_all, keywords, 'work', 'rich', 'poor')


keywords['affluence'] = keywords['rich'] + keywords['poor']
simdim.simdim(models_all, keywords, 'work', 'affluence')  # --> Piketty!


keywords['success'] = ["success", "succeed", "failure", "fail"]
simdim.simdim(google, keywords, 'work', 'success')

keywords['religion'] = ["redemption", "salvation", "god", "religion", "pious"]
simdim.simdim(google, keywords, 'work', 'religion')
simdim.simdim(google, keywords, 'work', 'religion', 'moral', 'affluence')



keywords['vocation'] = ["vocation", "calling", "meaning", "purpose"]
simdim.simdim(models_all, keywords, 'work', 'vocation')

keywords['moral'] = [
    'good', 'evil', 'moral', 'immoral', 'good', 'bad', 'honest', 'dishonest',
    'virtuous', 'sinful', 'virtue', 'vice'
]
simdim.simdim(models_all, keywords, 'work', 'moral')  # --> Piketty!

# work hard?

# Weber: was läuft bei WK?

keywords['patriot'] = ["duty", "country", "patriot", "fatherland", "home"]
simdim.simdim(models_all, keywords, 'work', 'patriot')









#%% VALIDATION

# faktisch

# connotation von Arbeit mit mann/frau

keywords['male'] = ["male", "man", "boy", "brother", "he", "him", "his", "son"]
keywords['female'] = ["female", "woman", "girl", "sister", "she", "her", "hers", "daughter"]

simdim.simdim(models_all, keywords, 'work', 'male')
simdim.simdim(models_all, keywords, 'work', 'female')
simdim.simdim(models_all, keywords, 'work', 'male', 'female', diff=False)
simdim.simdim(models_all, keywords, 'work', 'male', 'female', diff=True)


# typische arbeitsgeräte für verschiedene epochen

keywords['plow'] = ['plow']
keywords['telephone'] = ['telephone']
keywords['computer'] = ['computer']

simdim.simdim(models_all, keywords, 'work', 'plow')
simdim.simdim(models_all, keywords, 'work', 'telephone')
simdim.simdim(models_all, keywords, 'work', 'computer')

simdim.simdim(models_all, keywords, 'work', 'plow', 'telephone', 'computer', trend=3)


# historisches wachstum von sektoren

keywords['sector1'] = ["agriculture", "farming", "logging", "fishing", "forestry", "mining"]

keywords['sector2'] = ["manufacturing", "textile", "car", "handicraft"]

keywords['sector3'] = ["service", "social", "information", "advice", "access"]

simdim.simdim(models_all, keywords, 'work', 'sector1', 'sector2', 'sector3', trend=3)

# typisch weibliche/männliche Berufe

keywords['male'] = ["male", "man", "boy", "brother", "he", "him", "his", "son"]
keywords['female'] = ["female", "woman", "girl", "sister", "she", "her", "hers", "daughter"]


sim_occs.sim_occs(models_all, keywords, 'mechanic', 'carpenter', 'engineer', 'nurse', "dancer", "housekeeper")


# SEMANTIC DRIFT

# housework --> work

keywords['housework'] = ["housework", "household"]
simdim.simdim(models_all, keywords, 'work', 'housework')


# beziehungsarbeit

keywords['relations'] = ["relationship"]
simdim.simdim(models_all, keywords, 'work', 'relations')


# DISKURS: Arbeiterbewegung

keywords['politics'] = ["party", "politics", "movement", "election"]
simdim.simdim(models_all, keywords, 'work', 'politics')
