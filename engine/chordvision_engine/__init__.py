"""ChordVision chord-recognition engine.

A self-contained chord detection engine. No external chord-recognition
API is used anywhere: every chord returned by this package is derived
from direct spectral analysis of the audio signal.

Pipeline
--------
    audio file  ->  PCM (ffmpeg)
                ->  Constant-Q Transform  (own implementation)
                ->  tuning estimation + correction
                ->  chromagram (harmonic pitch class profile)
                ->  chord template matching
                ->  HMM / Viterbi sequence decoding
                ->  segmentation + bass detection + key estimation
                ->  ChordEvent list with confidence + alternatives
"""

__version__ = "1.0.0"

from .types import ChordEvent, KeyEstimate, AnalysisResult, Segment
from .analyze import analyze_file, analyze_samples, ChordEngine

__all__ = [
    "ChordEvent",
    "KeyEstimate",
    "AnalysisResult",
    "Segment",
    "analyze_file",
    "analyze_samples",
    "ChordEngine",
    "__version__",
]
