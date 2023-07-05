#!/usr/bin/env python
"""Top-level module for mir_eval."""

# Import all submodules (for each task)
from . import (alignment, beat, chord, hierarchy, io, key, melody, multipitch,
               onset, pattern, segment, separation, sonify, tempo,
               transcription, transcription_velocity, util)

__version__ = '0.7'
