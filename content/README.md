# Adding Content

The `content` directory contains subdirectories for each page on the webpage.

## Table of Contents

To add new content or modify existing content on the webpage, please view the `README.md` in whichever directory corresponding to the page you wish to edit.

In each section, anything enclosed within angle brackets (`< >`) should be replaced with the appropriate content.  
_For example, `<RESEARCH PROJECT NAME>` should be replaced with the name of the research project._

- [About](about)
- [Authors](authors)
- [Documentation](docs)
- [Downloads](downloads)
- [News](news)
- [Sidebar](sidebar)
- [Sponsors](sponsors)

## Miscellaneous
The following sections explain how to make specific changes that do not fit in the aforementioned categories.

### Static Directory
Any files in the [static/ directory](/static) are copied to the root directory of the webpage when it is deployed.  
Use this directory for assets that do not belong in the [content/ directory](/content).  
For an example of this, see [Changing Logo](#changing-logo), or the links on the [documentation page](docs/_index.md).

### Home Page
- To change the text written on the home page, edit the [\_index.md](_index.md) file in this directory.
- To change the images in the home page's slideshow, see the [About Page README](content/about)

### Changing Logo
To change the logo displayed in the navigation bar and footer, edit [/layouts/partials/logo.html](/layouts/partials/logo.html).  
You can change anything within the `#logo` div element. Do not remove this element.

To add new images to the logo, add them anywhere you desire in the [static directory](#static-directory), then ensure the paths are from the persective of the static directory.

### Changing Navbar and Footer Buttons
The buttons in the navigation bar and the footer are defined in [hugo.toml](/hugo.toml).

To add a new button to the navigation bar, copy and paste these four lines and make any desired changes.

```toml
[[menus.nav]]
name = "<BUTTON NAME>"
pageRef = "<RELATIVE LINK TO DESTINATION PAGE>"
weight = 1
```

To add a new button to the footer, copy and paste these four lines and make any desired changes.

```toml
[[menus.footer]]
name = "<BUTTON NAME>"
pageRef = "<RELATIVE LINK TO DESTINATION PAGE>"
weight = 1
```

> **Weight**  
> The `weight` parameter determines the order in which the equipment types sections are displayed.  
> Lower weights are displayed first.

### Favicon
The favicon displayed in the tab for the webpage is located in [/assets/favicon.ico](/assets/favicon.ico). Replace this file, but do not change the file name.

### CSS Stylesheets
The styles for the webpage are located in [/assets/overrides.css](/assets/overrides.css). Unlike the HTML of this webpage, this stylesheet is regular CSS with nothing special. The `:root` style defines colors used throughout the page.

If there is a change you want to make that isn't in this stylesheet, it is likely in the [theme's stylesheet](https://github.com/jadc/lab-theme/blob/main/assets/base_style.css); it is unlikely you should change this file, and anything in [/assets/overrides.css](/assets/overrides.css) will override this file.

### Figures

You can add an image with a caption to any markdown file with the following syntax.

```markdown
{{< figure src="PATH TO IMAGE" caption="CAPTION" >}}
```

Ensure the path leads to an image relative to the markdown file. The easiest method would be to place the image in the same directory as the markdown file. For example:

```markdown
{{< figure src="group_photo.jpeg" caption="A photo of the group" >}}
```

If you wish to have the figures adjacent to one another, use the following syntax:

```markdown
<div class="adjacent">
    {{< figure src="PATH TO IMAGE" caption="CAPTION" >}}
    {{< figure src="PATH TO IMAGE" caption="CAPTION" >}}
</div>
```

As you might have noticed, this is regular HTML. This is allowed in markdown documents, but I suggest keeping it to a minimum.
