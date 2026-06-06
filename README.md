# sing-box-bin

A Python wrapper for sing-box binary releases

Bundled binaries:

- Linux AMD64: `sing-box-linux-amd64`
- Linux ARM64: `sing-box-linux-arm64`
- Windows AMD64: `sing-box-windows-amd64.exe`

Patch releases such as `1.13.13.post1` are packaging-only fixes for the same
upstream sing-box version.


## build and bump version

```bash
.\scripts\build.sh "vx.y.z"
git add src/sing_box_bin/bin/
git commit -m "feat: update sing-box binary to version vx.y.z"
uv tool install bump-my-version
bump-my-version bump --new-version vx.y.z --commit --tag
git push origin main --tags
```

## install

```bash
uv add sing-box-bin
```

## usage

```python
from sing_box_bin import get_bin_path

>>> get_bin_path()
>>> Path(./sing-box-bin/bin/sing-box-windows-amd64.exe)
```
