#!/usr/bin/env python3
"""Fails when the public playbook carries private details: people other than the author's public first name, other
businesses, account and card identifiers, emails, phone numbers, local paths and private links. Run on every pull
request (.github/workflows/privacy.yml) and before any port from the private edition. Exit 1 lists each hit."""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
FILES = [p for p in ROOT.rglob("*") if p.suffix in (".md", ".json", ".txt", ".yml", ".yaml") and ".git" not in p.parts
         and p.name != "privacy_check.py"]
WORDS = r"Tony|Sandro|Mtsariashvili|Llucky|Lluckyai|LuckLucky|Receptly|Dentor|Dadvani|Garrison|Dental Hub|Dent ?Inn|" \
        r"Vedreba|Tamik|Shortex|Elizaveta|mwarevito|Tide|vito@|tony@|givi-chat|givi-agent|tony-hermes"
PATTERNS = {
    "private name or business": re.compile(r"\b(?:%s)\b" % WORDS, re.I),
    "email address": re.compile(r"[\w.+-]+@(?!example\.com|yourdomain\.com|yourbusiness\.com)[\w-]+\.[a-z.]{2,}", re.I),
    "card or account ending": re.compile(r"(?:····|\u2022{3,}|\*{2,4}|ending in)\s?\d{4}\b"),
    "platform account id": re.compile(r"\bact_\d{6,}|\b\d{15,}\b"),
    "uuid": re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I),
    "phone number": re.compile(r"\+\d[\d ()-]{8,}\d"),
    "local path": re.compile(r"/Users/|~/coding|C:\\\\Users", re.I),
    "private link": re.compile(r"claude\.ai/(?:artifact|code)/|railway\.app/project/|supabase\.co/dashboard/project/", re.I),
}
ALLOW = re.compile(r"hello@heygivi\.com|mwarevito/venture-launch-playbook|claude\.ai/code/routines")


def main():
    hits = []
    for path in FILES:
        for n, line in enumerate(path.read_text(encoding="utf-8", errors="ignore").splitlines(), 1):
            clean = ALLOW.sub("", line)
            for why, pattern in PATTERNS.items():
                for m in pattern.finditer(clean):
                    hits.append("%s:%d: %s: %r" % (path.relative_to(ROOT), n, why, m.group(0)))
    for hit in hits:
        print(hit)
    print("privacy check: %d hit(s) in %d files" % (len(hits), len(FILES)))
    return 1 if hits else 0


if __name__ == "__main__":
    sys.exit(main())
