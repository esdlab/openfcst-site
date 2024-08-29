# Adding Content to the Sidebar

1. In this directory, there are a number of subdirectories corresponding to sidebar categories.  
Navigate to the directory most related to your change.

2. Create a new file with any name, except it must end in `.md`. The file should contain the following content:

```markdown
+++
title = "<TITLE>"
date = "YYYY-MM-DD"
+++
<DESCRIPTION>
```

> **Date**  
> The date parameter is required and must be in the format `YYYY-MM-DD`.  
> The projects are sorted newest to oldest when displayed on the webpage.  
> _The weight parameter may be used instead for the same purpose._

# Adding Sidebar Categories

To add new sidebar categories (which are displayed in different headings on the sidebar):

1. Create a new subdirectory in this directory (`content/sidebar`) with any name.
2. Inside the new directory, create a new file named `_index.md` (don't forget the underscore).  
The file should contain the following content:

```markdown
+++
title = "<SIDEBAR CATEGORY NAME>"
weight = 1
[build]
    render = "never"
[[cascade]]
    [cascade.build]
        list = "always"
        publishResources = false
        render = "never"
+++
An optional, brief description of the research category.
```

> **Note**  
> The text below `[build]` should not be changed.

> **Weight**  
> The `weight` parameter determines the order in which the sidebar categories are displayed.  
> Lower weights are displayed first.  
> _The date parameter may be used instead for the same purpose._

# Example
The [_example/ directory](_example) is an example of a sidebar category.  
The [_example/_example.md directory](_example/_example.md) is an example of a post in the example sidebar category.  
Copy and paste these directories and modify it if you wish.
