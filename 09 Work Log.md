---
type: log
owner: Both
tags: [fin3010, log]
---

# Work Log

Everything that happens on this project, newest at the bottom. **Both of us and Claude add an entry at the end of every work session** — even a one-liner. This is also our evidence for "how we prompted our way there" in the post.

**Entry format:** date · who · what happened · decisions · files/commits · open items

---

### 2026-11-17 · Blake + Claude — setup
- Uploaded nothing yet; agreed Claude will build a **Tier 3** case study option and document it in an Obsidian vault.
- Compared ways for the partner to connect his own account: Obsidian Sync shared vault (paid, both need subscriptions), GitHub + Obsidian Git plugin (free), shared Google Drive/OneDrive (free, easiest, but conflict copies and no real history).
- **Decision:** GitHub repo for the vault, kept **separate** from Google Drive (a Git repo inside a Drive-synced folder can corrupt `.git`).
- **Decision:** connect Claude through the claude.ai GitHub connection rather than pasting a personal access token into chat.
- Created repo `blakedjoplin/Fin_Case_Study_FL2026`; Claude attached it with push access and cloned it (empty repo).
- Partner access: Blake adds partner under repo Settings → Collaborators; partner clones with his own GitHub login.

### 2026-11-26 (~11:04 MT) · Blake + Claude — idea ranking
- Uploaded `Case_Studies_export_1.zip`: assignment handout + case files and AI brainstorm lists for Units 1, 4, 5, 6, 8, 9 (Unit 9 had no brainstorm list).
- Read the handout: due **Wed Dec 2, 11:59 PM**; 40-pt rubric; each partner posts own version.
- Claude ranked all **50 ideas** (Tier 3 → Tier 2 → Tier 1) on difficulty, LinkedIn appeal, and time. Full table now in [[02 Idea Selection]] (appendix).
- Claude's recommendation: Unit 6 Tier 3 #10 *What would AI data centers have to earn?*; runner-ups Unit 8 #10 (alpha) and Unit 5 #8 (Dow vs S&P).

### 2026-11-26 (~11:09 MT) · Blake + Claude — plan, model, concepts
- **Decision:** go with Unit 6 Tier 3 #10.
- Claude web-searched 2026 capex guidance, Q3 2026 cloud revenue, and server useful-life changes (leads only — not yet verified in primary sources). Lead total: **~$730B** (Amazon ~$220B, Alphabet $195–205B, Meta $135–145B, Microsoft ~$170B CY).
- Claude built the break-even model: $730B @ 10%, 6 yrs → **$167.6B/yr** after-tax cash flow. Hand-checked: BA II Plus `N=6, I/Y=10, PV=-730, CPT PMT`; Python NPV check = 0.00.
- Found three AI-error candidates (see [[07 AI Error Log]]): capex totals ranging $630B–$745B by date/definition; "$33.2B Azure revenue" that Microsoft may not actually disclose; first-pass capex-vs-revenue comparison = the Apex VP's mistake.
- Wrote vault notes 00–08 + README + `.gitignore`. Commit `85967d5` pushed to `main`.
- Claude drew three deliverable concept sketches in chat (A: interactive break-even dial, B: scenario bar chart, C: life × return heatmap). Described in [[06 Deliverable Concepts]].
- **Open:** partner's name for owner tags; pick hero chart (B or C); Friday = verify every number in primary sources.

### 2026-11-26 (~11:14 MT) · Blake + Claude — logging
- Blake asked to log everything. Claude created this note, backfilled entries from Nov 17, and added the full 50-idea ranking to [[02 Idea Selection]].
- Clarified: Claude reaches the vault **through GitHub only** — local edits must be pushed before Claude can see them; Claude pulls before each session.
