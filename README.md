# Walphabet

Transform your fonts from TTF or OTF to WOFF2.

# Download

## Linux

## MacOS

Perhaps in the future.

## Windows

Perhaps in the future.

# Development

## 1. Install requirements

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## 2. Build

### Linux

```bash
pyinstaller main.spec
```

### Windows

```bash
venv\Scripts\pyinstaller.exe main.spec
```

### MacOS

Install `python-tk`.

```bash
brew install python-tk
```

Next.

```bash
pyinstaller main.spec
```

## 3. Run

```bash
./dist/walphabet
```

## GUI

```bash
pip3 install pygubu-designer
```

and then run `pygubu-designer`.