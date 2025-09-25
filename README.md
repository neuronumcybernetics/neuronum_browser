<h1 align="center">
  <img src="https://neuronum.net/static/neuronum.svg" alt="Neuronum" width="80">
</h1>
<h4 align="center">Neuronum Browser v0.0.1</h4>

<p align="center">
  <a href="https://neuronum.net">
    <img src="https://img.shields.io/badge/Website-Neuronum-blue" alt="Website">
  </a>
  <a href="https://github.com/neuronumcybernetics/neuronum">
    <img src="https://img.shields.io/badge/Docs-Read%20now-green" alt="Documentation">
  </a>
  <a href="https://pypi.org/project/neuronum/">
    <img src="https://img.shields.io/pypi/v/neuronum.svg" alt="PyPI Version">
  </a><br>
  <img src="https://img.shields.io/badge/Python-3.8%2B-yellow" alt="Python Version">
  <a href="https://github.com/neuronumcybernetics/neuronum/blob/main/LICENSE.md">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License">
  </a>
</p>

------------------

### **About the Neuronum Browser**
An real-time E2E Browser built on the [Neuronum network](https://github.com/neuronumcybernetics/neuronum)

### Requirements
Python installed

------------------

### **Create Directory**
```sh
mkdir neuronum_browser
```

```sh
cd neuronum_browser
```

```sh
git clone https://github.com/neuronumcybernetics/neuronum_browser
```

------------------

### **Build the Browser**
```sh
pip install pyinstaller
```

```sh
pyinstaller --windowed --name "Neuronum Browser" --icon=icon.icns --add-data=templates:templates --add-data=static:static app.py
```