import os
import platform
import sys
from pathlib import Path

__all__ = ["get_bin_path"]

__version__ = "1.13.21"


def get_bin_path() -> Path:
    base_path = Path(__file__).parent / "bin"

    if sys.platform == "win32":
        bin_path = base_path / "sing-box-windows-amd64.exe"
    elif sys.platform.startswith("linux"):
        machine = platform.machine().lower()
        if machine in {"x86_64", "amd64"}:
            bin_path = base_path / "sing-box-linux-amd64"
        elif machine in {"aarch64", "arm64"}:
            bin_path = base_path / "sing-box-linux-arm64"
        else:
            raise RuntimeError(f"Unsupported Linux architecture: {machine}")
    else:
        raise RuntimeError(f"Unsupported platform: {sys.platform}")

    if not bin_path.exists():
        raise FileNotFoundError(f"Binary not found at {bin_path}")

    if sys.platform != "win32":
        st = os.stat(bin_path)
        os.chmod(bin_path, st.st_mode | 0o111)

    return bin_path
