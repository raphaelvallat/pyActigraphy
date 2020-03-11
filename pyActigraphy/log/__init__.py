"""Classes for log files (Dairy, Start-Stop files, etc)"""

# Authors: Grégory Hammad <gregory.hammad@uliege.be>
#
# License: BSD (3-clause)

# from . import filters
from .sstlog import SSTLog

from .sstlog import read_sst_log

__all__ = ["SSTLog", "read_sst_log"]
