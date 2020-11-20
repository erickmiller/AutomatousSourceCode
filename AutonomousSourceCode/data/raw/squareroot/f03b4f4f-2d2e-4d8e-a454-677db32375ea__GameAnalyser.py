import Teams
import CheckerType
import TreeNode


def get_possible_moves(state, team):
	moves = []

	for checker in state.get_team_checkers(team):
		root = TreeNode.TreeNode([checker.location, True])
		_build_siblings(root, state, checker.team, checker.type, [])
		moves.append([checker.location, root])

	return moves


def _build_siblings(node, state, team, type, temp_deleted = []):
	moves = _find_moves(state=state, location=node.data[0], team=team , type=type, temp_deleted=temp_deleted)


	for move in moves[0]:
		if moves[1]:
			deleted = _find_deleted(move, node.data[0])
			temp_deleted.append(deleted)


		node.siblings.append(TreeNode.TreeNode([move, moves[1]]))

	for sib in node.siblings:
		if not sib.data[1]:
			continue
		_build_siblings(sib, state, team, type, temp_deleted)


def _find_moves(state, location, team, type, temp_deleted = []):
	direction = Teams.direction(team)
	if type == CheckerType.king():
		direction = 0

	empty_moves = []
	take_moves = []

	enemy = Teams.opposite(team)
	diagonals = _get_diagonals(location, direction)

	for square in diagonals:
		new_checker = state.get_checker_from_location(tuple(square))

		if new_checker == None or new_checker.location in temp_deleted:
			empty_moves.append(square)
			continue
		elif new_checker.team == enemy:
			dx = square[0] - location[0]
			dy = square[1] - location[1]

			new_square = (square[0] + dx, square[1] + dy)

			if not _valid_square(new_square):
				continue
			if state.get_checker_from_location(new_square) == None:
				take_moves.append(new_square)

	if not len(take_moves) == 0:
		return take_moves, True
	return empty_moves, False


def _get_diagonals(square, y_restrict):
	# y_restrict: -1 implies that y can only decrease from that given in square [max 2 diagonals]
	# 			   0 that y can increase and decrease [max 4 diagonals]
	#			   1 that y can increase [max 2 diagonals]

	coords = []

	c1 = [square[0] + 1, square[1] + 1]
	c2 = [square[0] - 1, square[1] + 1]

	c3 = [square[0] + 1, square[1] - 1]
	c4 = [square[0] - 1, square[1] - 1]

	if _valid_square(c1) and y_restrict >= 0:
		coords.append(c1)
	if _valid_square(c2) and y_restrict >= 0:
		coords.append(c2)
	if _valid_square(c3) and y_restrict <= 0:
		coords.append(c3)
	if _valid_square(c4) and y_restrict <= 0:
		coords.append(c4)

	return coords


def _valid_square(square):
	if square[0] < 0 or square[1] < 0:
		return False

	if square[0] > 7 or square[1] > 7:
		return False

	return True


def check_move_is_valid(moves, state, team):
	if len(moves) < 2:
		raise ValueError('Argument moves must have more than one item')

	possible_moves = get_possible_moves(state, team)
	current_node = None

	for move in possible_moves:
		if move[0] == moves[0]:
			current_node = move[1]
	if current_node == None:
		return False

	return _find_route(current_node, moves[1:])


def _find_route(start_node, values):
	current_level = 0
	current_node = start_node
	found_no_take = False
	deleted = []

	for val in values:
		current_level += 1

		sib = _find_sibling(current_node, val)
		if sib == None:
			return False

		if found_no_take:
			return False

		if not sib.data[1]:
			found_no_take = True
		else:
			# Figure out which piece has been taken
			start = current_node.data[0]
			end = sib.data[0]

			deleted.append(_find_deleted(start, end))

		current_node = sib

	return deleted

def _find_deleted(start, end):
	x = start[0] + ((end[0] - start[0]) / 2)
	y = start[1] + ((end[1] - start[1]) / 2)

	return (x, y)


def _find_sibling(node, value):
	for sib in node.siblings:
		if list(sib.data[0]) == list(value):
			return sib

	return None