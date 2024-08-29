# OpenFCST Webpage

This is a repository containing the source code for the OpenFCST redesigned webpage.

If you have any questions, feel free to open an issue or e-mail jchehimi(at)ualberta.ca.

## Contribution

To contribute new content, follow the steps below:

1. Clone the repository:

```bash
git clone https://github.com/esdlab/openfcst-site.git
```

2. You are not allowed to push changes directly to the `main` branch.  
You must make changes in your own branch, then open a pull request.

```bash
git checkout -b <branch-name>
```

3. To contribute content (i.e. people, news posts, edit text, etc.) you only need to modify the [content directory](content).  
[Click here for more information on how to add specific types of content](content).  
If you are unsure, chances are you are only modifying content.

4. Once you have made your changes, commit them to your branch:

```bash
git add -A
git commit -m "Your commit message here"
git push origin <branch-name>
```

5. Open a pull request on GitHub to merge your changes into the `main` branch.  
The pull request will be automatically tested, and once merged, automatically deployed.

## Development

If you wish to make more drastic changes to webpage (e.g. layout, styles, scripts) then you will likely want to compile the webpage locally.

This webpage makes extensive use of the [Hugo static site generator](https://gohugo.io). If you wish to make advanced changes to the webpage, I highly recommend [reading their documentation](https://gohugo.io/documentation).

1. Install [Hugo](https://gohugo.io/getting-started/installing/).

2. After cloning the repository, in the root of the repository, run the following command:

```bash
hugo server
```

3. Open your browser and navigate to "http://localhost:1313" to view the webpage.  
As you make changes to the source code, the webpage will automatically refresh.
