GPX Reader for Pelican
======================

Settings
--------

Set these in your ``pelicanconf.py`` file.

(See ``constants.py``)

GPX_AUTHOR
GPX_STATUS
GPX_CATEGORY
GPX_DEV_URL
GPX_VERSION
GPX_SAVE_AS
GPX_URL
GPX_HEATMAPS
GPX_PATHS
GPX_EXCLUDES
GPX_SIMPLIFY_DISTANCE

(and more)



"Article" Metadata
------------------

Each GPX file is turned into a Pelican Article. In addition to the "regular"
metadata, several gpx-specific metadata keys are set. Several of these keys are
repeated for each defined ``heatmap``:

title
  set to the source filename
category
  set to ``GPX_CATEGORY``
date
  set to the file's start time
author
  set to ``GPX_AUTHOR``
slug
  set to the source filename, *sans* file extension (and slightly "slug-ified")
save_as
  c.f. ``GPX_SAVE_AS``
url
  c.f. ``GPX_URL``
gpx
  set to ``True``. Useful if you want to be able to tell in your theme if
  you're dealing with a GPX "Article".
gpx_start_time
  Tme when the data in the GPX files starts
gpx_end_time
  Time when the data in the GPX file ends
gpx_min_elevation
  Minimum elevation in the GPX file
gpx_max_elevation
  Maximum elevation in the GPX file
gpx_min_latitude
gpx_min_longitude
gpx_max_latitude
gpx_max_longitude
  The geographic bounds of the GPX file
gpx_tracks
  Count of how many "tracks" were defined in the GPX file
gpx_segments
  Count of how many "segments" were defined in the GPX file
gpx_points
  Count of how many recorded points were defined in the GPX file
gpx_length_km
  Length of the recorded path, in kilometers
valid
  ``True`` or ``False``. Generally, invalid files are ignored for output.
gpx_{heatmap}_image
  path to the generated travel map
gpx_{heatmap}_trimmed
  The trimmed gpx file (in memory), only containing the points within the
  heatmap's bounding box 
gpx_{heatmap}_save_as
  The filename of the trimmed gpx file as saved to disk
gpx_{heatmap}_hash
  A hash of the resulting GPX file. This allows images to be reused.

Development Notes
-----------------

To build, clone `heatmap <https://github.com/sethoscope/heatmap>_` to a
parallel directory (under the same root as this project) and then vendorize
(with ``invoke vendorize``).::

    cd ..
    git clone https://github.com/sethoscope/heatmap
    cd minchin.pelican.readers.gpx
    invoke vendorize
