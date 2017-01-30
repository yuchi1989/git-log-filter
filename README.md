# git-log-filter

### Introduction
This is a tool that can filter the commits from git log by key words. And it supports logical expression.  

Filter commits file git_log.txt by "A and (B or C) and (D or E or F)", where A, B, C, D, E and F are key words.
```shell
python3 gitlogfilter.py git_log.txt "A" "B||C" "D||E||F"
```
### Example
If we want to get the commits that contain "bug" and either "copy" or "leak", we can use this tool as follows.
```shell
python3 gitlogfilter.py git_log.txt "bug" "copy||leak"
```
