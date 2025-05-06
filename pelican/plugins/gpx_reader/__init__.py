from pelican import signals as pelican_signals

from .constants import __version__  # NOQA
from .generator import GPXArticleGenerator, GPXGenerator, display_stats, insert_gpx_articles
from .initialize import check_settings
from .reader import GPXReader


def add_gpx_reader(readers):
    readers.reader_classes["gpx"] = GPXReader


def add_gpx_generator(pelican_instance):
    return GPXGenerator

def add_gpx_article_generator(pelican_instance):
    return GPXArticleGenerator


def register():
    """Register the plugin pieces with Pelican."""
    pelican_signals.initialized.connect(check_settings)
    pelican_signals.readers_init.connect(add_gpx_reader)
    pelican_signals.get_generators.connect(add_gpx_generator)
    pelican_signals.all_generators_finalized.connect(insert_gpx_articles)
    # pelican_signals.get_generators.connect(add_gpx_article_generator)
    pelican_signals.finalized.connect(display_stats)
