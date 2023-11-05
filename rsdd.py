import requests
import os

def download_remote_sensing_data(source, dataset, output_file, start_date, end_date, location_extent):
  """Downloads remote sensing data from a given source and dataset, for a given start date, end date, and location extent.

  Args:
    source: The name of the remote sensing data source.
    dataset: The name of the remote sensing dataset.
    output_file: The path to the output file where the data will be downloaded.
    start_date: The start date of the data to download.
    end_date: The end date of the data to download.
    location_extent: The location extent of the data to download.
  """

  if source == 1:
    url = "https://earthexplorer.usgs.gov/api/v1/download?dataset={}&startdate={}&enddate={}&bbox={}".format(dataset, start_date, end_date, location_extent)
  elif source == 2:
    url = "https://search.earthdata.nasa.gov/es/search?q=dataset:{}&provider=NASA&startdate={}&enddate={}&location={}".format(dataset, start_date, end_date, location_extent)
  elif source == 3:
    url = "https://scihub.copernicus.eu/dhus/#/home"
  elif source == 4:
    url = "https://www.class.noaa.gov/saa/products/search?platform=GOES-16&satellite=GOES-16&instrument=ABI&product=GeoColor&startTime={}&endTime={}".format(start_date, end_date)
  elif source == 5:
    url = "https://glovis.usgs.gov/#layers"
  elif source == 6:
    url = "https://data.nal.usda.gov/dataset/national-agricultural-imagery-program-naip/resource/a36a7107-f83f-4e87-92d8-d45405364621"
  elif source == 7:
    url = "https://data.nasa.gov/JPL/MODIS"
  elif source == 8:
    url = "https://data.esa.int/en/sentinel/user-guides/sentinel-1-sar/products"
  elif source == 9:
    url = "https://data.noaa.gov/dataset/noaa-cdr-dataset"
  elif source == 10:
    url = "https://www.wri.org/gfw/map/forests"
  elif source == 11:
    url = "https://data.glcf.umd.edu/data/lc/glcf_global_land_cover_2000.php"
  elif source == 12:
    url = "https://opentopography.org/data"
  else:
    raise NotImplementedError("Unsupported remote sensing data source: {}".format(source))

  response = requests.get(url, stream=True)

  with open(output_file, "wb") as f:
    for chunk in response.iter_content(chunk_size=1024):
      f.write(chunk)

if __name__ == "__main__":
  # Get the remote sensing data source from the user.
  source = int(input("Enter the number of the remote sensing data source:\n1. USGS EarthExplorer\n2. NASA Earthdata Search\n3. ESA's Copernicus Data Space\n4. NOAA CLASS\n5. GloVis\n6. USDA NAIP\n7. NASA JPL MODIS\n8. ESA Sentinel-1 SAR\n9. NOAA CDR\n10. WRI Global Forest Watch\n11. GLCF Global Land Cover\n12. OpenTopography\n"))

  # Get the remote sensing dataset from the user.
  dataset = input("Enter the remote sensing dataset: ")

  # Get the start date from the user.
  start_date = input("Enter the start date (YYYY-MM-DD): ")

  # Get the end date from the user.
  end_date = input("Enter the end date (YYYY-MM-DD): ")

# Get the location extent from the user.
location_extent = input("Enter the location extent (bounding box or shapefile): ")

# Download the remote sensing data.
download_remote_sensing_data(source, dataset, output_file, start_date, end_date, location_extent)

# Print a message to the user.
print("Remote sensing data downloaded successfully to {}.".format(output_file))

