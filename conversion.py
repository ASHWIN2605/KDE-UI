# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 14:12:16 2019

@author: LENOVO
"""


from pyproj import Proj, transform

def reproject_wgs_to_itm(longitude, latitude):
    prj_wgs = Proj(init='epsg:4326')
    prj_itm = Proj(init='epsg:2157') #
    x, y = transform(prj_itm,prj_wgs, longitude, latitude)
    return x, y


#print (reproject_wgs_to_itm(-7.748108, 53.431628))
print (reproject_wgs_to_itm(616739.1657790709, 742421.4589047702))
