"""RAG-Anything: A multimodal RAG framework that handles any type of document.

This package provides tools for parsing, indexing, and querying documents
containing text, images, tables, equations, and other modalities using
Retrieval-Augmented Generation (RAG) techniques.
"""

from raganything.raganything import RAGAnything
from raganything.modalprocessors import (
    ImageProcessor,
    TableProcessor,
    EquationProcessor,
    GeneralProcessor,
)

__version__ = "0.1.0"
__author__ = "HKUDS"
__license__ = "MIT"

__all__ = [
    "RAGAnything",
    "ImageProcessor",
    "TableProcessor",
    "EquationProcessor",
    "GeneralProcessor",
]
