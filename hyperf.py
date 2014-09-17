#!/usr/bin/python
# -*- coding: utf-8 -*-
###############################################################
# Program: HYPERF
# By: Urban Anjar, urban.anjar@gmail.com
# Copyleft, all rights reversed
# Calculates Hyperfocal Distance
# Version 0.1  2012-03-28
#         0.11 2012-09-17
############## Put in your own values here ####################
c = 0.030 #Circle of confusion (mm)
#for Nikon consumer DSLR and most other DSLR c=0.020
#for Canon consumer DSLR c=0.019
#for pro DSLR like Canon 5D, Leica M9 and Nikon D3s c=0.030
#for other cameras see http://www.dofmaster.com/digital_coc.html
f = [20, 28, 50, 85] # focal lengths
N = [22, 16, 11, 8, 5.6, 4, 2.8, 2, 1.8] #f-stops
###############################################################

def main():
    print "HYPERF by Urban Anjar"
    print "Circle of Confusion:",c
    print "Hyperfocal distance at different focal lengths and apertures\n"
    print "  f/\t|  f = \t",
    for flength in f:
        print flength,"\t",
    print "\n",
    print "-"*61
        
    for fstop in N:
        print " ", fstop, "\t|\t",
        
        for flength in f:
            print hyperfocal(flength, fstop),"\t",
        print "\n"


def hyperfocal(f,N): #calculate hyperfocal distance
    H= ((f**2) / (N*c)) + f 
    return round((H /1000), 2) ## in meter, 2 positions

   
#call main if running this module
if __name__ == '__main__': 
    main()
