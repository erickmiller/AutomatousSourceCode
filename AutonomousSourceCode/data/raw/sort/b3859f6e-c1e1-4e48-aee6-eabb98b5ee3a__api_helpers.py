# -*- coding: utf-8 -*-
from models.models import db, Location, FunRun, Theme, Challenge
import re

def filter_query_parameters(allowed_parameters, request_parameters):
	filtered_parameters = {}
	for k in allowed_parameters:
		if k in request_parameters:
			filtered_parameters[k] = request_parameters[k]
	return filtered_parameters

def select(table, predicate):
	return filter(predicate, table)

def isInt(inp):
	try:
		int(inp)
		return True
	except ValueError:
		return False

def isFloat(inp):
	try:
		float(inp)
		return True
	except ValueError:
		return False

def isNumber(inp):
	return isInt(inp) or isFloat(inp)

def retrieve_entry_points():
	root_urls = {
              		"funruns_url": "/funruns",
                	"themes_url": "/themes",
                	"challenges_url": "/challenges",
                	"locations_url": "/locations"
            	}
	return root_urls

def retrieve_funruns():
	return db.session.query(FunRun).order_by(FunRun.id)

def retrieve_themes():
	return db.session.query(Theme).order_by(Theme.id)

def retrieve_challenges():
	return db.session.query(Challenge).order_by(Challenge.id)

def retrieve_locations():
	return db.session.query(Location).order_by(Location.id)

def split_sort_string(sort_string):
	# Sort string is of format 'field:[asc or desc]'
	strings = re.split(':', sort_string)
	if len(strings) < 2:
		strings += ['']	
	return (strings[0], strings[1])

def is_sort_descending(sort_order):
	return sort_order == 'desc'

# MOVE SORTING FUNCTIONS TO MDOELS.PY
def sort_funruns(funruns, sort_string):
	sort_field, sort_order = split_sort_string(sort_string)

	if sort_field == 'name':
		return sorted(funruns, key=lambda funrun:funrun.name, reverse=is_sort_descending(sort_order))
	elif sort_field == 'date':
		return sorted(funruns, key=lambda funrun:funrun.get_date_object(), reverse=is_sort_descending(sort_order))
	elif sort_field == 'distance':
		if is_sort_descending(sort_order):
			return sorted(funruns, key=lambda funrun:max(funrun.get_lengths()), reverse=is_sort_descending(sort_order))
		else:
			return sorted(funruns, key=lambda funrun:min(funrun.get_lengths()), reverse=is_sort_descending(sort_order))
	elif sort_field == 'price':
		if is_sort_descending(sort_order):
			return sorted(funruns, key=lambda funrun:max(funrun.get_prices()), reverse=is_sort_descending(sort_order))
		else:
			return sorted(funruns, key=lambda funrun:min(funrun.get_prices()), reverse=is_sort_descending(sort_order))
	elif sort_field == 'number_of_themes':
		return sorted(funruns, key=lambda funrun:len(funrun.funRun_theme), reverse=is_sort_descending(sort_order))
	elif sort_field == 'number_of_challenges':
		return sorted(funruns, key=lambda funrun:len(funrun.funRun_challenge), reverse=is_sort_descending(sort_order))
	else:
		return funruns

def sort_themes(themes, sort_string):
	sort_field, sort_order = split_sort_string(sort_string)

	if sort_field == 'name':
		return sorted(themes, key=lambda theme:theme.name, reverse=is_sort_descending(sort_order))
	elif sort_field == 'number_of_runs':
		return sorted(themes, key=lambda theme:len(theme.funruns), reverse=is_sort_descending(sort_order))
	elif sort_field == 'number_of_challenges':
		return sorted(themes, key=lambda theme:len(theme.theme_challenge), reverse=is_sort_descending(sort_order))
	else:
		return themes

def sort_challenges(challenges, sort_string):
	sort_field, sort_order = split_sort_string(sort_string)

	if sort_field == 'name':
		return sorted(challenges, key=lambda challenge:challenge.name, reverse=is_sort_descending(sort_order))
	elif sort_field == 'difficulty':
		return sorted(challenges, key=lambda challenge:challenge.difficulty, reverse=is_sort_descending(sort_order))
	elif sort_field == 'number_of_runs':
		return sorted(challenges, key=lambda challenge:len(challenge.funruns), reverse=is_sort_descending(sort_order))
	elif sort_field == 'number_of_themes':
		return sorted(challenges, key=lambda challenge:len(challenge.theme), reverse=is_sort_descending(sort_order))
	else:
		return challenges

def sort_locations(locations, sort_string):
	sort_field, sort_order = split_sort_string(sort_string)

	seasons = {'winter', 'spring', 'summer', 'fall'}

	if sort_field == 'name':
		return sorted(locations, key=lambda location:location.name, reverse=is_sort_descending(sort_order))
	elif sort_field.endswith('_avgTemp'):
		if sort_field[:-len('_avgTemp')] in seasons:
			return sorted(locations, key=lambda location:getattr(location, sort_field), reverse=is_sort_descending(sort_order))
	elif sort_field.endswith('_avgHumidity'):
		if sort_field[:-len('_avgHumidity')] in seasons:
			return sorted(locations, key=lambda location:getattr(location, sort_field), reverse=is_sort_descending(sort_order))
	elif sort_field == 'altitude':
		return sorted(locations, key=lambda location:location.get_altitude_as_integer(), reverse=is_sort_descending(sort_order))
	elif sort_field == 'annual_rainfall':
		return sorted(locations, key=lambda location:location.get_annual_rainfall_as_integer(), reverse=is_sort_descending(sort_order))
	else:
		return locations
