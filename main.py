"""
SpendWise - start here.

    python main.py                       normal start
    python main.py --data-dir demo_data  use a different data folder (testing)
"""

import argparse
import sys


def _fail(message: str) -> None:
    """Show a readable error even when there is no console (the .exe)."""
    try:
        import tkinter
        from tkinter import messagebox
        root = tkinter.Tk()
        root.withdraw()
        messagebox.showerror("SpendWise", message)
        root.destroy()
    except Exception:
        pass
    if sys.stderr:
        print(message, file=sys.stderr)
    sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(description="SpendWise personal expense tracker")
    parser.add_argument("--data-dir", help="folder to keep the data files in")
    args, _unknown = parser.parse_known_args()

    # Crisp text on high-resolution Windows screens (must happen before the window exists).
    if sys.platform == "win32":
        try:
            import ctypes
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            try:
                ctypes.windll.user32.SetProcessDPIAware()
            except Exception:
                pass

    try:
        import tkinter  # noqa: F401
    except ImportError:
        _fail("Tkinter is missing. Re-run the Python installer, choose Modify, and tick "
              "'tcl/tk and IDLE'.")
    try:
        import matplotlib  # noqa: F401
    except ImportError:
        _fail("The 'matplotlib' package is not installed.\n\nIn the VS Code terminal run:\n"
              "pip install -r requirements.txt")

    from spendwise.app import SpendWiseApp
    SpendWiseApp(data_dir=args.data_dir).mainloop()


if __name__ == "__main__":
    main()
