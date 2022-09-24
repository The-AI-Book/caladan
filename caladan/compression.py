
from osgeo import gdal, gdalconst
import utils
gdal.UseExceptions()

def get_compression_options(compress_format: str = "JPEG", jpeg_quality: str = "80", photometric: str = "YCBCR", tiled: str = "YES") -> gdal.TranslateOptions:
    """Define options for lossy compression for image previews.

    Args:
        - None

    Return:
        - gdal.TranslateOptions

    """
    opts = {
        f"COMPRESS={compress_format}",     # Better lossy compression
        f"JPEG_QUALITY={jpeg_quality}"
        f"PHOTOMETRIC={photometric}", # Better than RGB for human perception
        f"TILED={tiled}"
        # "OUTPUTFORMAT=COG"
    }
    return gdal.TranslateOptions(format="GTiff", 
                                 bandList=[1,2,3], 
                                 outputType=gdalconst.GDT_Byte, 
                                 creationOptions=opts)

def compress_image(input_path: str, output_path: str) -> gdal.Translate:
    """Compress an image using gdal.Translate

    Args:
        - input_path (str)
        - output_path (str)

    Return: 
        - gdal.Translate

    """
    inputfile = utils.read_image(input_path) #gdal.Open(input_path, gdal.GA_ReadOnly)
    opts = get_compression_options()
    dest = gdal.Translate(output_path, inputfile, options=opts)
    return dest