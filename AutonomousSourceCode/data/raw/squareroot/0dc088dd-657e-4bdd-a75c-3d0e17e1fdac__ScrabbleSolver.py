import copy
import pickle
import re
import sys
import time

from Dawg import Dawg
from sets import Set
from Square import *

global dawg
valueMap = {'A':1, 'B':4, 'C':4, 'D':2, 'E':1, 'F':4, 'G':3, 'H':3, 'I':1, 'J':10, 'K':5, 'L':2, 'M':4, 'N':2, 'O':1, 'P':4, 'Q':10, 'R':1, 'S':1, 'T':1, 'U':2, 'V':5, 'W':4, 'X':8, 'Y':3, 'Z':10, '*':0}
rack = []  #list of tiles
spaceSquareList = []
crossCheckSet = Set()
plays = {}
boardHorizontal = []
boardVertical = []
global adjacentPlacedTileId
bestScore = 0
bestPlay = 'no plays'
global currentBoard

def formatBoard():
  global rack
  rack = re.findall('[a-z]|[*]', sys.argv[1])
  
  boardInput = open('../resources/board.txt').read().split()
  row = []
  for rowInputString in boardInput:
    rowInputList = re.findall('[-]|DW|TW|DL|TL|[a-z]', rowInputString)
    boardHorizontal.append(createRowLinkedList(rowInputList))

  collumn = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]] 
  for rowInputString in boardInput:
    for collumnNum, squareInput in enumerate(re.findall('[-]|DW|TW|DL|TL|[a-z]', rowInputString)):
      collumn[collumnNum].append(squareInput)
  for collumnInputList in collumn:
    boardVertical.append(createRowLinkedList(collumnInputList))
    
def createRowLinkedList(inputList):
  parseSquare(inputList)
  
  rowHead = extendRowRight(inputList)

  return rowHead

def extendRowRight(inputList):
  input = inputList[0]
  square = parseSquare(input)
  
  if len(inputList[1::]) > 0:
    square.nextSquare = extendRowRight(inputList[1::])
    return square
  else:
    endSquare = Square()
    endSquare.tile = '$'
    square.nextSquare = endSquare
    return square

def parseSquare(input):
  square = Square()
  if input == 'DW':
    square.wordBonus = 2
  elif input == 'TW':
    square.wordBonus = 3
  elif input == 'DL':
    square.letterBonus = 2
  elif input == 'TL':
    square.letterBonus = 3
  else:
    square.tile = input
  
  return square

def findWords(row, rowPointer, rowString):
  global adjacentPlacedTileId
  
  row.append(rowPointer)
  rowString += rowPointer.tile
  
  #tiles on the board (k == 0)
  m = re.search('([a-z]+)-$', rowString)
  if m != None:
    adjacentPlacedTileId = row[m.end(1)].id
    partialWord = row[m.start(1):m.end(1)]
    ExtendRight(partialWord, dawg.getNode(m.group(1)), rowPointer)
    
  #adding tiles from rack (k > 0)
  m = re.search('(-*)-[a-z]$', rowString)
  if m != None:
    adjacentPlacedTileId = row[m.end(1)+1].id
    partialWord = row[m.start(1):m.end(1)]
    LeftPart(partialWord, dawg.root, len(m.group(1)), row[m.end(1)])
    
  if rowPointer.nextSquare != None:
    findWords(row, rowPointer.nextSquare, rowString)
  
def LeftPart(partialWord, N, limit, square):
  ExtendRight(partialWord, N, square)
  if limit > 0:
    for Eletter, Enode in N.edges.items():
      if Eletter in rack:
        #insert tile at anchor square (pushing back the current leftPart --LP[])
        rack.remove(Eletter)
        #push LP back to the left one tile to make room for new tile to be placed at anchor square
        shiftLPLeft(partialWord, Eletter)
        LeftPart(partialWord, Enode, limit-1, square)
        #remove tile from anchor space, push LP back to the right
        shiftLPRight(partialWord)
        rack.append(Eletter)

def shiftLPLeft(leftPart, newTile):
  rightTile = newTile
  leftPart.reverse()
  for square in leftPart:
    tempTile = square.tile
    square.tile = rightTile
    rightTile = tempTile
  leftPart.reverse()

def shiftLPRight(leftPart):
  leftTile = '-'
  for square in leftPart:
    tempTile = square.tile
    square.tile = leftTile
    leftTile = tempTile

def ExtendRight(partialWord, N, square):
  if N.final and (square.tile == '-' or square.tile == '$'):
    addLegalMove(partialWord)
  if (square.tile == '-'):
    for Eletter, Enode in N.edges.items():
      if Eletter in rack : #TODO: and (E.letter in crossCheckSet)
        if square.nextSquare != None:
          rack.remove(Eletter)
          square.tile = Eletter
          partialWord.append(square)
          ExtendRight(partialWord, Enode, square.nextSquare)
          partialWord.pop()
          square.tile = '-'
          rack.append(Eletter)
  if re.match("^[a-z]$", square.tile):
    if square.tile in N.edges:
      Enode = N.edges[square.tile]
      if square.nextSquare != None:
        partialWord.append(square)
        ExtendRight(partialWord, Enode, square.nextSquare)
        partialWord.pop()

def addLegalMove(move):
  global adjacentPlacedTileId
  
  for square in move:
    if square.id == adjacentPlacedTileId:
      tallyPoints(move)

def tallyPoints(move):
  global bestScore
  global bestPlay
  
  score = 0
  word = ''
  wordBonus = 1
  for placement in move:
    if (placement.tile != '-' and placement.tile != '$'):
      word += placement.tile
      score += valueMap.get(placement.tile.upper()) * int(float(placement.letterBonus))
      wordBonus = wordBonus * placement.wordBonus
  score = score * wordBonus
  if score >= bestScore:
    bestScore = score
    bestPlay = ''
    for square in currentBoard:
      while square.nextSquare != None:
        bestPlay += '|' + square.tile
        square = square.nextSquare
      bestPlay += '|\n'
  plays[word] = score
#  print word, score

def sortMoves():  
  playList = [x for x in plays.items()]
  playList.sort(key = lambda x: x[0]) # sort by key
  playList.sort(key = lambda x: x[1]) # sort by value
  for word, score in playList:
    print word, score

if __name__ == '__main__':  
  start = time.time()
  dawg = Dawg()
  try:
      dawg = pickle.load(open('../resources/save.p', 'rb'))
  except:
    words = open("enable1.txt", 'rt').read().split()
    words.sort()
    for word in words:
      dawg.insert(word)
    dawg.finish()
    pickle.dump(dawg, open('../resources/save.p', 'wb'))

#  formatSpace() #creates rack, spaceSquareList
  
  formatBoard()
  for rowNum in range(0,15):
    plays = {}
    print '____ROW: ', rowNum
    rowHead = boardHorizontal[rowNum]
    currentBoard = boardHorizontal
    findWords(list(), rowHead, '')
    
  print bestPlay
  print bestScore
#    sortMoves()
  for collumnNum in range(0,15):
    plays = {}
    print '____COL: ', collumnNum
    collumnHead = boardVertical[collumnNum]
    currentBoard = boardVertical
    findWords(list(), collumnHead, '')
#    sortMoves()  
    
  print bestPlay
  print bestScore
  print time.time() - start
