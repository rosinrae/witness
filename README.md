This is a command line journaling app. Nothing I've found for digital 
journaling has met my needs, so I'm rolling my own solution.

remind me to redo this in Haskell or something.

usage:

```
>$ witness <line of text>
```
writes `<line of text>` to `~/journal/<today's date>.txt`

```
>$ witness
```
prints contents of `~/journal/<today's date>.txt`

does nothing if this file does not exist.

`<today's date>` is formatted as yyyy-mm-dd, or strfmt: `%Y-%m-%d`

You'll need python 3 for this to work.
