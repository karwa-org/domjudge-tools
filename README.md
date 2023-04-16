# domjudge-tools

Tools to make contest organizer's lives easier.

## `frama2domjudge`

Convert Framaforms output to a TSV input that can be directly uploaded to the DOMjudge platform.
Use it as such:

```console
cat framaform.tsv | python frama2domjudge.py > accounts.tsv
```
