# Adding News

1. Create a new directory with any name.  
_This name is what will appear in the URL of the page._

2. Inside the new directory, create a new file named `index.md`. The file should contain the following content:

```markdown
+++
title = "<NEWS POST TITLE>"
date = "YYYY-MM-DD"
tags = ["x", "y", "z"]
+++
<NEWS POST CONTENT>
```

> **Date**  
> The date parameter is required and must be in the format `YYYY-MM-DD`.  
> The news posts are sorted newest to oldest when displayed on the webpage.

> **Tags**  
> The optional tags parameter accepts a list of strings. These will be displayed under the title.  
> The tags can be anything, preferably not plural.  
> _Examples include: "experiment", "simulation", "design"_

All images (any format) placed in this directory will be displayed in a slideshow, in alphabetical order by file name.

# Example
The [_example/ directory](_example) is an example of the correct setup.  
Copy and paste this directory and modify it if you wish.
