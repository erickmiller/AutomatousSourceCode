#!/usr/bin/python
# Filename: chessboard.py
# -*- coding: utf-8 -*-

from Tkinter import *
import tkFont
import numpy as np
from string import maketrans
import time

class FICS(object):       
        pass
class ChessBoard(FICS):
        def __init__(self, data):
            self._data = data
        def create_chessboard(self):
            self.root = Tk() 
            self.square_size = 90
            self.font_size = self.square_size+2
            self.chessboard = Canvas(self.root,
                                     width=self.square_size*8,
                                     height=self.square_size*8)
            self.update_chessboard(self._data) # Draw the chessboard
            self.chessboard.pack()
            self.board_exist = True
        def update_chessboard(self, data):
            data = data[::-1]
            in_table = 'prnbqkx-RNBQKPX'          
            out_table ='prnbqkx tmvwloX'
            tran_table = maketrans(in_table, out_table)
            pieces = converted_data = list(data.translate(tran_table, ' <12>'))
            col = False,True
            colour_square = ( (col[0],col[1])* 4 + (col[1],col[0])*4 )*4
            file_board = [('a',0),('b',1),('c',2),('d',3),('e',4),
                          ('f',5),('g',6),('h',7),]
            rank_board = [('8',7),('7',6),('6',5),('5',4),('4',3),('3',2),
                          ('2',1),('1',0),]
            pieces=''
            for x,y in zip(colour_square,converted_data):
                    if x and y!=chr(32):
                        pieces = pieces+(y.upper())
                    elif x and y==chr(32):
                        pieces = pieces+('+')
                    else:
                        pieces = pieces+y
            # Create the master data list
            square = list(
                           [(7*self.square_size-x[1]*self.square_size,
                            y[1]*self.square_size,
                            x[0]+y[0],
                            pieces[(y[1]*8)+x[1]],)
                            for y in rank_board for x in file_board]
                         )
            self.chessboard.delete(ALL)
            for x in square:
                    self.output = self.chessboard.create_text(x[0]+self.square_size/2,
                                                              x[1]+self.square_size/2,
                                                              fill='black', font=('Chess Cases',
                                                               self.font_size,
                                                               'normal'))     
                    self.chessboard.itemconfig(self.output, text=x[3])
            self.chessboard.update_idletasks()
            return

        def show_bb(self, data):
        ''' Dev version shows a bitboard when testing.'''
        
                if data.type is not str:
                        result= np.binary_repr(data, 68)[::-1]
                else:
                        result = data
                print result[56:64]
                print result[48:56]
                print result[40:48]
                print result[32:40]
                print result[24:32]
                print result[16:24]
                print result[8:16]
                print result[0:8]
