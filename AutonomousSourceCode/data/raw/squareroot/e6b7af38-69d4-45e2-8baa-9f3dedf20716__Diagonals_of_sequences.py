#/usr/bin/env python

# 2010 Giannis Fysakis
# E-mail: giannisfs@gmail.com
# Released subject to the GPL  License
/*
 *      This program is free software; you can redistribute it and/or modify
 *      it under the terms of the GNU General Public License 3 as published by
 *      the Free Software Foundation; 
 *      This program is distributed in the hope that it will be useful,
 *      but WITHOUT ANY WARRANTY; without even the implied warranty of
 *      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *      GNU General Public License for more details.
 *      
 *      You should have received a copy of the GNU General Public License
 *      along with this program; if not, write to the Free Software
 *      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 *      MA 02110-1301, USA.
 *      
 */


from math import sqrt

#4 x 4 Matrix
SquareMatrixof4 = (1,2,3,4,\
                   2,3,5,7,\
                   2,5,7,0,\
                   3,4,5,6)

#5 x 5 Matrix
SquareMatrixof5 =  (1,4,3,4,5,\
                    2,3,4,5,8,\
                    5,6,8,9,6,\
                    1,2,3,4,5,\
                    3,3,4,6,4)
#6 x 6 Matrix
SquareMatrixof6 =  (1,4,3,4,5,7,\
                    2,3,4,5,8,6,\
                    5,6,8,9,6,4,\
                    1,2,3,4,5,3,\
                    3,3,4,6,4,8,\
                    4,5,6,8,7,6)

def isValidSquare(seq):
    """
Any Sequence can be treated as a square as long as
the square root of the number of elements is a positive integer"""
    NumberOfElements = len(seq)
    return sqrt(NumberOfElements).is_integer()



def Diagonal(seq ,Diagonal="Left",X=4):
    diag = []
    LeN = len(seq)
    if Diagonal == "Left":
        pos = 0
        for i in xrange(0,LeN,LeN/X):
            diag.append( seq[ pos + i ] )
            pos += 1
    elif Diagonal == "Right":
        pos = X
        for i in xrange(0,LeN,LeN/X):
            diag.append( seq[ pos - i ] )
            pos  -= 1

    return diag
    
        
        
#examples
##>>> isValidSquare(SquareMatrixof4)
##True
##>>> Diagonal(SquareMatrixof6,X=6)
##[1, 3, 8, 4, 4, 6]
##>>> Diagonal(SquareMatrixof5,X=5)
##[1, 3, 8, 4, 4]
##>>> Diagonal(SquareMatrixof4,X=4)
##[1, 3, 7, 6]
##>>> 
