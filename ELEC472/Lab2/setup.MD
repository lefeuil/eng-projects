### Setup local envronment

Environment can be directly created using python `venv` module or `conda`. In this example, we will be using `conda` to create an environment. You may choose an IDE of your choice, a good suggestion would be [VS Code](https://code.visualstudio.com/).

**Basic setups** 

You may follow the instructions available here in the following links to install `conda` in your local system.

Links to install conda for their respective OS platforms.
- [windows](https://docs.anaconda.com/anaconda/install/windows/)
- [linux](https://docs.anaconda.com/anaconda/install/linux/)
- [mac](https://docs.anaconda.com/anaconda/install/mac-os/)

Create environment:
`conda create --name elec472 python=3.10
`

Activate the environment:
`conda activate elec472
`

Note: Sometimes, after installing `conda`, you may face the error `Conda command is not recognized`; In that case, you need to manually specify the `conda` path in the `PATH` variable. e.g., in linux: `export PATH=~/anaconda3/bin:$PATH`. You may read more on this issue in the `stackoverflow` thread: 
https://stackoverflow.com/questions/44597662/conda-command-is-not-recognized-on-windows-10

Installing other packages: 

```
pip install matplotlib

```