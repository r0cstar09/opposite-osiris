---
title: "Evidence Hasher – Forensic File Integrity Tool (Usage Guide)"
publishDate: 2025-02-18
img: /assets/evidence_hasher.png
img_alt: "Digital hashing and file-integrity visualization"
description: |
  A comprehensive guide explaining how to use the Evidence Hasher: a Python-based forensic tool
  for generating authenticated SHA-256 manifests to support digital investigations, legal workflows,
  and cybersecurity evidence handling.
tags:
  - Python
  - Forensics
  - File Integrity
  - Evidence Handling
  - Security Automation
---

## Introduction

The **Evidence Hasher** is a platform-agnostic Python utility designed to generate tamper-evident,
cryptographically verifiable SHA-256 manifests for any folder of evidence. It is built for
investigators, cybersecurity analysts, auditors, and legal professionals who need a reliable and
repeatable method to prove that files have **not** been altered after collection.

This guide explains **exactly** how to use the tool, why it is important, and how it fits into
modern forensic and legal workflows.

---

## Why This Tool Matters

Digital evidence must be handled in a way that ensures:

- **Immutability**  
- **Chain of custody**  
- **Integrity verification**  
- **Reproducibility**  
- **Auditability**

Even a small change—such as opening a file in the wrong application—can alter metadata or timestamps.

The Evidence Hasher prevents this by producing a manifest that proves:

- what files existed  
- their exact byte-level fingerprint (SHA-256)  
- when they were created  
- when they were modified  
- their size  
- their path within the collection  

This is essential for:

- legal evidence submissions  
- human rights documentation  
- internal investigations  
- cybersecurity incident response  
- corporate audits  
- forensics reporting  

---

## What the Tool Produces

Running the Evidence Hasher creates a `manifest.csv` file containing:

| Field | Description |
|-------|-------------|
| relative_path | File location inside the evidence folder |
| filename | Name of the file |
| extension | File extension (e.g., .pdf, .png) |
| mime | Detected MIME type |
| size_bytes | File size |
| created | OS-reported created timestamp |
| modified | OS-reported modified timestamp |
| sha256 / sha1 / md5 | Cryptographic hashes |

This CSV can be imported into Excel, stored in an archive, or attached to court filings.

---

## Folder Setup

Organize your evidence folder like this:

/evidence-folder
├── 01-email-thread.pdf
├── 02-screenshot.png
├── audio-recording.m4a
├── chat-log.docx
├── evidence_hasher.py

Place the script in the same folder (or one level above).

---

## Running the Evidence Hasher

### 1. Open a Terminal

- macOS: Terminal  
- Windows: PowerShell  
- Linux: Any shell  
- iPad: GitHub Codespaces terminal  

### 2. Navigate to Your Evidence Folder

```bash
cd path/to/evidence-folder
```

### 3. Run the Basic Command

```bash
python3 evidence_hasher.py -r
```
Windows alternative:

```powershell
python evidence_hasher.py -r
```

This command performs a recursive scan of all files in the directory, hashes them safely, and generates a new file called:

```bash
manifest.csv
```

A successful run will show:

```bash
Wrote XX row(s) to manifest.csv
```

### Viewing the Output Manifest

Open manifest.csv in Excel, Numbers, LibreOffice, or any forensic tool.
Each row describes one file from your evidence set, including:
	•	filename
	•	extension
	•	MIME type
	•	file size
	•	created timestamp
	•	modified timestamp
	•	SHA-256 hash (and optional SHA-1 / MD5)
	•	relative path inside the case folder

Example entry:

```bash
screenshot1.png,screenshot1.png,.png,image/png,190284,2025-02-17T12:44:03,2025-02-17T12:44:03,ba59...
```

Matching hashes in future runs will confirm that the file has not been modified.

### Optional Features

#### ✅ Include SHA-1 and MD5 for Compatibility

```bash
python3 evidence_hasher.py -r --all-hashes
```

This captures .hidden folders, system files, and other OS-level artifacts.

#### ✅ Exclude Certain Patterns:

```bash
python3 evidence_hasher.py -r --exclude "*.tmp" --exclude ".DS_Store"
```

This allows you to skip:
	•	temp files
	•	cache files
	•	OS clutter
	•	backups

#### ✅ Follow Symlinks

```bash
python3 evidence_hasher.py -r --follow-symlinks
```

Adds support for scanning linked directories or mirrored storage.

#### ✅ Preview Files Before Hashing (Dry Run)

```bash
python3 evidence_hasher.py -r --dry-run
```

This prints the list of files that would be included without actually hashing them.

### Verifying Evidence Integrity (Chain-of-Custody)

The most critical feature of the Evidence Hasher is its ability to confirm that your files have not changed since the manifest was generated.

#### To verify a manifest:

```bash
python3 evidence_hasher.py --verify manifest.csv .
```

Output will resemble:

```bash
Verified: 12 file(s)
Mismatched: 0
Missing:
  (none)
```

Meaning:
	•	Verified → All files match their original SHA-256 fingerprint
	•	Mismatched → One or more files were altered
	•	Missing → Files listed in the manifest no longer exist

This step is essential before submitting evidence for legal review, audits, or IR reports.

#### Hashing a Single File

If you only need the SHA-256 hash of one file:

```bash
python3 evidence_hasher.py --hash-only important.pdf
```

Output:

```bash
important.pdf,sha256,<digest>
```

### Using the Tool From an iPad (Codespaces Workflow)

If you’re mobile:
	1.	Upload the script and your evidence to GitHub
	2.	Open GitHub Codespaces on the iPad
	3.	In the Codespaces terminal, run:

  ```bash
  python3 evidence_hasher.py -r
  ```

  4.	Download manifest.csv
	•	Right-click the file in the Codespaces sidebar
	•	Choose Download

This gives you full forensic hashing capability from anywhere.

⸻

### Best Practices for Evidence Handling

To maintain defensible chain-of-custody:
	•	Hash files before sending them anywhere
	•	Store the manifest alongside the evidence
	•	Re-verify the manifest before each transfer
	•	Never alter evidence after hashing
	•	Keep a secondary backup of both evidence and manifest
	•	Use encrypted archives for long-term storage

These steps ensure your documentation remains admissible, tamper-evident, and professionally maintained.

### Conclusion

The Evidence Hasher provides a practical, repeatable, and forensically reliable method to document digital evidence.
It supports:
	•	legal cases
	•	human rights documentation
	•	corporate audits
	•	incident response
	•	digital forensics
	•	chain-of-custody workflows

Its output is simple, trustworthy, and defensible — enabling you to prove the authenticity and integrity of every file you collect.

