GPX Reader for Pelican
======================

To build, clone `heatmap <https://github.com/sethoscope/heatmap>_` to a
parallel directory (under the same root as this project) and then vendorize
(with ``invoke vendorize``).::

    cd ..
    git clone https://github.com/sethoscope/heatmap
    cd minchin.pelican.readers.gpx
    invoke vendorize
