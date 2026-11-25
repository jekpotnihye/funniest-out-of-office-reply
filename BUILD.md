# Build notes

## Competition

Funniest One-Line Out-of-Office Reply
(`u-hamsyh-funniest-one-line-out-of-office-reply-5490c1c8`).
Gate: `/output/entry.txt` must be UTF-8 text of 1 to 160 characters,
not only white space. The kit supplied no starter template (only
`RULES.txt`, `competition.yaml`, the CLI, and harness files), so the
repository starts with an empty initial commit and every entry file
below was authored in this session.

## Judge brief, in criterion order

1. A one-line out-of-office reply, the sort a person sets before
   going away. Anything else loses to any reply that is one.
2. The laugh lands on the first read, with no setup and nothing
   to explain afterwards.
3. It still reads like a real away message a person would be glad
   to switch on, not a notice with a joke bolted to it.
4. The joke is fresh: a turn on the usual away message rather than
   the same beach, inbox, or limited-email lines.
5. Short enough to take in at a glance, with every word earning
   its place. A reply needing a signature or name is weaker than
   one that stands alone. Length for its own sake does not count.

The twist belongs in the last word or words, and the cap is a
ceiling, not a target.

## Variants drafted

Three original variants were drafted against the brief; none reuses
a line from another competition, and none reproduces a house text.

1. "Out of office until Monday; the same spreadsheet is in charge,
   unsupervised." — chosen and polished (see below).
2. "Away until Monday; I left my work with my future self, who has
   already resigned." — rejected: the resignation turn reads more
   like a joke bolted to an away notice than a message to switch on.
3. "Out of office — I am taking the holiday my calendar kept
   declining." — rejected: weaker first-read laugh, and "holiday"
   drifts toward the usual away-message scenery the brief warns
   against.

## Polishes of the winner (each re-run and verified byte-for-byte)

- Draft: "I am out of office until Monday; my replacement is the
  same spreadsheet, now unsupervised." (90 characters)
- Polish 1: cut "I am" to "Out of office", tightening the opening
  so the away message lands at once. (85 characters)
- Polish 2: "I left the same spreadsheet in charge, unsupervised."
  Stronger handover voice; the twist stays in the last word.
  (80 characters)
- Polish 3 (final): "the same spreadsheet is in charge,
  unsupervised." Filler cut; every remaining word earns its place.
  (76 characters)

## Verification

The program was run repeatedly, including at the default
`/output/entry.txt` path and via an `OUTPUT_PATH` override. Every
run produced byte-identical output: 76 characters, 76 bytes, no
trailing newline, SHA-256
`ba05f50dcd8a8b621a55df3216b753cda1b4dc7bcd0c0ef797c22037589451ab`.

## Files

- `main.py` — entrypoint; writes the entry verbatim.
- `README.md` — description and run instructions; the coordinator
  adds the three live make.fun badge lines at the top.
- `BUILD.md` — this file.
- `LICENSE` — MIT.
- `.gitignore` — keeps the kit and local output out of the repo.
- `.makefun/owner.json` — payout wallet.
