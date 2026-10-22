# DNA Sequence Analyzer

A beginner-friendly bioinformatics project that reads DNA sequences in FASTA format and reports sequence length, nucleotide composition, GC content, and ambiguous-base count.

## Features

- Reads one or more DNA sequences from a FASTA file.
- Handles sequences split across multiple lines and lowercase letters.
- Counts A, T, G, and C bases.
- Calculates GC content as `(G + C) / sequence length × 100`.
- Reports ambiguous IUPAC nucleotide symbols separately.
- Displays helpful errors for malformed files or unsupported characters.
- Uses only Python's standard library.

## Requirements

- Python 3.9 or later
- No additional packages

## Files

- `sequence_analyzer.py` — main program
- `sample.fasta` — example input containing two DNA sequences
- `requirements.txt` — dependency note

## Run the project

Open a terminal in this folder and run:

```bash
python sequence_analyzer.py sample.fasta
```

On some systems, use `python3` instead of `python`.

To analyze another FASTA file:

```bash
python sequence_analyzer.py path/to/your_file.fasta
```

FASTA files use a header line that starts with `>` followed by one or more lines of sequence.

## Example output

```text
DNA FASTA SEQUENCE REPORT
==============================

Record 1: sample_dna_sequence
Sequence length: 24 bp
A: 6
T: 6
G: 7
C: 5
GC content: 50.00%
Ambiguous bases: 0

Record 2: sample_dna_sequence_with_ambiguity
Sequence length: 15 bp
A: 3
T: 3
G: 4
C: 3
GC content: 46.67%
Ambiguous bases: 4
```

## Method

1. Parse the FASTA header and sequence lines.
2. Convert the sequence to uppercase.
3. Count nucleotide symbols.
4. Calculate GC content using the total sequence length.
5. Print a report for each sequence record.

GC content uses the full sequence length as the denominator, including ambiguous symbols such as `N`. Ambiguous symbols are counted separately because they do not identify a single nucleotide.

## Limitations

This program is intended for DNA nucleotide FASTA files, not protein FASTA files. It validates common IUPAC DNA symbols but does not verify that a sequence belongs to a particular organism or gene.

## Possible improvements

- Add CSV report export.
- Add RNA sequence support.
- Add unit tests.
- Retrieve a real public sequence from NCBI and cite its accession number.

## Author

Add your name, course, and institution here before submission.
