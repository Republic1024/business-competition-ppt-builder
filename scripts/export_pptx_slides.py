#!/usr/bin/env python
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Export PPTX slides to PNG using Microsoft PowerPoint COM on Windows."
    )
    parser.add_argument("pptx", type=Path)
    parser.add_argument("--outdir", type=Path, default=None)
    parser.add_argument("--slides", default="", help="Comma-separated 1-based slide numbers. Empty exports all.")
    parser.add_argument("--width", type=int, default=1920)
    parser.add_argument("--height", type=int, default=1080)
    args = parser.parse_args()

    try:
        import win32com.client
    except ImportError as exc:
        raise SystemExit("pywin32 is required for PowerPoint COM export on Windows.") from exc

    pptx = args.pptx.resolve()
    outdir = (args.outdir or (pptx.parent / "slide_previews")).resolve()
    outdir.mkdir(parents=True, exist_ok=True)

    app = win32com.client.Dispatch("PowerPoint.Application")
    app.Visible = True
    pres = app.Presentations.Open(str(pptx), WithWindow=False)
    try:
        if args.slides.strip():
            slide_nums = [int(x.strip()) for x in args.slides.split(",") if x.strip()]
        else:
            slide_nums = list(range(1, pres.Slides.Count + 1))
        for num in slide_nums:
            out = outdir / f"slide_{num:02d}.png"
            pres.Slides(num).Export(str(out), "PNG", args.width, args.height)
            print(out)
    finally:
        pres.Close()
        app.Quit()


if __name__ == "__main__":
    main()
