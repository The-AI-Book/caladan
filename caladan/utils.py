import os, random
from osgeo import gdal
gdal.UseExceptions()

RANDOM_COORDS = [[32.149989, -110.835842], [27.380583, 33.631839], [32.676373, -117.157741], 
          [-4.289077, 31.396238], [33.747252, -112.633853], [-33.836379, 151.080506], 
          [50.010611, -110.113422], [33.927911, -118.380690], [45.123853, -123.113603],
          [-33.867886, -63.987000], [41.303921, -81.901693], [40.452107, 93.742118],
          [37.563936, -116.851230], [-33.350534, -71.653268], [43.645074, -115.993081],
          [51.848637, -0.554620], [35.282902, 33.376891], [38.483378, -109.681333],
          [37.629562, -116.849556]]
          
def read_image(image_path : str) -> gdal.Dataset:
    """This functions returns and gdal.Dataset based on a file path.
    
    Args:
        - path (str)

    Return:
        - gdal.Dataset
    
    """
    _, file_extension = os.path.splitext(image_path)
    print("file extension: ", file_extension)
    extensions_accepted = ['.tif', '.jp2', '.img']
    if file_extension in extensions_accepted:
        image = gdal.Open(image_path)
        print("open image")
        return image
    formats = ", ".join(extensions_accepted)
    raise Exception(f"Image format is not valid, accepted extensions are {formats}")

def generate_random_latlong() -> tuple:
    """This function generate random latitude and longitude coordinates
    Range from -90 to 90 for latitude and -180 to 180 for longitude.

    Args:
        - None

    Return:
        - tuple (float, float)
    
    """
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return latitude, longitude

def change_image_coordinates(image: gdal.Dataset, funny = True) -> gdal.Dataset:
    """This function change the coordinates of the image.
    
    Args:
        - image (gdal.Dataset)
        - funny (bool: optional): If True, new coordinates are set to funny 
                                  places found in Google maps.
        
    Return:
        - gdal.Dataset
    
    """
    image = read_image(image_path = image_path)
    wgs84_wkt = """
        GEOGCS["WGS 84",
        DATUM["WGS_1984",
            SPHEROID["WGS 84",6378137,298.257223563,
                AUTHORITY["EPSG","7030"]],
            AUTHORITY["EPSG","6326"]],
        PRIMEM["Greenwich",0,
            AUTHORITY["EPSG","8901"]],
        UNIT["degree",0.01745329251994328,
            AUTHORITY["EPSG","9122"]],
        AUTHORITY["EPSG","4326"]]
    """
    image.SetProjection(wgs84_wkt)
    gt = image.GetGeoTransform()
    if funny:
        latlong = RANDOM_COORDS[random.randrange(len(RANDOM_COORDS))]
    else:
        latlong = generate_random_latlong()

    latitude = latlong[0]
    longitude = latlong[1]
    
    trf = [longitude, gt[1], gt[2], latitude, gt[4], gt[5]]
    image.SetGeoTransform(trf)
    image.FlushCache() #Saves to disk 
    return image