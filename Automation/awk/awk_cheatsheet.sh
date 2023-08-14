### AWK Cheatsheet

**Basics**:
- `awk` processes files line by line.
- `awk` splits each input line into fields.
- Fields are referenced as `$1`, `$2`, `$3`, etc. `$0` refers to the entire line.

**Basic Usage**:
- Print entire file: `awk '{print}' filename`
- Print specific field (e.g., 2nd): `awk '{print $2}' filename`

**Patterns and Actions**:
- Format: `awk 'pattern { action }' filename`
- Example: Print lines containing "example": `awk '/example/ {print}' filename`

**Built-in Variables**:
- `NF`: Number of fields in the current record.
- `NR`: Current record number.
- `FS`: Field separator (default is whitespace).
- `OFS`: Output field separator.

**Examples**:
1. Print last field of each line: `awk '{print $NF}' filename`
2. Print line numbers alongside lines: `awk '{print NR, $0}' filename`
3. Change field separator: `awk -F':' '{print $1}' filename` (for colon-separated files)
4. Sum a column (e.g., 1st) and print total: `awk '{sum+=$1} END {print sum}' filename`

**Control Structures**:
- **if statement**: 
  ```awk
  awk '{ if ($1 > 50) print $0 }' filename
  ```
- **for loop**:
  ```awk
  awk '{ for (i = 1; i <= NF; i++) print $i }' filename
  ```

**Functions**:
- **length**: Find the length of the string.
  `awk '{print length($1)}' filename` prints the length of the first field.
- **substr**: Extract substring.
  `awk '{print substr($1, 2, 3)}' filename` prints 3 characters of the first field starting at the second character.

**Multiple Patterns and Actions**:
```bash
awk '
/example1/ {print "Found example1"}
/example2/ {print "Found example2"}
' filename
```

This is a concise cheatsheet to get you started with `awk`. However, `awk` is a very powerful tool with many more capabilities and options. Consider diving into its man pages or detailed tutorials for more in-depth exploration.
