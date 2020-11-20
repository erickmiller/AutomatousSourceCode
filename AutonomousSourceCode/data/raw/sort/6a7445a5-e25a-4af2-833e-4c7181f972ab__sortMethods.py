from Mafiastats.mafiaStats.models import  Game, Team, Category,Player
from django.db.models.query import QuerySet


def attrSort(items,attr,reverse,category=None):
	print str(reverse)
	return sorted(items,(lambda x,y: cmp(getattr(x,attr),getattr(y,attr))),reverse=reverse)


def sortQuery(query,sortMethod,reverse,category):
	"""Returns a sorted queryset Will use sort_by if sortMethod is a string 	Will pass a sequence pulled from query if sortMethod is callable"""
	if(type(sortMethod) is str):
		if type(query) is QuerySet:
			if reverse:
				sortMethod = '-'+sortMethod
			return query.order_by(sortMethod)
		else:
			return attrSort(query,sortMethod,reverse)
	items = query.all() if type(query) is QuerySet else query
	if(hasattr(sortMethod,'__call__')):
		return sortMethod(items,reverse,category)


def playersByWins(players,reverse,category=None):
	return sorted(players,(lambda x,y:cmp(x.wins(category),y.wins(category))),reverse=reverse)

def playersByLosses(players,reverse,category=None):
	return sorted(players,(lambda x,y:cmp(x.losses(category),y.losses(category))),reverse=reverse)

def playersByWinPct(players,reverse,category=None):
	return sorted(players,(lambda x,y:cmp(x.winPct(category),y.winPct(category))),reverse=reverse)

def playersByModerated(players,reverse,category=None):
	return sorted(players,(lambda x,y:cmp(x.modded(),y.modded())),reverse=reverse)

def modsByLargestGame(mods,reverse,category=None):
	return sorted(mods,(lambda x,y:cmp(x.largestModdedCount(),y.largestModdedCount())),reverse=reverse)

def gamesByLength(games,reverse,category=None):
	return sorted(games,(lambda x,y:cmp(x.length(),y.length())),reverse=reverse)

def gamesByPlayers(games,reverse,category=None):
	return sorted(games,(lambda x,y:cmp(x.num_players(),y.num_players())),reverse=reverse)
def teamsByGame(teams,reverse,category=None):
	return sorted(teams,(lambda x,y:cmp(x.game.title,y.game.title)),reverse=reverse)
def teamsByLength(teams,reverse,category=None):
	return sorted(teams,(lambda x,y:cmp(x.game.length(),y.game.length())),reverse=reverse)
def sequenceByElmnt(elNumb):
	def sortFunc(sequence,reverse,category=None):
		return sorted(sequence,(lambda x,y:cmp(x[elNumb],y[elNumb])),reverse=reverse)
	return sortFunc
