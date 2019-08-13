# j2scr: Avoid Jinja2 boilerplate for small scripts
This is a very simple package that wraps Jinja2.
The purpose is to avoid boilerplate for micro-scripts that use jinja.
This is achieved by setting a default jinja environment, a filesystemloader searching the
current dir, and providing utility functions `render`, `render_to_file`, and `set_options`.

Use as such:

```python
from j2scr import render, render_to_file, set_options

# You can render into a variable
string_with_content = render("my_template.j2", var=2, var2='Michael')
# Or into a file
render_to_file("my_template.j2", "my_content." var=2, var2='Michael')

# You can optionally change the loader parameters (do it before rendering, of course):
set_options(encoding="latin-1", searchpath="/some/other/fixed/dir", followlinks=True)
# The set_options function also supports modifying the environment (eg. filters or newline_sequence)
# Alternatively the environment and loaders are available as attributes.
```

If for some reason you want the minimalism of `j2scr` but without the global settings (eg. for a
class), you can use the `j2scr.J2Scr` class which works the same way but has it's own env and loader.
