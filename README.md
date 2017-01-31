# git-log-filter

### Introduction
This is a tool that can filter the commits from git log by key words. And it supports logical expression.  

Filter commits file git_log.txt by "A and (B or C) and (D or E or F)", where A, B, C, D, E and F are key words.
```shell
python3 gitlogfilter.py git_log.txt "A" "B||C" "D||E||F"

```
And space inside each argument does matter.  
For example, the following two commands will output different results.
```shell
python3 gitlogfilter.py git_log.txt "A" "B||C"  
python3 gitlogfilter.py git_log.txt "A" " B ||C"

```
### Example
If we want to get the commits that contain exactly "bug" and either "copy" or "leak", we can use this tool as follows.
```shell
python3 gitlogfilter.py git_log.txt " bug " " copy || leak "
```

If we want to get the commits that contain "bug" including "buggy", "bugs" and so on, we can use this tool as follows.
```shell
python3 gitlogfilter.py git_log.txt " bug"
```
### Future work
The regular expression support will be future work. I will implement it soon.
