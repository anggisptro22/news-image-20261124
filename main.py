import os
import sys
from pathlib import Path

def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    src = Path("entry.png")
    
    if not src.is_file():
        print(f"Error: Required file '{src}' is missing.", file=sys.stderr)
        raise FileNotFoundError(f"entry.png is missing at {src.absolute()}")
        
    dst_dir = Path(output_dir)
    dst_dir.mkdir(parents=True, exist_ok=True)
    dst = dst_dir / "entry.png"
    
    # Byte-for-byte copy
    with open(src, "rb") as f_in, open(dst, "wb") as f_out:
        while chunk := f_in.read(8192):
            f_out.write(chunk)
            
    print(f"Successfully copied {src} to {dst}")

if __name__ == "__main__":
    main()
