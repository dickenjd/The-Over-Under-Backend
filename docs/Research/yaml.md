# YAML Research
## General

Source: [Basic YAML Tutorial](https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started)

### YAML Introduction
From our source at CloudBees "YAML Ain't Markup Language (YAML) is a data serialization language that is consistently listed as one of the most popular programming 
languages. It's often used as a format for configuration files, but its object serialization abilities make it a viable replacement for languages like JSON."

YAML has become one of the most used languages for unit and lint test integration over the last several years. YAML can be written to test and lint almost every
programming language to confide to almost any software engineering standard in the world. This kind of tool is powerful and useful to understand, as it can make
testing code in almost any scenario near effortless with sufficent knowledge of the language. YAML also has other powerful capabilities, such as it's use in github
actions to automate features of specific code.

YAML is in it's own way a type of scripting language, as its files will contain a set of instructions for a compiler to read off of, which can be executed in 
various amounts of ways, such as time, on pushes of other code, on execution of other programs, and more. 

YAML is also extremely similar to JSON, with the main difference being that YAML sacrifices some of it's configuration abilities to provide more indepth scripting.

YAML can also be used with docker to run specific instructions off of containers, which is seen amongst GitHub Actions.

### Reading and Writing YAML Files
Using this example from our source, we can breakdown a YAML file and its capabilities.
```yaml
---
 doe: "a deer, a female deer"
 ray: "a drop of golden sun"
 pi: 3.14159
 xmas: true
 french-hens: 3
 calling-birds:
   - huey
   - dewey
   - louie
   - fred
 xmas-fifth-day:
   calling-birds: four
   french-hens: 3
   golden-rings: 5
   partridges:
     count: 1
     location: "a pear tree"
   turtle-doves: two
```

YAML files start with three dashes to indicate the beginning of a new YAML document or seperate instruction. YAML supports being compiled in most standard languages,
and uses this distinction for each compiler to know it is reading YAML instruction.

YAML files contain keys, which are just pointers to different types of values such as strings, floats, integers, or booleans. Strings do not need to be enclosed in
paranthesis. In this file, "doe", "ray", "pi", "xmas", and "french-hens" are all keys.

YAML files also contain arrays, as seen with "calling-birds" each value in an array is seperated by a dash with its value. The number of spaces are allowed to vary,
but YAML cannot read tabs.

YAML files can contain dictionaries, and these can hold any range of values from keys, arrays, to more dictionaries inside of them. This is denoted in "xmas-fifth-day"

You can use this to your advantage by modifying these data types into executing commands, as seen in the Super Linter written in our second source. The code is listed
below:

```yaml
---
name: Super-Linter

on: push

jobs:
  super-lint:
    name: Lint code base
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Run Super-Linter
        uses: github/super-linter@v4
        env:
         DEFAULT_BRANCH: main
         GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
         SUPER_LINTER_EXCLUDE: |
           "**/*.md"
           "**/*.txt"
```

Certain keywords have the ability to execute specific commands, as seen here to run a Super Linter, which can be used to Lint through code in any standard programming
language. The command "on" refers to exactly when this file will execute, which is set to execute anytime new code is pushed to this repo. "jobs" is a dictionary
defining the list of jobs the file will perform when executed on push. 

Inside of jobs is two more dictionaries, named "super-lint", and "steps". Super-lint is the name of the job that is being executed on push and the 
values inside are naming the action of linting the code base and determining the container the file will be ran on, which here is using the latest 
update of Ubuntu provided by GitHub Actions. 

Each dash with a "name" beside it is a step that the super linter is running to lint the code, and inside each name dash is the set of instructions that step is
performing.

The uses key is a source the YAML file is reading off of to determine what is necessary to perform that specific step.

# Correcting issues in YAML Linters
## General

Source: [Introduction To Github Actions CI/CD](https://www.youtube.com/watch?v=mFFXuXjVgkU)

Any lines of code that have a "+" sign indicate adding a line with the code to the right of the plus sign into the code of that file.

Any lines of code that have a "-" sign indicate removing that specific line of code from that file. A "-" sign on a line with no code indicates that there is
additional white space in the file that needs to be removed.
