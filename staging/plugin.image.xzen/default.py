﻿# *  This Program is free software; you can redistribute it and/or modify
# *  it under the terms of the GNU General Public License as published by
# *  the Free Software Foundation; either version 2, or (at your option)
# *  any later version.
# *
# *  This Program is distributed in the hope that it will be useful,
# *  but WITHOUT ANY WARRANTY; without even the implied warranty of
# *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# *  GNU General Public License for more details.
# *
# *  You should have received a copy of the GNU General Public License
# *  along with XBMC; see the file COPYING. If not, write to
# *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
# *  http://www.gnu.org/copyleft/gpl.html
# *

#imports
import xbmc
import xbmcplugin
import xbmcgui
from time import time
from pprint import pprint
#some handy stuff
from b808common import *
#uses zenapi by Scott Gorling (http://www.scottgorlin.com)
from zenapi import ZenConnection
from zenapi.snapshots import Group, PhotoSet

def buildRootMenu(zen):

    #load the album hierchy for the user
    h = zen.LoadGroupHierarchy()
    for element in h.Elements:
      if isinstance(element,PhotoSet):
        log(str(element.AccessDescriptor))
        idTitle = element.TitlePhoto
        titlePhoto = zen.LoadPhoto(idTitle)
        uTitle = titlePhoto.getUrl(2)
        u=sys.argv[0]+"?mode=1&galleryid=" + str(element.Id)
        item=xbmcgui.ListItem(element.Title,u,'',uTitle,'')
        xbmcplugin.addDirectoryItem(THIS_PLUGIN,u,item,True,len(h.Elements))

def buildGallery(zen,galleryid):

    ps = zen.LoadPhotoSet(galleryid, includePhotos=True)
    for photo in ps.Photos:
      #log(photo.Id)
      u = photo.getUrl(6)
      uThumb = photo.getUrl(10)
      item=xbmcgui.ListItem(photo.Title,u,'',uThumb,'')
      xbmcplugin.addDirectoryItem(THIS_PLUGIN,u,item,False)


#ok we're firing up
footprints()

#get the settings & parameters
username=ADDON.getSetting('username')
password=ADDON.getSetting('password')
params=get_params()
log("Parameters parsed: " + str(params))


#MENU MODES
ROOT = 0
GALLERY = 1

#zero out data between passes
mode = None
url = None
galleryid=None

#try and get data from the paramters
try:
    url=urllib.unquote_plus(params["url"])
except:
    pass

try:
    galleryid=int(params["galleryid"])
except:
    pass

try:
    mode=int(params["mode"])
except:
    pass


#connect to ZenFolio
zen = ZenConnection(username = username, password = password)
if zen is None:
  notify("Couldn't connect to Zenfolio!!")
  sys.exit()
zen.Authenticate()

#OK the mode variable controls what we're actually doing...
if mode==None or mode==ROOT:
  log( "XZen Root Menu" )
  try:
      buildRootMenu(zen)
  except:
      print_exc()

elif mode==GALLERY:
  log( "XZen Gallery id: " + str (galleryid) )
  try:
      buildGallery(zen,galleryid)
  except:
      print_exc()

else:
  notify("Something went wrong - which mode??")
  sys.exit()

#and tell XBMC we're done...
xbmcplugin.endOfDirectory(THIS_PLUGIN)

#and power this puppy down....
footprints(startup=False)

