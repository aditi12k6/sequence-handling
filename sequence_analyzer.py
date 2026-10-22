#!/usr/bin/env python3
"""Analyze nucleotide sequences from a FASTA file using only Python's standard library."""

import argparse
from collections import Counter
from pathlib import Path

DNA_BASES = set("ACGT")
VALID_IUPAC_DNA = set("ACGTRYSWKMBDHVN")


def read_fasta(file_path):
    """Return a list of (header, sequence) records from a FASTA file."""
    records = []
    header = None
    chunks = []

    try:
        with open(file_path, "r", encoding="utf-8") as handle:
            for line_number, raw_line in enumerate(handle, start=1):
                line = raw_line.strip()
                if not line:
                    continue
                if line.startswith(">"):
                    if header is not None:
                        records.append((header, "".join(chunks).upper()))
                    header = line[1:].strip()
                    if not header:
                        raise ValueError(f"Empty FASTA header on line {line_number}.")
                    chunks = []
                else:
                    if header is None:
                        raise ValueError(
                            f"Sequence data found before the first FASTA header "
                            f"(line {line_number})."
                        )
                    chunks.append("".join(line.split()))

        if header is not None:
            records.append((header, "".join(chunks).upper()))
    except OSError as exc:
        raise ValueError(f"Could not read '{file_path}': {exc}") from exc

    if not records:
        raise ValueError("No FASTA records found. Check that the file contains a header beginning with '>'.")
    for header, sequence in records:
        if not sequence:
            raise ValueError(f"Sequence '{header}' is empty.")
        invalid = sorted(set(sequence) - VALID_IUPAC_DNA)
        if invalid:
            raise ValueError(
                f"Sequence '{header}' contains unsupported characters: {', '.join(invalid)}. "
                "This analyzer expects nucleotide DNA sequences."
            )
    return records


def analyze_sequence(sequence):
    """Calculate length, base counts, GC percentage, and ambiguous-base count."""
    counts = Counter(sequence)
    length = len(sequence)
    gc_count = counts["G"] + counts["C"]
    gc_percent = (gc_count / length * 100) if length else 0.0
    return {
        "length": length,
        "counts": counts,
        "gc_count": gc_count,
        "gc_percent": gc_percent,
        "ambiguous_count": sum(counts[base] for base in sequence if base not in DNA_BASES),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Calculate length, nucleotide composition, and GC content from a DNA FASTA file."
    )
    parser.add_argument("fasta_file", help="Path to the input FASTA file")
    args = parser.parse_args()

    try:
        records = read_fasta(Path(args.fasta_file))
    except ValueError as exc:
        parser.error(str(exc))

    print("DNA FASTA SEQUENCE REPORT")
    print("=" * 30)
    for index, (header, sequence) in enumerate(records, start=1):
        result = analyze_sequence(sequence)
        print(f"\nRecord {index}: {header}")
        print(f"Sequence length: {result['length']} bp")
        print(f"A: {result['counts']['A']}")
        print(f"T: {result['counts']['T']}")
        print(f"G: {result['counts']['G']}")
        print(f"C: {result['counts']['C']}")
        print(f"GC content: {result['gc_percent']:.2f}%")
        print(f"Ambiguous bases: {result['ambiguous_count']}")


if __name__ == "__main__":
    main()
