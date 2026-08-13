# Version History

| Version | Branch | Commit Message | Description |
|---|---|---|---|
| V1 | main | Initial project setup | Created project with main.py, students.py and README.md |
| V2 | main | Add student information | Added student name, enrollment number and marks |
| V3 | main | Add average marks calculation | Added average marks calculation |
| V4 | main | Add student search feature | Added student search by enrollment number |
| V5 | main | Improve input validation | Added marks validation and documentation |
| V6 | feature-grade | Add grade calculation | Added A/B/C/D/F grade calculation |
| V7 | feature-grade | Improve grade calculation | Added validation to grade calculation and updated README |
| V8 | main | Update student display | Changed student display message on main branch |
| V9 | feature-grade | Update feature display | Changed the same display message on feature branch to intentionally create a conflict |
| V10 | main | Resolve merge conflict | Resolved the conflict and successfully merged feature-grade into main |

## Git Analysis

1. **Number of commits:** 10
2. **Feature branch:** `feature-grade`
3. **Feature developed:** Grade calculation based on marks
4. **Conflicting file:** `students.py`
5. **Why the conflict occurred:** The `main` and `feature-grade` branches changed the same display-message line differently.
6. **How it was resolved:** The conflicting line was replaced with the final agreed message, then the file was staged and committed.
