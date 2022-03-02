###Description: Displays to map a pointfile, selects out data and exports seperate point based on selection

layer_path = "/home/turkey/Desktop/GISdata/Data/shootings.shp"
#Defines layer path to file to be selected from
layer_name = "shootings"
#define layer name
vlayer = QgsVectorLayer(layer_path, layer_name, "ogr")
#Use QgsVectorLayer to load and define layer_name
QgsProject.instance().addMapLayer(vlayer)
# adds vlayer to map
layer = iface.activeLayer()
#use iface to select elements from map layers
layer.selectByExpression('"fatal" = 0')
#select out data by SQl expression
fn = '/home/turkey/Desktop/GISdata/Data/shootingWounded.shp'
#file path for new shapefile. Last /isFileName.shp
writer = QgsVectorFileWriter.writeAsVectorFormat(layer, fn, 'utf-8', driverName= 'ESRI Shapefile', onlySelected=True)
selected_layer = iface.addVectorLayer(fn,' ','ogr')
# creates a writer type vector (layer name, file name, encoding, driver name is file type, only selected T/F)
del(writer)
#cleans up writer

