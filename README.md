# CSV Tracker

## Introduction

The intention of this program is to be an exercise in pushing the usage of CSV files for tracking items and their relations.

## Main functions

### Creating a new table

The creation of a table (_ie_ CSV file) requires the name of the headers to be provided.
Some hidden headers are created by default (task ID, nesting level, parent task).
These headers, or columns, can be re-ordered if need be.

### Tasks management

- Task creation
- Task update
- Task removal

### Status display

- Display current global status and progress
- Display current task status and progress ; including subtasks

## Roadmap

- Once the project runs on Python terminal, create a proper TUI
  - look into customisation possibilities
- Create a way to consult the status via a web browser
